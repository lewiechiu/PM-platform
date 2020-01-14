from mysql_conf import *
con = MySQL_query()


def SalesmanExist(salesman_id):
    # check if salesman_id exists
    con.queryALL("SELECT EXISTS(SELECT * FROM DB2019FP.Salesman WHERE SALESMANID={})".format((salesman_id)))
    return con[0][0]


def SWEExist(swe_id):
    # check if swe_id exists
    return True