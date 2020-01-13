from mysql_conf import *
import json
connect = MySQL_query()
'''
state = " finished"
state_string = "'" + state + "'"
task_id = "2"
cmd = "UPDATE Task SET state = " + state_string +" WHERE taskID = " + task_id
connect.query_insertORdelete(cmd)
'''
cmd = "SELECT * FROM Task WHERE taskID = 2"
reponse = connect.queryALL(cmd)
print(reponse)
#cmd = "INSERT INTO Task(taskID, state, category) VALUES(1001,' notstart','chatbot')"
#connect.query_insertORdelete(cmd)
'''
cmd = "SELECT * FROM Task"
response = connect.queryALL(cmd)
print(response)
'''