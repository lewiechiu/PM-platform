from mysql_conf import *
import json
import requests
from tabulate import tabulate
connect = MySQL_query()

# # state = " notstart"
# # state_string = "'" + state + "'"
# # task_id = "2"
# # cmd = "UPDATE Task SET state = " + state_string +" WHERE taskID = " + task_id
# # connect.query_insertORdelete(cmd)

# # cmd = "SELECT * FROM Task WHERE taskID = 2"
# # reponse = connect.queryALL(cmd)
# # print(reponse)
# # cmd = "SELECT COUNT(ID) FROM SWE WHERE age = 36"
# # response = connect.queryALL(cmd)
# # response = clean_tuple(response,0)
# # print(response[0])
# # '''
# # cmd = "SELECT * FROM Task"
# # response = connect.queryALL(cmd)
# # print(response)
# # '''
# # cmd2 = "SELECT name,title FROM SWE WHERE ID=10" 
# # reponse2 = connect.queryALL(cmd2)
# # swe_name = clean_tuple(reponse2,0)
# # swe_title = clean_tuple(reponse2,1)
# # print(swe_name[0])
# # def SWEProject(state, swe_id=None):
# #     # if swe_id == None -> find all swe_id
# #     # else only search for the specified swe_id
# #     # check Project_SWE table: find the same swe_id. summarize all the project_id that the swe has worked on
# #     # check Project table: check the project state, if the state is same as required, add to the list
# #     # return a list of projectIDs which are in the required state
# #     # return 
# #     # 安安GO~     change to: return a list of dictionary
# #     if swe_id == None:
# #         #SQL:
# #         return_list_of_dict = []
# #         dict_that_go_into_list = {}
# #         cmd = "SELECT SWEID,Name FROM SWE"
# #         response = connect.queryALL(cmd)
# #         SWE_ID = clean_tuple(reponse,0)
# #         SWE_NAME = clean_tuple(response,1)
# #         for i in range(len(SWE_ID)):
# #             dict_that_go_into_list["SWE_id"] = SWE_ID[i]
# #             dict_that_go_into_list["name"] = SWE_NAME[i]
# #             cmd2 = "SELECT COUNT(PS.PROJECTID) FROM Project P,Project_SWE PS WHERE PS.PROJECTID = P.PROJECTID and  PS.SWEID = "
# #             cmd2 = cmd2 + str(SWE_ID[i]) +" and P.State = '" + state + "'"
# #             response2 = connect.queryALL(cmd2)
# #             response2 = clean_tuple(response2,0)
# #             dict_that_go_into_list["Available capacity"] = 5-response2[0]
# #             return_list_of_dict.append(dict_that_go_into_list)
# #     else:
# #         #SQL:
# #         return_list_of_dict = []
# #         dict_that_go_into_list = {}
# #         cmd = "SELECT SWEID,Name FROM SWE WHERE SWEID = "
# #         cmd = cmd + str(swe_id)
# #         response = connect.queryALL(cmd)
# #         SWE_ID = clean_tuple(response,0)
# #         SWE_NAME = clean_tuple(response,1)
# #         dict_that_go_into_list["SWE_id"] = SWE_ID[0]
# #         dict_that_go_into_list["name"] = SWE_NAME[0]
# #         cmd2 = "SELECT COUNT(PS.PROJECTID) FROM Project P,Project_SWE PS WHERE PS.PROJECTID = P.PROJECTID and  PS.SWEID = "
# #         cmd2 = cmd2 + str(SWE_ID[0])+" and P.State = '" + state + "'"
# #         response2 = connect.queryALL(cmd2)
# #         response2 = clean_tuple(response2,0)
# #         dict_that_go_into_list["Available capacity"] = 5-response2[0]
# #         return_list_of_dict.append(dict_that_go_into_list)

# #     return return_list_of_dict

# # projectLisDict = SWEProject(' in-progress',9)
# # print(type(projectLisDict[0]["Available capacity"]))
# # project_ID = 1
# # cmd = "INSERT INTO Project(PROJECTID, ORDERID, MANAGERID, State) VALUES("
# # cmd = cmd + "555555" + "," + "6666666" + "," + "777777" + "," + "'" + "str(state)" +"'"+ ")"
# # connect.query_insertORdelete(cmd)

# cmd = "INSERT INTO Project_SWE(PROJECTID,SWEID) VALUES("
# cmd = cmd + "555555" + "," + "1111111" +")"
# connect.query_insertORdelete(cmd)

