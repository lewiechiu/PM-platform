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
        projectLis = SWEProject(swe, 'in-progress')
        if len(projectLis) >= 4:
            abort(400, "Engineer ID:{} unavailable for more task".format(swe))
    
    # Insert such record into database.
    # TODO
    InsertProject(project_ID, Oder_ID, manager_id, state, swe_list)
    return jsonify({"status": 200})

@project.route('/api/project/task/<project_ID>', methods=['POST'])
def new_task(project_ID):
    # TODO
    # Query if the project_ID exists
    exist = ProjectExist(project_ID)
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
    # TBD: specify resource_amount when insert task?
    InsertTask(taskID, state, category, project_id, resource_amount)
    record = request.get_json()

    return jsonify({"status": 200})

# ***** READ

@project.route('/api/project/active', defaults = {'project_id': None}, methods = ['GET'])
@project.route('/api/project/active/<project_id>', methods = ['GET'])
def get_active(project_id):
    # TBD
    # what is the diff bw the output of None and a specified proejct_id
    if project_id == None: 
        # TODO
        active_projects = ProgressProject()
        return active_projects
    else:
        # TODO
        active_tasks = ProgressProject(project_id)
        return active_tasks
        

@project.route('/api/project/talent/<project_id>', methods = ['GET'])
def get_project_talent(project_id):
    # TODO
    response = GetProjectTalent(project_id)
    return response


@project.route('/api/project/availability/<swe_id>', methods = ['GET'])
def get_swe_availablitiy(swe_id):
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
    
def SWEProject(swe_id, state):
    # if swe_id == None -> find all swe_id
    # else only search for the specified swe_id

    # check Project_SWE table: find the same swe_id. summarize all the project_id that the swe has worked on
    # check Project table: check the project state, if the state is same as required, add to the list
    # return a list of projectIDs which are in the required state
    # return 
    return []

def SWEExist(swe_id):
    return True

def InsertSWEintoProject(swe_id, project_id):
    # Insert the SWE ID into the dev_team which owns PROJECT_ID
    return True

def InsertProject(project_ID, Oder_ID, manager_id, state, swe_list):
    # insert Project: project_ID, Oder_ID, manager_id, state
    # insert Project_SWE: project_ID, swe_list 
    return True

def ProjectExist(project_id):
    # query if the project_ID exists
    return True

def InsertTask(taskID, state, category, project_id, resource_amount):
    # Insert ["project ID" , "State", "Category" , "Description"] into (task)
    # Insert ["resource_amount"] into (task_resource)
    return True

def ProgressProject(project_id=None):
    # if project_id==None
    # query all the in-progress proejcts' ID and return a list
    # else if project_id is specified 
    # query all the in-progress task' ID and return a list
    return {}

def GetProjectTalent(project_id):
    # query project_SWE table for the swe id
    # query talent with the swe id
    # return a dictionary
    # {
    #   {
    #     "name" : "name of the swe",
    #     "Job title" : "title",
    #     "Talent" : ["Talent1" ,"Talent 2", "Talent 3"]
    #   },...
    # }
    return {}

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









