from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/api/cust/', methods = ['POST'])
def cust_api():
    return jsonify({"status": 200})
