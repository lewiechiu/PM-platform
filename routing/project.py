from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
import json
project = Blueprint('project', __name__, template_folder='../templates')
connect = MySQL_query()
#maimum # of projects SWE can do
MAXSWEWORKLOAD = 5

# ************* Project API ************* 
# ***** Create

@project.route('/api/project/new_projects', methods = ['POST'])
def new_project_api():
    # Field checking
    fields = ["SWE ID", "Manager ID","Project ID","Order ID","State"]
    for i in request.get_json():
        if i in fields:
            fields.remove(i)
    if len(fields) != 0:
        abort(400, "missing input field")
    print(request.get_json())

    # Check if the SWEs are available
    # Iterate throught the SWEs and query their availability.
    for swe in request.get_json()['SWE ID']:
        # Some query and checking
        # TODO
        projectLisDict = SWEProject(' in-progress',swe)
        if projectLisDict[0]["Available capacity"] <= 0:
            abort(400, "Engineer ID:{} unavailable for more task".format(swe))
    
    project_ID = request.get_json()['Project ID']
    Order_ID = request.get_json()['Order ID']
    manager_id = request.get_json()['Manager ID']
    state = request.get_json()['State']
    swe_list = request.get_json()['SWE ID']
    # Insert such record into database.
    # TODO
    InsertProject(project_ID, Order_ID, manager_id, state, swe_list)
    return jsonify({"status": 200})

@project.route('/api/project/task/<project_ID>', methods=['POST'])
def new_task(project_ID):
    # TODO
    # Query if the project_ID exists
    exist = ProjectExist(project_ID)
    if not exist:
        return abort(400, "project ID not exist")

    fields = ["project ID", "Resources" , "State", "Category" ,"Resource Amount"]
    for i in request.get_json():
        if i not in fields:
            return abort(400, "Input field error")
    
    if len(fields) != len(request.get_json()):
        return abort(400, "Input field error")

    cmd = "SELECT MAX(TASKID) FROM Task"
    response = connect.queryALL(cmd)
    response = clean_tuple(response,0)
    taskID = response[0] + 1
    state = request.get_json()["State"]
    category = request.get_json()["Category"]
    project_id = request.get_json()["project ID"]
    resource_amount = request.get_json()["Resource Amount"]
    resource_ID = request.get_json()["Resources"]
    # TODO
    # Insert the record into database.
    # TBD: specify resource_amount when insert task?
    InsertTask(taskID, state, category, project_id, resource_amount,resource_ID)
    record = request.get_json()

    return jsonify({"status": 200})

# ***** READ

@project.route('/api/project/active', defaults = {'project_id': None}, methods = ['GET'])
@project.route('/api/project/active/<project_id>', methods = ['GET'])
def get_active(project_id):
    # TBDe
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
    #return jsonify({"status": 200})
    # TODO
    project_lis = []
    project_lis_dict = SWEProject(' in-progress',swe_id)
    return_json = json.dumps(project_lis_dict[0])
    return return_json


# ***** UPDATE
@project.route('/api/project/resources/<task_id>', methods = ['PUT'])
def update_task_resource(task_id, resource_id, resource_amount):
    if not request.json():
        return abort(400, "input not json")
    if "Resources" not in request.json():
        return abort(400, "Input field error")
    #TBD
    #why is here a for loop?
    for res in request.json()["Resources"]:
        # TODO
        #check if the resource exists
        exist = ResourceExist(resource_id)
        if not exist:
            return abort(400, "resource id: {} does NOT EXIST".format(resource_id))
        enough = AllocateNewResource(resource_id, resource_amount)
        if( not enough):
            return abort(400, "resource id: {} does have ENOUGH resource".format(resource_id))

@project.route('/api/project/task/<task_id>', methods= ['PUT'])
def update_task_state(task_id):
    if not request.args.get('status') :
        return abort(400, "Input field error")
    
    # TODO
    Exist = TaskExist(task_id)
    if not Exist:
        return abort(400, "task id: {} does NOT EXIST".format(task_id))
    else:
        UpdateTask(task_id, state)
        return jsonify({"status": 200})

@project.route('/api/project/<int:project_id>/swe/<int:swe_id>', methods = ['PUT'])
def update_project_swe(project_id, swe_id):
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
    projectLisDict = SWEProject(' in-progress',swe_id)
    if projectLisDict[0]["Available capacity"] <= 0:
        Exist = False
    else:
        Exist = True
    if not Exist:
        return abort(400, "SWE id: {} cannot take this project".format(swe_id))

    # TODO
    InsertSWEintoProject(swe_id, project_id)

    return jsonify({"status": 200})
    
