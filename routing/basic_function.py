from mysql_conf import *
MySQL_query con
def SalesmanExist(salesman_id):
    # check if salesman_id exists
    con.queryALL("SELECT EXIST() ")
    return True


def SWEExist(swe_id):
    # check if swe_id exists
    return True