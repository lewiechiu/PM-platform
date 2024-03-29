from flask import Flask, render_template, jsonify, request, make_response, abort, blueprints
import routing
from routing.project import project
from routing.order import order
from routing.salesman import salesman
from routing.swe import swe
# from routing.crew import crew
from mysql_conf import *

app = Flask(__name__)
tmp = MySQL_query()
# print(tmp.query("SELECT * FROM db2019FP.Bugs;"))


app.register_blueprint(project)
app.register_blueprint(order)
app.register_blueprint(salesman)
app.register_blueprint(swe)

@app.errorhandler(404)
def NOT_FOUND():
    return make_response(jsonify({"status": 404}))

@app.route('/', methods=['GET', 'POST'])
def starting():
    return render_template('main.html')

@app.route('/<pageName>', methods=['GET'])
def page(pageName):
    return render_template(pageName)
  

if __name__ == '__main__':
    app.run(debug=True)
