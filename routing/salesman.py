from flask import Flask, render_template, jsonify, request, Blueprint, abort
salesman = Blueprint('salesman', __name__, template_folder='../templates')




# show the ranking of each salesman by performance.
# Know what each salesman is accountable for. (sales item)
# Set KPI for each of the salesmen.
# Show the customer SalesMan are related to

# Update the time period for the crew in the company
# Promote a crew to Manager or Senior SWE





@salesman.route('/api/sales/', methods = ['POST'])
def sales_api():
    return jsonify({"status": 200})

@salesman.route('/api/sales/ranking/', methods = ['GET'])
def sales_ranking(id):
    # Query all the salesman id and their performance status?
    # sort by the performance ranking 
    return 