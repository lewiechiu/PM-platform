import mysql.connector


class MySQL_query:
    def __init__(self):
        self.con = mysql.connector.connect(host = "114.32.23.161", user = "DBMS2019", passwd = "fu. wu/6vu;6")
        self.cur = self.con.cursor()
    def queryALL(self, cmd):
        self.cur.execute(cmd)
        return self.cur.fetchall()
    def query1(self, cmd):
        self.cur.execute(cmd)
        return self.cur.fetchone()
    def __del__(self):
        self.cur.close()
        self.con.close()