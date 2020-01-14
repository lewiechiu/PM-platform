from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
from basic_function import *

swe = Blueprint('swe', __name__, template_folder='../templates')

connect = MySQL_query()
resp = connect.queryALL("SELECT ....")
resp = [(), (), ...]
[()]

# Create swe
@swe.route('/api/swe/<int:swe_id>', methods = ['POST'])
def create_swe(swe_id):
    # TODO
    # Insert SWE with the the following params.
    # find the max id
    # SQL : 
    cmd = "SELECT MAX(ID) FROM SWE"
    response = connect.queryALL(cmd)
    response = clean_tuple(response,0)
    jname = str(request.json()["name"])
    jssn = str(request.json()["ssn"])
    jtitle = str(request.json()["title"])
    jsalary = str(request.json()["salary"])
    jage = str(request.json()["age"])
    jyoe = str(request.json()["yoe"])
    jaddress = str(request.json()["address"])
    jgender = str(request.json()["gender"])
    # SQL :
    # INSERT INTO SWE(ID,name,ssn,title, salary,age,years_of_experience,address,gender)
    # VALUES(request.json()["name"],request.json()["ssn"],request.json()["title"],request.json()["salary"],request.json()["age"],request.json()["yoe"],request.json()["address"],request.json()["gender"])
    
    cmd2 = "INSERT INTO SWE(ID,name,ssn,title, salary,age,years_of_experience,address,gender)"
    print(request.json())
    # request.json() should have the following property.
    # ["name", "ssn", "title", "salary", "year", "address", "gender"]
    createswe(swe_id, name, ssn, title, salary, year, address, gender)

'''
# show if the swe can be promoted
@swe.route('/api/swe/<int:swe_id>', methods = ['GET'])
def show_project_experience(swe_id):
    # TODO
    # Check if swe exist in DB.
    exist = SWEExist(swe_id)
    if not exist:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    getsweproject(swe_id)
    return 
'''
# show if the swe can be promoted
@swe.route('/api/swe/<int:salesman_id>', methods = ['GET'])
def show_order_experience(salesman_id):
    # TODO
    # Check if swe exist in DB.
    exist = SalesmanExist(salesman_id)
    if not exist:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    getSalesOrder(salesman_id)
    return

# Select certain Talents of the People
@swe.route('/api/swe/<string:talent>', methods = ['GET'])
def select_by_talent(talent):
    #
    pass
    # TODO
    # Select from swe and swe where Talent in the variable talent.
    # You can use some formatting like
    getsweByTalent(talent)
    # return the result selected


# Show the background, basic info for each person.
@swe.route('/api/swe/background', methods = ['GET'])
def get_swe_info(swe_id):
    pass
    # TODO
    getsweInfo(swe_id)
    # Select the whole table.
    #SQL:
    #SELECT * FROM SWE
    response = connect.queryAll('SELECT * FROM SWE')

# Show what they are accountable for(Manage) or assigned to do(has a manager).
@swe.route('/api/swe/<int:id>', methods = ['GET'])
def get_swe_manager(swe_id):
    pass
    # TODO
    # Do it in 2 pass.
    # First, we look for what ID is managing.
    # SQL:
    # SELECT project_ID FROM Project WhERE manager_id = ID
    cmd = "SELECT project_ID FROM Project WhERE manager_id = " + str(ID)
    he_manages = connect.queryAll(cmd)
    # Second, We look for what ID is assigned to do.
    # SQL:
    # SELECT P_ID FROM Project_SWE WHERE SWE_ID = ID
    cmd = "SELECT P_ID FROM Project_SWE WHERE SWE_ID = " + str(ID)
    he_involved_in = connect.queryAll(cmd)
    # TOFIX:
    # There is a problem that some swe has "many many" project while some are salary thrief!!
    # Merge those two into a list

    # Return them
'''
# Select swe by Dev Team
@swe.route('/api/swe/inTeam/<int:ID>', methods = ['GET'])
def get_swe_manages(ID):
    pass
    # TODO
    # Select the SWE ID having Dev Team being ID.
# Read
'''

    # First, we look for what id is managing.
    # Second, We look for what id is assigned to do.
    # Merge those two into a list
    if(swe_id != None):
        exist = SWEExist(swe_id)
        if not exist:
            return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    
    getManageProject(swe_id)
    # Return them

# Update
# Update the time period for the swe in the company
@swe.route('/api/swe/time_period/<int:swe_id>', methods = ['PUT'])
def update_swe(swe_id):
    # TODO
    # In request body, there will be a field "period".
    # Update the swe/swe having id with "years_of_experience" being "period"
    exist_swe = SWEExist(swe_id)
    if not exist_swe:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    exist_sales = SalesmanExist(salesman_id)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    if(exist_swe):
        update_swe(swe_id,  target_attri, new_value, 'swe')
    else:
        update_swe(swe_id,  target_attri, new_value, 'sales')
    pass

# Delete
@swe.route('/api/swe/<int:swe_id>', methods = ['DELETE'])
def delete_swe(swe_id):
    # TODO
    exist_swe = SWEExist(swe_id)
    if not exist_swe:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    exist_sales = SalesmanExist(salesman_id)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    # Delete the record for swe
    if(exist_swe):
        changesweState(swe_id, 'swe','retired')
    else:
        changesweState(swe_id, 'sales', 'retired')
    pass

@swe.route('/api/swe/', methods = ['POST'])
def swe_api():
    return jsonify({"status": 200})


def createswe(name, ssn, title, salary, year, address, gender):
    return True



def getsweproject(swe_id):
    return {}

def getSalesOrder(salesman_id):
    return {}

def getsweByTalent(talent):
    # check swe and salesman table and see if they have the talent
    return {}

def getsweInfo(swe_id):
    # return the swe info
    return {}

def getManageProject(swe_id=None):
    # if None get all the SWEs who are project managers
    # else only get the specified one
    return{}

def update_swe(swe_id,  target_attri, new_value, role)
    # if role == 'swe'
        # update swe
    # else 
        # update sales
    return TRUE

def changesweState(swe_id, role, state):
    # if role == 'swe'
        # if he doesn't manage active project
            # update the swe state to 'retire'
        # else
            # return false
    # else 
        # if he doesn't have active order
            # update the salesman state to 'retire'
        # else
            # return false
    return TRUE

