from flask import Flask, render_template, jsonify, request, Blueprint, abort
salesman = Blueprint('salesman', __name__, template_folder='../templates')





    # Know what each salesman is accountable for. (sales item)
    # Set KPI for each of the salesmen.
# Show the customer SalesMan are related to
# Update the time period for the crew in the company (repeat)
# Promote a crew to Manager or Senior SWE





@salesman.route('/api/sales/', methods = ['POST'])
def sales_api():
    return jsonify({"status": 200})

# show the ranking of each salesman by performance.
@salesman.route('/api/sales/ranking/', methods = ['GET'])
def sales_ranking(id):
    # We use the number of projects and a salesman has handled as the KPI.
    # This can be decided afterwards.
    # TODO:
    # 1. Query all the salesman id
    # For each of the salesman id, query their "KPI" data.
    # sort the result by some 
    # sort by the performance ranking 
    return 

@salesman.route('/api/sales/')