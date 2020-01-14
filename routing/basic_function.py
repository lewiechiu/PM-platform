from mysql_conf import *

def SalesmanExist(salesman_id):
    # check if salesman_id exists
    con.queryALL("SELECT EXIST() ")
    return True


def SWEExist(swe_id):
    # check if swe_id exists
    return True