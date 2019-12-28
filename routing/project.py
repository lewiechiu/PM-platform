from flask import Flask, render_template, jsonify, request, Blueprint, abort

project = Blueprint('project', __name__, template_folder='../templates')



# ************* Project API ************* 
# ***** Create

@project.route('/api/project/new_projects', methods = ['POST'])
def new_project_api():
    # Field checking
    fields = ["SWE ID", "Dev Team ID", "Manager ID"]
    for i in request.json():
        if i in fields:
            fields.remove(i)
    if len(fields) != 0:
        abort(400, "missing input field")
    print(request.get_json())

    # Check if the SWEs are available
    # Iterate throught the SWEs and query their availability.
    for swe in request.json()['SWE ID']:
        # Some query and checking
        # TODO
        # Query the projects swe ID is working on.
        "SELECT * FROM .... where"
        projects = []
        if len(projects) >= 4:
            abort(400, "Engineer ID:{} unavailable for more task".format(swe))
    
    # Insert
    # TODO
    # Insert such record into database.

    return jsonify({"status": 200})

@project.route('/api/project/task/<project_ID>', methods=['POST'])
def new_task(project_ID):
    # TODO
    # Query if the project_ID exists
    # exist = some_query()
    exist = True
    if not exist:
        return abort(400, "project ID not exist")

    fields = ["project ID", "Resources" , "State", "Category" , "Description"]
    for i in request.get_json():
        if i not in fields:
            return abort(400, "Input field error")
    
    if len(fields.keys()) != len(fields):
        return abort(400, "Input field error")

    
    # TODO
    # Insert the record into database.
    record = request.get_json()

    return jsonify({"status": 200})

# ***** READ

@project.route('/api/project/active', defaults = {'project_id': None}, methods = ['GET'])
@project.route('/api/project/active/<project_id>', methods = ['GET'])
def get_active(project_id):
    

    if project_id == None:
        # TODO
        # Query with project ID
        # active_projects = query()
        active_projects = []
        return active_projects
    else:
        return 
        # TODO
        # Query the number of tasks under

@project.route('/api/project/talent/<Team>', methods = ['GET'])
def get_domain_talen(Team):
    # TODO
    # Get the SWE ID of Team_id and Union all of the (SWE_ID, Talent) pairs.
    response = []
    SWE_talent = {}

    return response


@project.route('/api/project/availability/<team_id>', methods = ['GET'])
def get_team_availablitiy(team_id):
    return jsonify({"status": 200})
    # TODO
    # Query for each of the SWE_ID in team "team_id", find the numbers of task each SWE_ID is accountable for.

# ***** UPDATE
@project.route('/api/project/resources/<project_id>', methods = ['PUT'])
def update_project_resource(project_id):
    if not request.json():
        return abort(400, "input not json")
    if "Resources" not in request.json():
        return abort(400, "Input field error")
    for res in request.json()["Resources"]:
        # TODO
        # Check if res["id"] exists, and has store greater than res["amount"]
        # IF it does not
        # return abort(400, "Can't allocate resource {} with amount {}".format(res["id"], res["amount"]))
        continue

    for res in request.json()["Resources"]:
        # TODO
        # Modify resources and deduct the stored amount by res["amount"]
        continue

@project.route('/api/project/task/<task_id>', methods= ['PUT'])
def update_task_state(task_id):
    if not request.args.get('status') :
        return abort(400, "Input field error")
    
    # TODO
    # Check if the task of task id is present
    # If not, then abort and return 400

    # If it exists, update and return status 200

@project.route('/api/project/<int:project_id>/swe/<int:swe_id>', methods = ['PUT'])
def update_project_swe(project_id,swe_id):
    # TODO
    # Return True if projectID exists,
    # Otherwise, False.
    Exist = True # Replace this with the SQL Query

    if not Exist:
        return abort(400, "project id: {} does NOT EXIST".format(project_id))

    # TODO
    # Return True if SWE ID exists,
    # Otherwise, False.
    Exist = True # Replace this with the SQL Query

    if not Exist:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))

    # TODO
    # Return True if SWE ID has capacity taking this role. count (task or project ) > 3
    # Otherwise, False.
    Exist = True # Replace this with the SQL Query

    if not Exist:
        return abort(400, "SWE id: {} cannot take this project".format(swe_id))

    # TODO
    # Insert the SWE ID into PROJECT_ID

    return jsonify({"status": 200})
    

  