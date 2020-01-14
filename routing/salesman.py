from flask import Flask, render_template, jsonify, request, Blueprint, abort
salesman = Blueprint('salesman', __name__, template_folder='../templates')
from mysql_conf import *
from routing.basic_function import *
import json
con = MySQL_query()

#basic_function: SalesmanExist(SALESMANID)

    # Know what each salesman is accountable for. (sales item)
    # Set KPI for each of the salesmen.
# Show the customer SalesMan are related to
# Update the time period for the salesman in the company (repeat)
# Promote a salesman to Manager or Senior salesman

# Create salesman
@salesman.route('/api/salesman/', methods = ['POST'])
def create_salesman():
    params = ["Name", "Ssn" , "Title", "Salary" , "Age", "YearsOfExperience", "Address","Gender", "State"]
    body = request.get_json()
    for i in body:
        if i in params:
            continue
        else:
            return "missing params"
    TABLE = "DB2019FP.Salesman"
    now_id = con.query1("SELECT MAX(SALESMANID) FROM {};".format(TABLE))

    SQL_command = "INSERT INTO {} VALUES( {}, {}, {} ,'{}' , {} , {}, {}, {}, {}, {});".format(TABLE, now_id[0]+2, body[params[0]], body[params[1]], body[params[2]], body[params[3]], body[params[4]], body[params[5]],body[params[6]],body[params[7]],body[params[8]])
    print("## SQL command to execute: ", SQL_command)
    con.query_insertORdelete(SQL_command)
    #TBD: how to return insert results
    return jsonify({"status": 200})

@salesman.route('/api/salesman/order_experience/<int:SALESMANID>', methods = ['GET'])
def show_order_experience(SALESMANID):    
    exist = SalesmanExist(SALESMANID)
    if not exist:
        return abort(400, "Salesman id: {} does NOT EXIST".format(SALESMANID))
    TABLE = "DB2019FP.Salesman"
    SQL_command = "SELECT SALESMANID FROM {} WHERE SALESMANID={});".format(TABLE, SALESMANID)
    print("## SQL command to execute: ", SQL_command)
    con.query1(SQL_command)
    
    return


# Select certain Talents of the People
@salesman.route('/api/salesman/<string:Talent>', methods = ['GET'])
def select_by_Talent(Talent):
    #
    pass
    # TODO
    # Select from salesman and salesman where Talent in the variable Talent.
    # You can use some formatting like
    getsalesmanByTalent(Talent)
    # return the result selected


# Show the background, basic info for each person.
@salesman.route('/api/salesman/background', methods = ['GET'])
def get_salesman_info(SALESMANID):
    pass
    # TODO
    getsalesmanInfo(SALESMANID)
    # Select the whole table.
    #SQL:
    #SELECT * FROM salesman
    response = connect.queryAll('SELECT * FROM salesman')

# Update
# Update the time period for the salesman in the company
@salesman.route('/api/salesman/time_period/<int:SALESMANID>', methods = ['PUT'])
def update_salesman(SALESMANID):
    # TODO
    # In request body, there will be a field "period".
    # Update the salesman/salesman having id with "years_of_experience" being "period"
    exist_salesman = salesmanExist(SALESMANID)
    if not exist_salesman:
        return abort(400, "salesman id: {} does NOT EXIST".format(SALESMANID))
    exist_sales = SalesmanExist(SALESMANID)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(SALESMANID))
    if(exist_salesman):
        update_salesman(SALESMANID,  target_attri, new_value, 'salesman')
    else:
        update_salesman(SALESMANID,  target_attri, new_value, 'sales')
    pass

# Delete
@salesman.route('/api/salesman/<int:SALESMANID>', methods = ['DELETE'])
def delete_salesman(SALESMANID):
    # TODO
    exist_salesman = salesmanExist(SALESMANID)
    if not exist_salesman:
        return abort(400, "salesman id: {} does NOT EXIST".format(SALESMANID))
    exist_sales = SalesmanExist(SALESMANID)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(SALESMANID))
    # Delete the record for salesman
    if(exist_salesman):
        changesalesmanState(SALESMANID, 'retired')
    else:
        changesalesmanState(SALESMANID,  'retired')
    pass




#------------------------------------------------------------------
@salesman.route('/api/sales/', methods = ['POST'])
def sales_api():
    return jsonify({"status": 200})

# show the ranking of each salesman by performance.
@salesman.route('/api/sales/ranking/', methods = ['GET'])
def sales_ranking(id):
    # We use the number of projects and a salesman has handled as the KPI.
    # This can be decided afterwards.
    # TODO:
    # 1. Query all the salesman id
    # For each of the salesman id, query their "KPI" data.
    # sort the result by some 
    # sort by the performance ranking 
    return 
