from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
order = Blueprint('order', __name__, template_folder='../templates')

con = MySQL_query()
params = ["EstablishTime", "EndTime", "Deadline", "SALESMANID", "Price", "State"]

# dummy_state = jsonify({"status": 200})
# Create
@order.route('/api/order/', methods = ['POST'])
def create_order():
    params = ["EstablishTime", "EndTime", "Deadline", "SALESMANID", "Price", "State"]
    fillin = [None] * 6
    body = request.get_json()
    print(body)
    for i in body.keys():
        if i in params:
            continue
        else:
            return "missing params"
    next_id = con.query1("SELECT MAX(ORDERID) FROM DB2019FP.Order;")
    print("Next available id: {}".format(next_id))
    SQL_command = "INSERT INTO DB2019FP.Order VALUES( {}, '{}', '{}' ,'{}' , {} , {}, '{}');".format(next_id[0]+1, body[params[0]], body[params[1]], body[params[2]], body[params[3]], body[params[4]], body[params[5]])
    print("## SQL command to execute: ", SQL_command)
    con.query_insertORdelete(SQL_command)
    return jsonify({"status": 200})

# CHeckings
# Order and assign sales
# Check resource (Machine, SWE, MGR) availability
# # of talent in each field (SWE’s cases < 3)
# server resource
# budget
# Create Projects.
# Allocate SWE, Resources.
# Assign Manager.
# Allocate Dev Team.

@order.route('/api/order/priority', methods = ['GET'])
def get_order_priority():
    SQL_command = "SELECT * FROM DB2019FP.Order ORDER BY Price DESC;"
    query_result = con.queryALL(SQL_command)
    resp = []
    
    cur = con.get_cur()
    print(query_result)
    cur.execute("SELECT * FROM DB2019FP.Order WHERE OrderID=1;")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    
    for i in query_result:
        resp.append(dict(zip(row_headers, i)))
    print(jsonify(resp))

    return jsonify(resp)

@order.route('/api/order/project_state/<orderID>', methods = ['GET'])
def get_ProjectState_of_Order(orderID):
    SQL_command = "SELECT * FROM DB2019FP.Project WHERE ORDERID={}".format(orderID)
    print(SQL_command)
    query_result = con.queryALL(SQL_command)

    cur = con.get_cur()
    print(query_result)
    cur.execute("SELECT * FROM DB2019FP.Project WHERE PROJECTID=1;")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    resp = []
    for i in query_result:
        resp.append(dict(zip(row_headers, i)))

    return jsonify(resp)
    

@order.route('/api/order/salesman/<orderID>', methods = ['GET'])
def get_sales_of_Order(orderID):
    SQL_command = "SELECT * FROM DB2019FP.Salesman WHERE SALESMANID = (SELECT SALESMANID FROM DB2019FP.Order WHERE ORDERID={})".format(orderID)
    print(SQL_command)
    query_result = con.queryALL(SQL_command)

    cur = con.get_cur()
    print(query_result)
    cur.execute("SELECT * FROM DB2019FP.Salesman WHERE SALESMANID=2;")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    resp = []
    for i in query_result:
        resp.append(dict(zip(row_headers, i)))

    return jsonify(resp)
    
@order.route('/api/order/<orderID>', methods = ['PUT'])
def update_order_state(orderID):
    body = request.get_json()
    print(body)
    for i in body.keys():
        if i in params:
            continue
        else:
            return "illegal param: {}".format(i)
    for i in body.keys():
        SQL_command = "UPDATE DB2019FP.Order SET {}='{}' WHERE ORDERID={};".format(i, body[i], orderID)
        print(SQL_command)
        con.query_insertORdelete(SQL_command)
    return jsonify({"status" : 200})


# Read
# Know the current progress of each child project
# Contain a set of projects.  
# Each project itself can link to its own project management page.


# Delete
# An order can be marked as due when the day of 交付 has arrived.
# Release the resources occupied by the projects.


@order.route('/api/order', methods = ["POST"])
def create_api():

    return 