import requests
import json
import pprint
import pandas as pd
from tabulate import tabulate
landing_page = '''

##### Order page #####
1). Create    --> Press C
    * Create order
2). Order     --> Press R
    1 Get the each order's priority in ascending order.
    2 Get what's inside each of the project order.
    3 Get which salesman is responsible for what order.
3). Press enter to return.'''

def create_order():
    print(
'''[CREATE] EstablishTime  |   EndTime    |   Deadline   |  SALESMANID  |  Price  |     State     |
   eg.        2019-11-02      2019-11-07     2019-11-05          3         12345     in-progress ''')
    user_type = dict()
    user_type["EstablishTime"] = input("EstablishTime: ")
    user_type["EndTime"] = input("EndTime: ")
    user_type["Deadline"] = input("Deadline: ")
    user_type["SALESMANID"] = int(input("SALESMANID: "))
    user_type["Price"] = int(input("Price: "))
    user_type["State"] = input("State: ")
    # user_type["EstablishTime"] = "2019-11-02"
    # user_type["EndTime"] = "2019-11-07"
    # user_type["Deadline"] = "2019-11-05"
    # user_type["SALESMANID"] = 3
    # user_type["Price"] = 12345
    # user_type["State"] = "in-progress"
    r = requests.post('http://localhost:5000/api/order/', json=user_type)
    print("[CREATE Status]: Finished!\n  Returning to Order page menu")
    return

def get_order_priority():
    print("[GET] Order priority:")
    r = requests.get('http://localhost:5000/api/order/priority')
    r = json.loads(r.text)
    print(tabulate(r[-40:], headers="keys"))
    
    print("The returned ")

def get_order_project():
    print("[GET] Projects within Order")
    print("Search for the projects under the Order")
    id = input("id: ")
    r = requests.get('http://localhost:5000/api/order/project_state/{}'.format(id))
    r = json.loads(r.text)
    print(tabulate(r, headers="keys"))

def get_order_salesman():
    print("[GET] Salesman's Background info whose responsible for an Order")
    id = input("id: ")
    r = requests.get('http://localhost:5000/api/order/salesman/{}'.format(id))
    r = json.loads(r.text)
    print(tabulate(r, headers="keys"))

def order():
    while 1:
        print(landing_page)
        option = input()
        if option == '':
            print("returning to main")
            break
        elif option == 'C':
            create_order()
        elif option == 'R1':
            get_order_priority()
            pass
        elif option == 'R2':
            get_order_project()
        elif option == 'R3':
            get_order_salesman()