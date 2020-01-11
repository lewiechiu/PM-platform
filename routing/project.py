from flask import Flask, render_template, jsonify, request, Blueprint, abort

project = Blueprint('project', __name__, template_folder='../templates')

#maimum # of projects SWE can do
MAXSWEWORKLOAD = 5

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
        projectLis = SWEProjectNum(swe)
        if len(projectLis) >= 4:
            abort(400, "Engineer ID:{} unavailable for more task".format(swe))
    
    # Insert
    # TODO
    # CONFIRMATION
    # new task? allocate resource? assign new project manager, new/old dev team? 
    InsertProject()
    # Insert such record into database.

    return jsonify({"status": 200})

@project.route('/api/project/task/<project_ID>', methods=['POST'])
def new_task(project_ID):
    # TODO
    # Query if the project_ID exists
    exist = ProjectExist(project_ID)
    # exist = True
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
    InsertTask(project_ID , State, Category , Description, Resource)
    record = request.get_json()

    return jsonify({"status": 200})

# ***** READ

@project.route('/api/project/active', defaults = {'project_id': None}, methods = ['GET'])
@project.route('/api/project/active/<project_id>', methods = ['GET'])
def get_active(project_id):
    # CONFIRMATION
    # what is project_id ==None
    # progress. i.e. Project 123: 3/5/2 (finished/in-progress/notstart) tasks
    progress = {} 
    progress = ProgressProject(project_id)
        
    if project_id == None: #what is this
        # TODO
        # Query with project ID
        # active_projects = query()
        active_projects = []
        return active_projects
    else:
        return 
        # TODO
        

@project.route('/api/project/talent/<Team>', methods = ['GET'])
def get_domain_talent(team_id):
    # TODO
    # Get the SWE ID of Team_id and Union all of the (SWE_ID, Talent) pairs.
    response = []
    response = GetTeamTalent(team_id)
    return response


@project.route('/api/project/availability/<team_id>', methods = ['GET'])
def get_team_availablitiy(team_id):
    return jsonify({"status": 200})
    # TODO
    project_lis = []
    project_lis = TeamAvailability(team_id)

    # Query for each of the SWE_ID in team "team_id", find the numbers of task each SWE_ID is accountable for.

# ***** UPDATE
@project.route('/api/project/resources/<project_id>', methods = ['PUT'])
def update_project_resource(project_id):
    # CONFIRMATION
    # input should be task not project
    if not request.json():
        return abort(400, "input not json")
    if "Resources" not in request.json():
        return abort(400, "Input field error")
    for res in request.json()["Resources"]:
        # TODO
        # CONFIRMATION: 機器的運算資源 以 # of tasks 當作單位, 因為data裡沒有表明amount
        # Nick
        ResourceExist(resource_id)
        Task_lis = []
        Task_lis = ResourceAvailability
        # IF len(Task_lis) > 10 or doesn't exist
        # return abort(400, "Can't allocate resource {} with amount {}".format(res["id"], res["amount"]))
        continue

    for res in request.json()["Resources"]:
        # TODO
        # Nick 
        AllocateNewResource(resource_id, task_id)
        continue

@project.route('/api/project/task/<task_id>', methods= ['PUT'])
def update_task_state(task_id):
    if not request.args.get('status') :
        return abort(400, "Input field error")
    
    # TODO
    Exist = TaskExist(task_id)
    if not Exist:
        return abort(400, "task id: {} does NOT EXIST".format(task_id))
    else:
        UpdateTask(task_id, status)
        return jsonify({"status": 200})

@project.route('/api/project/<int:project_id>/swe/<int:swe_id>', methods = ['PUT'])
def update_project_swe(project_id,swe_id):
    # TODO
    Exist =  ProjectExist(project_id)
    if not Exist:
        return abort(400, "project id: {} does NOT EXIST".format(project_id))

    # TODO
    Exist = SWEExist(swe_id)
    if not Exist:
        return abort(400, "SWE id: {} does NOT EXIST".format(swe_id))
    
    # TODO
    # Return True if SWE ID has capacity taking this role. count (task or project ) > 3
    projectLis = SWEProjectNum(swe_id)
    if(len(projectLis) > MAXSWEWORKLOAD):
        Exist = False
    else:
        Exist = True
    if not Exist:
        return abort(400, "SWE id: {} cannot take this project".format(swe_id))

    # TODO
    # Insert the SWE ID into the dev_team which owns PROJECT_ID
    InsertSWEintoProject(swe_id, project_id)

    return jsonify({"status": 200})
    
def SWEProjectNum(swe_id):
    # check which DevTeam the SWE is in (dev team_SWE)
    # check how many projects the dev team is working on (dev team project)
    # query # of the projects and their ID
    return []

def SWEExist(swe_id):
    return True

def InsertSWEintoProject(swe_id, project_id):
    # Insert the SWE ID into the dev_team which owns PROJECT_ID
    return True

def InsertProject():
    return True

def ProjectExist(project_id):
    return True

def InsertTask(project_ID , State, Category , Description, Resource):
    # Insert ["project ID" , "State", "Category" , "Description"] into (task)
    # Insert ["Resource"] into (task_resource)
    return True

def ProgressProject(project_id):
    # loop through all the projects (project TABLE)
    # loop through all the task that are under that project (task TABLE)
    # calculate # of tasks in each state 
    return {}

def GetTeamTalent(team_id):
    # loop through dev team (team_SWE)
    # get SWE's talent set (talent_v3)
    # union all talent sets
    return []

def TeamAvailability(team_id):
    # check how many projects the dev team is working on (dev team project)
    # query # of the projects and their ID
    return []

def ResourceExist(resource_id):
    return True

def ResourceAvailability(resource_id):
    return []


def AllocateNewResource(resource_id, task_id):
    # add new resource <-> task relationship in (task resource)
    return True

def TaskExist(task_id):
     # Check if the task of task id is present (task)
     return True

def UpdateTask(task_id, status):
    # update task's status
    return 