# def SWEProject(state, swe_id=None):
#     # if swe_id == None -> find all swe_id
#     # else only search for the specified swe_id
#     # check Project_SWE table: find the same swe_id. summarize all the project_id that the swe has worked on
#     # check Project table: check the project state, if the state is same as required, add to the list
#     # return a list of projectIDs which are in the required state
#     # return 
#     # 安安GO~     change to: return a list of dictionary
#     if swe_id == None:
#         #SQL:
#         return_list_of_dict = []
#         dict_that_go_into_list = {}
#         cmd = "SELECT SWEID,Name FROM SWE"
#         response = connect.queryALL(cmd)
#         SWE_ID = clean_tuple(response,0)
#         SWE_Name = clean_tuple(response,1)
#         for i in range(len(SWE_ID)):
#             dict_that_go_into_list["SWE_id"] = SWE_ID[i]
#             dict_that_go_into_list["Name"] = SWE_Name[i]
#             cmd2 = "SELECT COUNT(PS.PROJECTID) FROM Project P,Project_SWE PS WHERE PS.PROJECT = P.PROJECTID and PS.SWEID = "
#             cmd2 = cmd2 + str(SWE_ID[i]) +" and P.State =" + "'" + state + "'"
#             response2 = connect.queryALL(cmd2)
#             response2 = clean_tuple(response2,0)
#             dict_that_go_into_list["Available capacity"] = 5-response2[0]
#             return_list_of_dict.append(dict_that_go_into_list)
#     else:
#         #SQL:
#         return_list_of_dict = []
#         dict_that_go_into_list = {}
#         cmd = "SELECT SWEID,Name FROM SWE WHERE SWEID = "
#         cmd = cmd + str(swe_id)
#         response = connect.queryALL(cmd)
#         SWE_ID = clean_tuple(response,0)
#         SWE_Name = clean_tuple(response,1)
#         dict_that_go_into_list["SWE_id"] = SWE_ID[0]
#         dict_that_go_into_list["Name"] = SWE_Name[0]
#         cmd2 = "SELECT COUNT(PS.PROJECTID) FROM Project P,Project_SWE PS WHERE PS.PROJECTID = P.PROJECTID and PS.SWEID = "
#         cmd2 = cmd2 + str(SWE_ID[0])+" and P.State = " +"'" +state + "'"
#         print(cmd2)
#         response2 = connect.queryALL(cmd2)
#         response2 = clean_tuple(response2,0)
#         dict_that_go_into_list["Available capacity"] = 5-response2[0]
#         return_list_of_dict.append(dict_that_go_into_list)

#     return return_list_of_dict

# a = SWEProject(' in-progress',1)
# print(a)
# cmd = "SELECT SWEID,Name FROM SWE WHERE SWEID = "
# cmd = cmd + str(2)
# response = connect.queryALL(cmd)
# print(response)
# SWE_ID = clean_tuple(response,0)
# SWE_Name = clean_tuple(response,1)
# print(SWE_ID[0])
# print(SWE_Name[0])
# cmd = "SELECT SWEID FROM SWE WHERE SWEID = 5"
# response = connect.queryALL(cmd)
# response = clean_tuple(response,0)
# print(response)

# URL = "http://127.0.0.1:5000/api/project/active/833"
  
# # location given here 
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 
  
# # sending get request and saving the response as response object 
# r = requests.get(URL) 
  
# # extracting data in json format 
# data = r.json() 
  
  
# # extracting latitude, longitude and formatted address  
# # of the first matching location 
# id = data["project_id"] 
# task = data["task"]
# # printing the output 
# print(int(id))
# print(task)


# URL = "http://127.0.0.1:5000/api/project/new_projects"
# print("Please enter SWE ID : ")
# swe_id = input()
# print("Please enter Manager ID : ")
# manage_id = input()
# print("Please enter Project ID : ")
# project_id = input()
# print("Please enter Order ID : ")
# order_id = input()
# print("Please enter State : ")
# state = input()
# swe_id = swe_id.split(" ")
# data_send = {"SWE ID":swe_id,"Manager ID":manage_id,"Project ID":project_id,"Order ID":order_id,"State":state}
# r = requests.post(URL,json = data_send)
# if r.status_code == 200:
#      print("successfully added!")


# URL = "http://127.0.0.1:5000/api/project/task/"
# print("Please enter project ID : ")
# project_id = input()
# URL = URL + project_id
# print("Please enter Resources : ")
# resource = input()
# print("Please enter State : ")
# state = input()
# print("Please enter Category : ")
# category = input()
# print("Please enter Resource Amount : ")
# r_amount = input()
# data_send = {"project ID":project_id,"Resources":resource,"State":state,"Category":category,"Resource Amount":r_amount}
# r = requests.post(URL,json = data_send)
# if r.status_code == 200:
#     print("successfully added!")


# URL = "http://127.0.0.1:5000/api/project/active"
# r = requests.get(URL)
# response = r.json()
# print(response["No_id"]," projects")
# cnt = 0
# print_dataList = []
# while cnt < len(response["Projects"]):
#     print_dataList.append(response["Projects"][cnt:cnt+5])
#     cnt = cnt + 5
# print (tabulate(print_dataList))

# URL = "http://127.0.0.1:5000/api/project/active/" + "833"
# r = requests.get(URL)
# response = r.json()
# print(response["project_id"]," is the project's ID")
# cnt = 0
# print_dataList = []
# while cnt < len(response["task"]):
#     print_dataList.append(response["task"][cnt:cnt+5])
#     cnt = cnt + 5
# print (tabulate(print_dataList,headers = ["Task"]))

# print("Please enter Project ID : ")
# project_id = input()
# URL = "http://127.0.0.1:5000/api/project/talent/" + project_id
# r = requests.get(URL)
# response = r.json()
# print_dataList = []
# for i in range(len(response)):
#     tempt = []
#     tempt.append(response[i]["Name"])
#     tempt.append(response[i]["Job title"])
#     tempt.append(response[i]["Talent"])
#     print_dataList.append(tempt)
# print(tabulate(print_dataList,headers = ["Name","Job Title","Talent"]))
# URL = "http://127.0.0.1:5000/api/project/availability/1001"
# r = requests.get(URL)
# print(r)
# response = r.json()
# print(response)
# print_dataList = []
# for i in range(len(response)):
#     tempt = []
#     tempt.append(response[i]["SWE_id"])
#     tempt.append(response[i]["Name"])
#     tempt.append(response[i]["Available capacity"])
#     print_dataList.append(tempt)
# print(tabulate(print_dataList,headers = ["SWE ID","Name","Avaliable Capacity"]))   



cmd = "SELECT SWEID,Name FROM SWE"
response = connect.queryALL(cmd)
SWE_ID = clean_tuple(response,0)
SWE_Name = clean_tuple(response,1)
print(response)
print(SWE_ID)
print(SWE_Name)








