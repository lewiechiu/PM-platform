from flask import Flask, render_template, jsonify, request, Blueprint, abort
swe = Blueprint('swe', __name__, template_folder='../templates')
from mysql_conf import *
from routing.basic_function import *
import json
con = MySQL_query()


# Create swe
@swe.route('/api/swe/', methods = ['POST'])
def create_swe():
    params = ["Name", "Ssn" , "Title", "Salary" , "Age", "YearsOfExperience", "Address","Gender", "State"]
    body = request.get_json()
    for i in body:
        if i in params:
            continue
        else:
            return "missing params"
    TABLE = "DB2019FP.SWE"
    now_id = con.query1("SELECT MAX(SWEID) FROM {};".format(TABLE))

    SQL_command = "INSERT INTO {} VALUES( {}, '{}', {} ,'{}' , {} , {}, {}, '{}', '{}', '{}');".format(TABLE, now_id[0]+2, body[params[0]], body[params[1]], body[params[2]], body[params[3]], body[params[4]], body[params[5]],body[params[6]],body[params[7]],body[params[8]])
    print("## SQL command to execute: ", SQL_command)
    con.query_insertORdelete(SQL_command)
    #TBD: how to return insert results
    return jsonify({"status": 200})

@swe.route('/api/swe/project_experience/<int:SWEID>', methods = ['GET'])
def show_project_experience(SWEID):    
    exist = SWEExist(SWEID)
    if not exist:
        return abort(400, "swe id: {} does NOT EXIST".format(SWEID))
    
    #order expirence
    TABLE = "DB2019FP.Project_SWE"
    SQL_command = "SELECT PROJECTID, COUNT(*) FROM {} WHERE SWEID={} GROUP BY PROJECTID;".format(TABLE, SWEID)
    cursor = con.get_cur()
    cursor.execute(SQL_command)
    projectLis = [i[0] for i in cursor.fetchall()]
    
    #name 
    TABLE = "DB2019FP.SWE"
    SQL_command = "SELECT SWEID, Name FROM {} WHERE SWEID={};".format(TABLE, SWEID)
    cursor.execute(SQL_command)
    ID, Name = cursor.fetchall()[0]

    header = ['SWEID','Name', 'PastProjectsExperience']
    values = [ID, Name, projectLis]
    resp = []
    resp.append(dict(zip(header,values)))

    return jsonify(resp)



# Select certain Talents of the People
@swe.route('/api/swe/get_all_swe_Talent', methods = ['GET'])
def get_all_swe_Talent():
    TABLE = "DB2019FP.Talent"
    SQL_command = "SELECT DISTINCT Talent FROM {} WHERE ID%2 = 1;".format(TABLE)
    print(SQL_command)
    cursor = con.get_cur()
    cursor.execute(SQL_command)
    talentLis = cursor.fetchall()
    res = [talent[0] for talent in talentLis]

    return jsonify(res)

# Select certain Talents of the People
@swe.route('/api/swe/select_by_Talent/<string:Talent>', methods = ['GET'])
def select_by_Talent(Talent):
    exist = TalentExist(Talent)
    if not exist:
        return abort(400, "Talent: {} does NOT EXIST".format(Talent))
    
    return jsonify(SelectByTalent(Talent))


# Show the background, basic info for each person.
@swe.route('/api/swe/background/<int:SWEID>', methods = ['GET'])
def get_swe_info(SWEID):
    exist = SWEExist(SWEID)
    if not exist:
        return abort(400, "swe id: {} does NOT EXIST".format(SWEID))
    
    #SWE
    TABLE = "DB2019FP.SWE"
    SQL_command = "SELECT * FROM {} WHERE SWEID={};".format(TABLE, SWEID)
    cursor = con.get_cur()
    cursor.execute(SQL_command)
    header = [i[0] for i in cursor.description]
    values = [i for i in cursor.fetchall()[0]]
    
    resp = []    
    resp.append(dict(zip(header,values)))

    return jsonify(resp)

# Update
# Update the time period for the swe in the company
@swe.route('/api/swe/update/<int:SWEID>', methods = ['PUT'])
def update_swe(SWEID):
    exist = SWEExist(SWEID)
    if not exist:
        return abort(400, "swe id: {} does NOT EXIST".format(SWEID))

    params = ["Name", "Ssn" , "Title", "Salary" , "Age", "YearsOfExperience", "Address","Gender", "State"]
    body = request.get_json()
    for i in body.keys():
        if i in params:
            continue
        else:
            return "Illeagal params!"
    for i in body.keys():
        TABLE = "DB2019FP.SWE"
        SQL_command = "UPDATE %s SET %s = '%s' WHERE SWEID = %s"%(TABLE, i, body[i], SWEID)
        print(SQL_command)
        con.query_insertORdelete(SQL_command)
    return jsonify({"status": 200})

# Delete
@swe.route('/api/swe/retired/<int:SWEID>', methods = ['PUT'])
def delete_swe(SWEID):
    exist = SWEExist(SWEID)
    if not exist:
        return abort(400, "swe id: {} does NOT EXIST".format(SWEID))

    TABLE = "DB2019FP.swe"
    SQL_command = "UPDATE %s SET %s = '%s' WHERE SWEID = %s;"%(TABLE, 'State', 'retired', SWEID)
    print(SQL_command)
    con.query_insertORdelete(SQL_command)
    print(con.get_cur().rowcount, "record(s) affected")
    return jsonify({"status": 200})


@swe.route('/api/swe/promote/<int:SWEID>', methods = ['PUT'])
def promote_swe(SWEID):
    exist = SWEExist(SWEID)
    if not exist:
        return abort(400, "swe id: {} does NOT EXIST".format(SWEID))
    
    TABLE = "DB2019FP.swe"
    SQL_command = "SELECT Salary FROM {} WHERE SWEID={};".format(TABLE, SWEID)
    print(SQL_command)
    salary = int(con.queryALL(SQL_command)[0][0])
    salary *= 1.1

    SQL_command = "UPDATE %s SET %s = '%s' WHERE SWEID = %s;"%(TABLE, 'Salary', salary, SWEID)
    con.query_insertORdelete(SQL_command)
    print(con.get_cur().rowcount, "record(s) affected")
    return jsonify({"status": 200})


@swe.route('/api/swe/get_customer/<int:SWEID>', methods = ['GET'])
def get_customer_by_swe(SWEID):
    exist = SWEExist(SWEID)
    if not exist:
        return abort(400, "swe id: {} does NOT EXIST".format(SWEID))
    
    TABLE = "DB2019FP.Customer"
    SQL_command = "SELECT CustomerName, CompanyName FROM {} WHERE SWEID={};".format(TABLE, SWEID)
    print(SQL_command)
    CustomerLis = con.queryALL(SQL_command)
    res = []
    header = ['CustomerName', 'CompanyName']
    for c in CustomerLis:
        CustomerName, CompanyName = c
        values = [CustomerName, CompanyName]
        res.append(dict(zip(header,values)))
    return jsonify(res)
