from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
crew = Blueprint('crew', __name__, template_folder='../templates')

connect = MySQL_query()

#

# Create
# Create Crew
@crew.route('/api/crew/<int:crew_id>', methods = ['POST'])
def create_crew(crew_id):
    # TODO
    # Insert swe with the the following params.
    print(request.json())
    # request.json() should have the following property.
    # ["name", "ssn", "title", "salary", "year", "address", "gender"]
    createCrew(crew_id, name, ssn, title, salary, year, address, gender)

# show if the crew can be promoted
@crew.route('/api/crew/<int:swe_id>', methods = ['GET'])
def show_project_experience(swe_id):
    # TODO
    # Check if swe exist in DB.
    
    getsweproject(swe_id)
    return

# Select certain Talents of the People
@crew.route('/api/crew/<string:talent>', methods = ['GET'])
def get_crew_talent(talent):
    #
    pass
    # TODO
    # Select from swe and Crew where Talent in the variable talent.
    # You can use some formatting like
    print("This is replaced by {}".format())
    # return the result selected


# Show the background, basic info for each person.
@crew.route('/api/crew/background', methods = ['GET'])
def get_crew_background():
    pass
    # TODO
    # Select the whole table.

# Show what they are accountable for(Manage) or assigned to do(has a manager).
@crew.route('/api/crew/<int:id>', methods = ['GET'])
def get_crew_manages(id):
    pass
    # TODO
    # Do it in 2 pass.
    # First, we look for what id is managing.
    # Second, We look for what id is assigned to do.
    # Merge those two into a list
    # Return them

# Select Crew by Dev Team
@crew.route('/api/crew/inTeam/<int:id>', methods = ['GET'])
def get_crew_manages(id):
    pass
    # TODO
    # Select the swe id having Dev Team being id.
# Read


# Update
# Update the time period for the crew in the company
@crew.route('/api/crew/time_period/<int:id>', methods = ['PUT'])
def update_crew_period(id):
    # TODO
    # In request body, there will be a field "period".
    # Update the swe/crew having id with "years_of_experience" being "period"
    pass

# Delete
@crew.route('/api/crew/<int:id>', methods = ['DELETE'])
def update_crew_period(id):
    # TODO
    # Delete the record for crew
    pass

@crew.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})


def createCrew(name, ssn, title, salary, year, address, gender):
    return True



def getsweproject(swe_id):
    return 0