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
cmd = "SELECT name FROM SWE WHERE name = 'Alta Radmer'"
response = connect.queryALL(cmd)
response = clean_tuple(response,0)
print(response[0])
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





