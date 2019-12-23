from flask import Flask, render_template, jsonify, request, make_response, abort
import routing
app = Flask(__name__)

@app.errorhandler(404)
def NOT_FOUND():
    return make_response(jsonify({"status": 404}))

@app.route('/', methods=['GET', 'POST'])
def starting():
    return render_template('main.html')

@app.route('/<pageName>', methods=['GET'])
def page(pageName):
    return render_template(pageName)

@app.route('/api/', methods=['POST'])
def receive():
    content = request.get_json()
    print(content)
    return jsonify({"type": "good"})

@app.route('/api/sale/', methods = ['POST'])
def sale_api():
    return jsonify({"status": 200})

@app.route('/api/swe/', methods = ['POST'])
def swe_api():
    return jsonify({"status": 200})


@app.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})

# ************* Project API ************* 
# ***** Create


@app.route('/api/project/new_projects', methods = ['POST'])
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
        projects = []
        if len(projects) >= 4:
            abort(400, "Engineer ID:{} unavailable for more task".format(swe))
    
    # Insert
    # TODO
    # Insert such record into database.

    return jsonify({"status": 200})

@app.route('/api/project/task/<int:project_ID>', methods=['POST'])
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

@app.route('api/project/active', defaults = {'project_id': None}, methods = ['GET'])
@app.route('api/project/active/<int:project_id>', methods = ['GET'])
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

@app.route('api/project/talent/<int:Team>', methods = ['GET'])
def get_domain_talen(Team):
    # TODO
    # Get the SWE ID of Team_id and Union all of the (SWE_ID, Talent) pairs.
    response = []
    SWE_talent = {}

    return response


@app.route('api/project/availability/<int:team_id>', methods = ['GET'])
def get_team_availablitiy(team_id):
    # TODO
    # Query for each of the SWE_ID in team "team_id", find the numbers of task each SWE_ID is accountable for.

# ***** UPDATE

@app.route('api/project/resources/<int:project_id>', methods = ['PUT'])
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

    


    

if __name__ == '__main__':
    app.run(debug=True)
