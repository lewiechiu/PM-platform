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
    res = con.queryALL("SELECT EXISTS(SELECT * FROM DB2019FP.SWE WHERE SWEID={})".format((swe_id)))
    return res[0][0]


def SelectByTalent(Talent):
    exist = TalentExist(Talent)
    if not exist:
        return abort(400, "Talent: {} does NOT EXIST".format(Talent))
    
    TABLE = "DB2019FP.Talent"
    SQL_command = "SELECT ID FROM {} WHERE Talent={};".format(TABLE, Talent)
    cursor = con.get_cur()
    cursor.execute(SQL_command)
    IDLis = [i[0] for i in cursor.fetchall()]
    resp = []
    print(SQL_command)
    print(IDLis)
    for _id in IDLis:
        if(int(_id)%2==0):
            #salesman
            TABLE = "DB2019FP.Salesman"
            SQL_command = "SELECT Name, Title FROM {} WHERE SALESMANID={};".format(TABLE, _id)
        else:
            #swe
            TABLE = "DB2019FP.SWE"
            SQL_command = "SELECT Name, Title FROM {} WHERE SWEID={};".format(TABLE, _id)
        
        cursor.execute(SQL_command)
        Name, Title = cursor.fetchall()[0]
        header = ['ID','Name','Title']
        values = [_id, Name,Title]
        resp.append(dict(zip(header,values)))

    return (resp)