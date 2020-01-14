from mysql_conf import *

connect = MySQL_query()
resp = connect.queryALL("SELECT * FROM db2019FP.resource WHERE `capacity` > 10000;")

for i in resp:
    print(i)
