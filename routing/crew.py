from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
from basic_function import *

crew = Blueprint('crew', __name__, template_folder='../templates')

connect = MySQL_query()


# Create Crew
@crew.route('/api/crew/<int:crew_id>', methods = ['POST'])
def create_crew(crew_id):
    # TODO
    # Insert SWE with the the following params.
    # find the max id
    # SQL : 
    cmd = "SELECT MAX(ID) FROM SWE"
    response = connect.queryALL(a)
    # SQL :
    # INSERT INTO SWE(ID,name,ssn,title, salary,age,years_of_experience,address,gender)
    # VALUES(request.json()["name"],request.json()["ssn"],request.json()["title"],request.json()["salary"],request.json()["age"],request.json()["yoe"],request.json()["address"],request.json()["gender"])
    print(request.json())
    # request.json() should have the following property.
    # ["name", "ssn", "title", "salary", "year", "address", "gender"]
    createCrew(crew_id, name, ssn, title, salary, year, address, gender)

'''
# show if the crew can be promoted
@crew.route('/api/crew/<int:swe_id>', methods = ['GET'])
def show_project_experience(swe_id):
    # TODO
    # Check if swe exist in DB.
    exist = SWEExist(swe_id)
    if not exist:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    getsweproject(swe_id)
    return 
'''
# show if the crew can be promoted
@crew.route('/api/crew/<int:salesman_id>', methods = ['GET'])
def show_order_experience(salesman_id):
    # TODO
    # Check if swe exist in DB.
    exist = SalesmanExist(salesman_id)
    if not exist:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    getSalesOrder(salesman_id)
    return

# Select certain Talents of the People
@crew.route('/api/crew/<string:talent>', methods = ['GET'])
def select_by_talent(talent):
    #
    pass
    # TODO
    # Select from swe and Crew where Talent in the variable talent.
    # You can use some formatting like
    getCrewByTalent(talent)
    # return the result selected


# Show the background, basic info for each person.
@crew.route('/api/crew/background', methods = ['GET'])
def get_crew_info(crew_id):
    pass
    # TODO
    getCrewInfo(crew_id)
    # Select the whole table.
    #SQL:
    #SELECT * FROM SWE
    response = connect.queryAll('SELECT * FROM SWE')

# Show what they are accountable for(Manage) or assigned to do(has a manager).
@crew.route('/api/crew/<int:id>', methods = ['GET'])
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
# Select Crew by Dev Team
@crew.route('/api/crew/inTeam/<int:ID>', methods = ['GET'])
def get_crew_manages(ID):
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
# Update the time period for the crew in the company
@crew.route('/api/crew/time_period/<int:crew_id>', methods = ['PUT'])
def update_crew(crew_id):
    # TODO
    # In request body, there will be a field "period".
    # Update the swe/crew having id with "years_of_experience" being "period"
    exist_swe = SWEExist(swe_id)
    if not exist_swe:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    exist_sales = SalesmanExist(salesman_id)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    if(exist_swe):
        update_crew(crew_id,  target_attri, new_value, 'swe')
    else:
        update_crew(crew_id,  target_attri, new_value, 'sales')
    pass

# Delete
@crew.route('/api/crew/<int:crew_id>', methods = ['DELETE'])
def delete_crew(crew_id):
    # TODO
    exist_swe = SWEExist(swe_id)
    if not exist_swe:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    exist_sales = SalesmanExist(salesman_id)
    if not exist_sales:
        return abort(400, "Salesman id: {} does NOT EXIST".format(salesman_id))
    # Delete the record for crew
    if(exist_swe):
        changeCrewState(crew_id, 'swe','retired')
    else:
        changeCrewState(crew_id, 'sales', 'retired')
    pass

@crew.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})


def createCrew(name, ssn, title, salary, year, address, gender):
    return True



def getsweproject(swe_id):
    return {}

def getSalesOrder(salesman_id):
    return {}

def getCrewByTalent(talent):
    # check swe and salesman table and see if they have the talent
    return {}

def getCrewInfo(crew_id):
    # return the crew info
    return {}

def getManageProject(swe_id=None):
    # if None get all the SWEs who are project managers
    # else only get the specified one
    return{}

def update_crew(crew_id,  target_attri, new_value, role)
    # if role == 'swe'
        # update swe
    # else 
        # update sales
    return TRUE

def changeCrewState(crew_id, role, state):
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

