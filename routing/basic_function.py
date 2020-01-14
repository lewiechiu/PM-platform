from mysql_conf import *
con = MySQL_query()


def SalesmanExist(salesman_id):
    # check if salesman_id exists
    res = con.queryALL("SELECT EXISTS(SELECT * FROM DB2019FP.Salesman WHERE SALESMANID={})".format((salesman_id)))
    return res[0][0]

def TalentExist(Talent):
    res = con.queryALL("SELECT EXISTS(SELECT * FROM DB2019FP.Talent WHERE Talent={})".format((Talent)))
    return res[0][0]

def SWEExist(swe_id):
    # check if swe_id exists
    return True