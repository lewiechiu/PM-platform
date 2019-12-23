from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/api/project/new_projects', methods = ['POST'])
def new_project_api():
    return jsonify({"status": 200})
