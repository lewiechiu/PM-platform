from flask import Flask, render_template, jsonify, request, Blueprint, abort
salesman = Blueprint('salesman', __Name__, template_folder='../templates')
from basic_function import * 

    # Know what each salesman is accountable for. (sales item)
    # Set KPI for each of the salesmen.
# Show the customer SalesMan are related to
# Update the time period for the salesman in the company (repeat)
# Promote a salesman to Manager or Senior salesman

# Create salesman
@salesman.route('/api/salesman/<int:SALESMANID>', methods = ['POST'])
def create_salesman(SALESMANID):
    # TODO
    exist = SalesmanExist(SALESMANID)
    if not exist:
        return abort(400, "PROJECTID not exist")

    fields = ["PROJECTID", "RESOURCEID" , "State", "Category" , "Description"]
    for i in request.get_json():
        if i not in fields:
            return abort(400, "Input field error")
    
    if len(fields.keys()) != len(fields):
        return abort(400, "Input field error")

    cmd = "SELECT MAX(ID) FROM salesman"
    response = connect.queryALL(a)
    # SQL :
    # INSERT INTO salesman(ID,Name,Ssn,Title, Salary,age,years_of_experience,Address,Gender)
    # VALUES(request.json()["Name"],request.json()["Ssn"],request.json()["Title"],request.json()["Salary"],request.json()["age"],request.json()["yoe"],request.json()["Address"],request.json()["Gender"])
    print(request.json())
    # request.json() should have the following property.
    # ["Name", "Ssn", "Title", "Salary", "year", "Address", "Gender"]
    createsalesman(SALESMANID, Name, Ssn, Title, Salary, YearOfExperience, Address, Gender)

# show if the salesman can be promoted
@salesman.route('/api/salesman/<int:SALESMANID>', methods = ['GET'])
def show_order_experience(SALESMANID):
    # TODO
    # Check if salesman exist in DB.
    exist = SalesmanExist(SALESMANID)
    if not exist:
        return abort(400, "Salesman id: {} does NOT EXIST".format(SALESMANID))
    getSalesOrder(SALESMANID)
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