def SWEProject(state, swe_id=None):
    # if swe_id == None -> find all swe_id
    # else only search for the specified swe_id
    # check Project_SWE table: find the same swe_id. summarize all the project_id that the swe has worked on
    # check Project table: check the project state, if the state is same as required, add to the list
    # return a list of projectIDs which are in the required state
    # return 
    # 安安GO~     change to: return a list of dictionary
    if swe_id == None:
        #SQL:
        return_list_of_dict = []
        dict_that_go_into_list = {}
        cmd = "SELECT SWEID,Name FROM SWE"
        response = connect.queryALL(cmd)
        SWE_ID = clean_tuple(reponse,0)
        SWE_Name = clean_tuple(response,1)
        for i in range(len(SWE_ID)):
            dict_that_go_into_list["SWE_id"] = SWE_ID[i]
            dict_that_go_into_list["Name"] = SWE_Name[i]
            cmd2 = "SELECT COUNT(P_ID) FROM Project P,Project_SWE WHERE P_ID = P.project_ID and  SWE_ID = "
            cmd2 = cmd2 + str(SWE_ID[i]) +" and P.state = '" + state + "'"
            response2 = connect.queryALL(cmd2)
            response2 = clean_tuple(response2,0)
            dict_that_go_into_list["Available capacity"] = 5-response2
            return_list_of_dict.append(dict_that_go_into_list)
    else:
        #SQL:
        return_list_of_dict = []
        dict_that_go_into_list = {}
        cmd = "SELECT ID,Name FROM SWE WHERE ID = "
        cmd = cmd + str(swe_id)
        response = connect.queryALL(cmd)
        SWE_ID = clean_tuple(reponse,0)
        SWE_Name = clean_tuple(response,1)
        dict_that_go_into_list["SWE_id"] = SWE_ID[0]
        dict_that_go_into_list["Name"] = SWE_Name[0]
        cmd2 = "SELECT COUNT(P_ID) FROM Project P,Project_SWE WHERE P_ID = P.project_ID and  SWE_ID = "
        cmd2 = cmd2 + str(SWE_ID[0])+" and P.state = '" + state + "'"
        response2 = connect.queryALL(cmd2)
        response2 = clean_tuple(response2,0)
        dict_that_go_into_list["Available capacity"] = 5-response2
        return_list_of_dict.append(dict_that_go_into_list)

    return return_list_of_dict
#    return []

def SWEExist(swe_id):
    #SQL:
    #SELECT ID FROM SWE WHEWE ID=swe_id
    cmd = "SELECT ID FROM SWE WHEWE ID=" + str(swe_id)
    response = connect.queryALL(cmd)
    response = clean_tuple(response,0)
    if len(response) > 0:
        return True
    else:
        return False

    

def InsertSWEintoProject(swe_id, project_id):
    # Insert the SWE ID into project_SWE table
    # SQL:
    # INSERT INTO Project_SWE(P_ID,SWE_ID) VALUES(project_id,swe_id) 
    cmd = "INSERT INTO Project_SWE(P_ID,SWE_ID) VALUES("
    cmd = cmd + str(project_id) + "," + str(swe_id) +")"
    connect.query_insertORdelete(cmd)
    return True

def InsertProject(project_ID, Oder_ID, manager_id, state, swe_list):
    # insert Project: project_ID, Oder_ID, manager_id, state
    # insert Project_SWE: project_ID, swe_list
    # SQL:
    # INSERT INTO Project(project_ID, Oder_ID, manager_id, state) VALUES(
    cmd = "INSERT INTO Project(project_ID, Oder_ID, manager_id, state) VALUES("
    cmd = cmd + str(project_ID) + "," + str(Oder_ID) + "," + str(manager_id) + "," + "'" + str(state) + "')"
    connect.query_insertORdelete(cmd)
    for i in swe_list:
        InsertSWEintoProject(i, project_ID)
    return True

def ProjectExist(project_id):
    # query if the project_ID exists
    # SQL:
    #SELECT project_ID FROM Project WHERE project_ID = 
    cmd = "SELECT project_ID FROM Project WHERE project_ID = "
    cmd = cmd + str(project_id)
    response = connect.queryALL(cmd)
    response = clean_tuple(response,0)
    if len(response) > 0:
        return True
    else:
        return False
#    return True

def InsertTask(taskID, state, category, project_id, resource_amount,resource_ID):
    # Insert ["project ID" , "State", "Category"] into (task)
    # Insert ["resource_amount"] into (task_resource)
    # SQL1:
    # INSERT INTO Task(taskID, state, category) VALUES(
    cmd = "INSERT INTO Task(taskID, state, category, P_ID) VALUES("
    cmd = cmd + str(taskID) + "," + "'" + str(state) + "'" +"," + "'" + str(category) + "'" +","+str(project_id)+")"
    connect.query_insertORdelete(cmd)
    # SQL2:
    # INSERT INTO Task_Resource(R_ID,T_ID,resource_amount) VALUES(
    cmd = "INSERT INTO Task_Resource(R_ID,T_ID,resource_amount) VALUES("
    cmd = cmd + str(resource_ID) +","+str(taskID)+","+str(resource_amount)+ ")"
    connect.query_insertORdelete(cmd)
    return True

