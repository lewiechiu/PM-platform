from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
crew = Blueprint('crew', __name__, template_folder='../templates')

connect = MySQL_query()



# Create
# Create Crew
@crew.route('/api/crew/<int:SWE_ID>', methods = ['POST'])
def create_crew(SWE_ID):
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
    # ["name", "ssn", "title", "salary", "yoe", "address", "gender"]
    # TONOTICE :
    # not sure if "age" is in request.json()
    # ["name", "ssn", "title", "salary", "age", "yoe", "address", "gender"]

'''
# show if the crew can be promoted
@crew.route('/api/crew/<int:SWE_ID>', methods = ['GET'])
def get_is_swe_promotable(SWE_ID):
    # TODO
    # Check if SWE exist in DB.
    # TO DISCUSS
    # There should be some rank ordering.
    # Also, We should modify the title, salary, ...etc. once being promoted.
    
    return
'''
# Select certain Talents of the People
@crew.route('/api/crew/<string:talent>', methods = ['GET'])
def get_crew_talent(talent):
    #
    pass
    # TODO
    # Select from SWE and Crew where Talent in the variable talent.
    # You can use some formatting like
    print("This is replaced by {}".format())
    # return the result selected


# Show the background, basic info for each person.
@crew.route('/api/crew/background', methods = ['GET'])
def get_crew_background():
    pass
    # TODO
    # Select the whole table.
    #SQL:
    #SELECT * FROM SWE
    response = connect.queryAll('SELECT * FROM SWE')

# Show what they are accountable for(Manage) or assigned to do(has a manager).
@crew.route('/api/crew/<int:ID>', methods = ['GET'])
def get_crew_manages(ID):
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

# Update
# Update the time period for the crew in the company
@crew.route('/api/crew/time_period/<int:ID>', methods = ['PUT'])
def update_crew_period(ID):
    # TODO
    # In request body, there will be a field "period".
    # Update the SWE/crew having ID with "years_of_experience" being "period"
    # SQL:
    # UPDATE SWE SET SWE.years_of_experience = request.json()["period"] WHERE SWE.ID = ID

    pass

# Delete
@crew.route('/api/crew/<int:ID>', methods = ['DELETE'])
def update_crew_period(ID):
    # TODO
    # Delete the record for crew
    # SQL:
    # DELETE FROM Project_SWE WHERE SWE_ID = ID 

    pass

@crew.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})
