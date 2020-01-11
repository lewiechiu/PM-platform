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
    print(request.json())
    # request.json() should have the following property.
    # ["name", "ssn", "title", "salary", "year", "address", "gender"]
    createCrew(name, ssn, title, salary, year, address, gender)

# show if the crew can be promoted
@crew.route('/api/crew/<int:SWE_ID>', methods = ['GET'])
def get_is_swe_promotable(SWE_ID):
    # TODO
    # Check if SWE exist in DB.
    # TO DISCUSS
    # There should be some rank ordering.
    # Also, We should modify the title, salary, ...etc. once being promoted.
    
    return

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

# Show what they are accountable for(Manage) or assigned to do(has a manager).
@crew.route('/api/crew/<int:ID>', methods = ['GET'])
def get_crew_manages(ID):
    pass
    # TODO
    # Do it in 2 pass.
    # First, we look for what ID is managing.
    # Second, We look for what ID is assigned to do.
    # Merge those two into a list
    # Return them

# Select Crew by Dev Team
@crew.route('/api/crew/inTeam/<int:ID>', methods = ['GET'])
def get_crew_manages(ID):
    pass
    # TODO
    # Select the SWE ID having Dev Team being ID.
# Read


# Update
# Update the time period for the crew in the company
@crew.route('/api/crew/time_period/<int:ID>', methods = ['PUT'])
def update_crew_period(ID):
    # TODO
    # In request body, there will be a field "period".
    # Update the SWE/crew having ID with "years_of_experience" being "period"
    pass

# Delete
@crew.route('/api/crew/<int:ID>', methods = ['DELETE'])
def update_crew_period(ID):
    # TODO
    # Delete the record for crew
    pass

@crew.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})


def createCrew(name, ssn, title, salary, year, address, gender):
    return True