def ProgressProject(project_id=None):
    # if project_id==None
    # query all the in-progress proejcts' ID and return a list
    # else if project_id is specified 
    # query all the in-progress task' ID and return a list
    dict_to_become_jason = {}
    in_progress = "'" + " in-progress" + "'"
    if project_id == None:
    # SQL:
    # SELECT COUNT(P_ID) FROM Task WHERE state = 'in-progess'
        cmd = "SELECT COUNT(P_ID) FROM Task WHERE state = "
        cmd =cmd + in_progress
        response = connect.queryALL(cmd)
        response = clean_tuple(response,0)
        dict_to_become_jason['No_id'] = int(response[0])
        cmd = "SELECT P_ID FROM Task WHERE state = "
        cmd =cmd + in_progress
        response = connect.queryALL(cmd)
        response = clean_tuple(response,0)
        dict_to_become_jason['Projects'] = response
    else:
        cmd = "SELECT taskID FROM Task WHERE state="
        cmd = cmd + in_progress + " and P_ID =" + str(project_id)
        response = connect.queryALL(cmd)
        response = clean_tuple(response,0)
        dict_to_become_jason['project_id'] = project_id
        dict_to_become_jason['task'] = response
    jason_form = json.dumps(dict_to_become_jason)
#    return {}
    return jason_form

def GetProjectTalent(project_id):
    # query project_SWE table for the swe id
    # query talent with the swe id
    # return a dictionary
    # {
    #   {
    #     "Name" : "Name of the swe",
    #     "Job title" : "title",
    #     "Talent" : ["Talent1" ,"Talent 2", "Talent 3"]
    #   },...
    # }
    # SQL:
    # SELECT SWE_ID FROM Project_SWE WHERE P_ID =
    list_to_be_json = []
    cmd = "SELECT SWE_ID FROM Project_SWE WHERE P_ID =" + str(project_id)
    reponse = connect.queryALL(cmd)
    list_of_swe_id = clean_tuple(response,0)
    for i in list_of_swe_id:
        dict_itr = {}
        cmd2 = "SELECT Name,title FROM SWE WHERE ID=" + str(i)
        reponse2 = connect.queryALL(cmd2)
        swe_Name = clean_tuple(reponse2,0)
        swe_title = clean_tuple(reponse2,1)
        cmd3 = "SELECT talent FROM Talent WHERE ID = " + str(i)
        reponse3 = connect.queryALL(cmd3)
        swe_talents = clean_tuple(reponse3,0)
        dict_itr['Name'] = swe_Name[0]
        dict_itr['Job title'] = swe_title[0]
        dict_itr['Talent'] = swe_talents
        list_to_be_json.append(dict_itr)
    return_json = json.dumps(list_to_be_json)
    return return_json

def ResourceExist(resource_id):
    # SQL:
    # SELECT resourceID FROM resource WHERE resourceID = 
    cmd = "SELECT resourceID FROM resource WHERE resourceID = "
    cmd = cmd + str(resource_id)
    response = connect.queryALL(cmd)
    response = clean_tuple(response,0)
    if len(response) > 0:
        return True
    else:
        return False


def AllocateNewResource(resource_id, task_id):
    # query the capacity from resource table
    # summarize resource comsumption from task resource table
    # if (total comsumption < capacity)
        # add new resource <-> task relationship in (task resource)
    # else 
    # return False
    # SQL:
    # SELECT capacity FROM resource WHERE resourceID = 
    cmd = "SELECT capacity FROM resource WHERE resourceID = "
    cmd = cmd + str(resource_id)
    response = connect.queryALL(cmd)
    response = clean_tuple(response,0)
    max_amount = int(response[0])
    cmd2 = "SELECT SUM(amount) FROM Task_Resource WHERE R_ID = "
    cmd2 = cmd2 + str(resource_id)
    response2 = connect.queryALL(cmd2)
    response2 = clean_tuple(response2,0)
    current_amount = int(response2[0])
    if current_amount + resource_amount <= max_amount:
        cmd3 = "INSERT INTO Task_Resource(R_ID,T_ID,resource_amount) VALUES("
        cmd3 = cmd + str(resource_id) +","+str(task_id)+","+str(resource_amount)+")"
        connect.query_insertORdelete(cmd3)
        return True
    else:
        return False

def TaskExist(task_id):
     # Check if the task of task id is present (task)
     # SQL:
     # SELECT taskID FROM Task WHERE taskID =
     cmd = "SELECT taskID FROM Task WHERE taskID = " + str(task_id)
     response = connect.queryALL(cmd)
     response = clean_tuple(response,0)
     if len(response) > 0:
         return True
     else:
         return False

def UpdateTask(task_id, state):
    # update task's state
    # SQL:
    # UPDATE Task SET state = 
    state_string = "'" + state + "'"
    cmd = "UPDATE Task SET state = " + state_string +" WHERE taskID = " + str(task_id)
    connect.query_insertORdelete(cmd)
    return True









