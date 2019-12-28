from flask import Flask, render_template, jsonify, request, Blueprint, abort
crew = Blueprint('crew', __name__, template_folder='../templates')




# Create
# show if the crew can be promoted

@crew.route('/api/crew/<int:SWE_ID>', methods = ['POST'])
def create_crew(SWE_ID):
    # TODO
    # Insert SWE with the the following params.
    print(request.json())
    # request.json() should have the following property.
    # ["name", "ssn", "title", "salary", "yoe", "address", "gender"]
    
@crew.route('/api/crew/<int:SWE_ID>', methods = ['GET'])
def get_is_swe_promotable(SWE_ID):
    # TODO
    return
    
@crew.route('/api/crew/<string:talent>', methods = ['GET'])
def get_crew_talent(talent):
    pass
    # TODO

# Select certain Talents of the People
# Show the background, basic info for each person.
# Show what they are accountable for(Manage) or assigned to do(has a manager).
# Also, provide a link to the project management page.
# Select Crew by Dev Team

# Read


# Update
# Update the time period for the crew in the company
# Promote a crew to Manager or Senior SWE

# Delete



@crew.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})
