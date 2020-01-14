from mysql_conf import *
import json
connect = MySQL_query()

# state = " notstart"
# state_string = "'" + state + "'"
# task_id = "2"
# cmd = "UPDATE Task SET state = " + state_string +" WHERE taskID = " + task_id
# connect.query_insertORdelete(cmd)

# cmd = "SELECT * FROM Task WHERE taskID = 2"
# reponse = connect.queryALL(cmd)
# print(reponse)
# cmd = "SELECT COUNT(ID) FROM SWE WHERE age = 36"
# response = connect.queryALL(cmd)
# response = clean_tuple(response,0)
# print(response[0])
# '''
# cmd = "SELECT * FROM Task"
# response = connect.queryALL(cmd)
# print(response)
# '''
# cmd2 = "SELECT name,title FROM SWE WHERE ID=10" 
# reponse2 = connect.queryALL(cmd2)
# swe_name = clean_tuple(reponse2,0)
# swe_title = clean_tuple(reponse2,1)
# print(swe_name[0])
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
        cmd = "SELECT ID,name FROM SWE"
        response = connect.queryALL(cmd)
        SWE_ID = clean_tuple(reponse,0)
        SWE_NAME = clean_tuple(response,1)
        for i in range(len(SWE_ID)):
            dict_that_go_into_list["SWE_id"] = SWE_ID[i]
            dict_that_go_into_list["name"] = SWE_NAME[i]
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
        cmd = "SELECT ID,name FROM SWE WHERE ID = "
        cmd = cmd + str(swe_id)
        response = connect.queryALL(cmd)
        SWE_ID = clean_tuple(response,0)
        SWE_NAME = clean_tuple(response,1)
        dict_that_go_into_list["SWE_id"] = SWE_ID[0]
        dict_that_go_into_list["name"] = SWE_NAME[0]
        cmd2 = "SELECT COUNT(P_ID) FROM Project P,Project_SWE WHERE P_ID = P.project_ID and  SWE_ID = "
        cmd2 = cmd2 + str(SWE_ID[0])+" and P.state = '" + state + "'"
        response2 = connect.queryALL(cmd2)
        response2 = clean_tuple(response2,0)
        dict_that_go_into_list["Available capacity"] = 5-response2
        return_list_of_dict.append(dict_that_go_into_list)

    return return_list_of_dict

projectLisDict = SWEProject(' in-progress',9)
print(projectLisDict[0]["Available capacity"])




