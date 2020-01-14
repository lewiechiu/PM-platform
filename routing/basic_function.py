from mysql_conf import *
MySQL_query con
def SalesmanExist(salesman_id):
    # check if salesman_id if exists
    con.queryALL("SELECT EXIST() ")
    return True