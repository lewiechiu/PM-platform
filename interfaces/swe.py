import requests
import json
import pprint
import pandas as pd
from tabulate import tabulate
landing_page = '''

##### Software Engineer page #####
1). Create   --> Press C
    * Create Software Engineer
2). Read     --> Press R
    1 Get the past project of a software Engineer.
    2 Get SWEs matching specific talents.
    3 Get all the talents of SWEs
    4 Get background info of a Software Engineer.
3). Update   --> Press U
    1. Update background information of Software Engineer
    2. Retire a Software engineer.
*). Press enter to return.'''

def create_SWE():
    user_type = dict()
    columns = ["Name", "Ssn" , "Title", "Salary" , "Age", "YearsOfExperience", "Address","Gender", "State"]

    for i in columns:
        user_type[i] = input(i + " : ")
    # user_type["EstablishTime"] = "2019-11-02"
    # user_type["EndTime"] = "2019-11-07"
    # user_type["Deadline"] = "2019-11-05"
    # user_type["SALESMANID"] = 3
    # user_type["Price"] = 12345
    # user_type["State"] = "in-progress"
    r = requests.post('http://localhost:5000/api/swe/', json=user_type)
    print("[CREATE Status]: Finished!\n  Returning to Order page menu")
    return

def past_project():
    id = input("id : ")
    r = requests.get('http://localhost:5000/api/swe/project_experience/{}'.format(id))
    r = json.loads(r.text)
    print(tabulate(r, headers="keys"))

def swe():
    while 1:
        print(landing_page)
        option = input()
        if option == '':
            print("returning to main")
            break
        elif option == 'C':
            create_SWE()
            
        elif option == 'R1':
            past_project()
