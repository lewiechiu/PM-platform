from flask import Flask, render_template, jsonify, request, Blueprint, abort
order = Blueprint('order', __name__, template_folder='../templates')

@order.route('/api/cust/', methods = ['POST'])
def cust_api():
    return jsonify({"status": 200})


# Create
# Order and assign sales
# Check resource (Machine, SWE, MGR) availability
# # of talent in each field (SWE’s cases < 3)
# server resource
# budget
# Create Projects.
# Allocate SWE, Resources.
# Assign Manager.
# Allocate Dev Team.

# Read
# View order priority 
# Formula: consider time and price
# Know the current progress of each child project
# Contain a set of projects.  
# Each project itself can link to its own project management page.
# show responsible salesman

# Update
# Update an order.
# Modify an order’s project, ending date.

# Delete
# An order can be marked as due when the day of 交付 has arrived.
# Release the resources occupied by the projects.


@order.route('/api/order', methods = ["POST"])
def create_api():

    return 