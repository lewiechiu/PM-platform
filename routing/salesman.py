from flask import Flask, render_template, jsonify, request, Blueprint, abort
salesman = Blueprint('salesman', __name__, template_folder='../templates')





    # Know what each salesman is accountable for. (sales item)
    # Set KPI for each of the salesmen.
# Show the customer SalesMan are related to
# Update the time period for the salesman in the company (repeat)
# Promote a salesman to Manager or Senior salesman

# Create salesman
@salesman.route('/api/salesman/<int:salesman_id>', methods = ['POST'])
def create_salesman(salesman_id):
    # TODO
    # Insert salesman with the the following params.
    # find the max id
    # SQL : 
    cmd = "SELECT MAX(ID) FROM salesman"
    response = connect.queryALL(a)
    # SQL :
    # INSERT INTO salesman(ID,name,ssn,title, salary,age,years_of_experience,address,gender)
    # VALUES(request.json()["name"],request.json()["ssn"],request.json()["title"],request.json()["salary"],request.json()["age"],request.json()["yoe"],request.json()["address"],request.json()["gender"])
    print(request.json())
    # request.json() should have the following property.
    # ["name", "ssn", "title", "salary", "year", "address", "gender"]
    createsalesman(salesman_id, name, ssn, title, salary, year, address, gender)

# show if the salesman can be promoted
@salesman.route('/api/salesman/<int:salesman_id>', methods = ['GET'])
def show_order_experience(salesman_id):
    # TODO
    # Check if salesman exist in DB.
    exist = SalesmanExist(salesman_id)
    if not exist:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    getSalesOrder(salesman_id)
    return


# Select certain Talents of the People
@salesman.route('/api/salesman/<string:talent>', methods = ['GET'])
def select_by_talent(talent):
    #
    pass
    # TODO
    # Select from salesman and salesman where Talent in the variable talent.
    # You can use some formatting like
    getsalesmanByTalent(talent)
    # return the result selected


# Show the background, basic info for each person.
@salesman.route('/api/salesman/background', methods = ['GET'])
def get_salesman_info(salesman_id):
    pass
    # TODO
    getsalesmanInfo(salesman_id)
    # Select the whole table.
    #SQL:
    #SELECT * FROM salesman
    response = connect.queryAll('SELECT * FROM salesman')

# Update
# Update the time period for the salesman in the company
@salesman.route('/api/salesman/time_period/<int:salesman_id>', methods = ['PUT'])
def update_salesman(salesman_id):
    # TODO
    # In request body, there will be a field "period".
    # Update the salesman/salesman having id with "years_of_experience" being "period"
    exist_salesman = salesmanExist(salesman_id)
    if not exist_salesman:
        return abort(400, "salesman id: {} does NOT EXIST".format(salesman_id))
    exist_sales = SalesmanExist(salesman_id)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    if(exist_salesman):
        update_salesman(salesman_id,  target_attri, new_value, 'salesman')
    else:
        update_salesman(salesman_id,  target_attri, new_value, 'sales')
    pass

# Delete
@salesman.route('/api/salesman/<int:salesman_id>', methods = ['DELETE'])
def delete_salesman(salesman_id):
    # TODO
    exist_salesman = salesmanExist(salesman_id)
    if not exist_salesman:
        return abort(400, "salesman id: {} does NOT EXIST".format(salesman_id))
    exist_sales = SalesmanExist(salesman_id)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    # Delete the record for salesman
    if(exist_salesman):
        changesalesmanState(salesman_id, 'salesman','retired')
    else:
        changesalesmanState(salesman_id, 'sales', 'retired')
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

@salesman.route('/api/sales/')