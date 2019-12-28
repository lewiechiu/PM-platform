import mysql.connector

def make_connection():
    mydb = mysql.connector.connect(
        host="114.32.23.161",
        user="DBMS2019",
        passwd="fu. wu/6vu;6"
    )

    if mydb:
        return mydb
