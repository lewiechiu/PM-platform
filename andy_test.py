from flask import Flask, render_template, jsonify, request, Blueprint, abort
from mysql_conf import *
crew = Blueprint('crew', __name__, template_folder='../templates')

connect = MySQL_query()
id = 50
a = "SELECT MAX(ID) FROM SWE"
repo = connect.queryALL(a)
print(repo[0][0])
