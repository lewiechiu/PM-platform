import mysql.connector

def clean_tuple(response,position):
    return_list = []
    for i in range(len(response)):
        return_list.append(response[i][position])
    return return_list

class MySQL_query:
    def __init__(self):
        self.con = mysql.connector.connect(host = "114.32.23.161", user = "DBMS2019", passwd = "fu. wu/6vu;6",database = "DB2019FP")
        self.cur = self.con.cursor()
    def queryALL(self, cmd):
        self.cur.execute(cmd)
        return self.cur.fetchall()
    def query1(self, cmd):
        self.cur.execute(cmd)
        return self.cur.fetchone()
    def query_insertORdelete(self, cmd):
        self.cur.execute(cmd)
        self.con.commit()
    #    return self.cur.fetchone()
    def get_cur(self):
        return self.cur
    
    # def __del__(self):
    #     self.cur.close()
    #     self.con.close()