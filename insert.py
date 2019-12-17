import mysql.connector
import pandas as pd
import ast


mydb = mysql.connector.connect(
    host="114.32.23.161",
    user="DBMS2019", passwd="fu. wu/6vu;6"
)

con = mydb.cursor()
df = pd.read_csv("./fp_data/talent.csv")

for i in range(len(df.talent)):
    print(ast.literal_eval(df.talent[i]))