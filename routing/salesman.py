from flask import Flask, render_template, jsonify, request, Blueprint, abort
salesman = Blueprint('salesman', __name__, template_folder='../templates')

@salesman.route('/api/sales/', methods = ['POST'])
def sales_api():
    return jsonify({"status": 200})