import json
import requests
from tabulate import tabulate

def project():
    
    print('''
    Project view....
    c : Create
    r : Read
    u : Update
    ''')

    option = input()
    if option == "c":
        print('''
        Create mode....
        p : Create new project
        t : Create new task for a project
        ''')
        C_option = input()
        if C_option == "p":
            URL = "http://127.0.0.1:5000/api/project/new_projects"
            print("Please enter SWE ID : ")
            swe_id = input()
            print("Please enter Manager ID : ")
            manage_id = input()
            print("Please enter Project ID : ")
            project_id = input()
            print("Please enter Order ID : ")
            order_id = input()
            print("Please enter State : ")
            state = input()
            swe_id = swe_id.split(" ")
            data_send = {"SWE ID":swe_id,"Manager ID":manage_id,
                    "Project ID":project_id,"Order ID":order_id,"State":state}
            r = requests.post(URL,json = data_send)
            if r.status_code == 200:
                print("successfully added!")
        elif C_option == "t":
            URL = "http://127.0.0.1:5000/api/project/task/"
            print("Please enter project ID : ")
            project_id = input()
            URL = URL + project_id
            print("Please enter Resources : ")
            resource = input()
            print("Please enter State : ")
            state = input()
            print("Please enter Category : ")
            category = input()
            print("Please enter Resource Amount : ")
            r_amount = input()
            data_send = {"project ID":project_id,"Resources":resource,"State":state,"Category":category,"Resource Amount":r_amount}
            r = requests.post(URL,json = data_send)
            if r.status_code == 200:
                print("successfully added!")
        return True
    elif option == "r":
        print('''
        Read mode....
        a : Get active projects or active tasks under a specified project
        t : Get SWE Name , Job title ,and Talent which involed in a specified project
        ga : Get all SWEs' or a specified SWE's avalible capacity for work
        ''')
        R_option = input()
        if R_option == "a":
            print("Specified project? Please enter Project ID or 'n'")
            project_id = input()
            if(project_id == "n"):
                URL = "http://127.0.0.1:5000/api/project/active"
                r = requests.get(URL)
                response = r.json()
                print(response["No_id"]," projects")
                cnt = 0
                print_dataList = []
                while cnt < len(response["Projects"]):
                    print_dataList.append(response["Projects"][cnt:cnt+5])
                    cnt = cnt + 5
                print (tabulate(print_dataList))
            elif:
                URL = "http://127.0.0.1:5000/api/project/active/" + project_id
                r = requests.get(URL)
                response = r.json()
                print(response["project_id"]," is the project's ID")
                cnt = 0
                print_dataList = []
                while cnt < len(response["task"]):
                    print_dataList.append(response["task"][cnt:cnt+5])
                    cnt = cnt + 5
                print (tabulate(print_dataList,headers = ["Task"]))
        elif R_option == "t":
            print("Please enter Project ID : ")
            project_id = input()
            URL = "http://127.0.0.1:5000/api/project/talent/" + project_id
            r = requests.get(URL)
            response = r.json()
            print_dataList = []
            for i in range(len(response)):
                tempt = []
                tempt.append(response[i]["name"])
                tempt.append(response[i]["Job title"])
                tempt.append(response[i]["Talent"])
                print_dataList.append(tempt)
            print(tabulate(print_dataList,headers = ["Name","Job Title","Talent"]))
        elif R_option == "ga":
            print("All SWE or specified? Please enter SWE ID or 'A'")
            swe_id = input()
            if swe_id == "A":
                URL = "http://127.0.0.1:5000/api/project/availability/"
                r = requests.get(URL)
                response = r.json()
                print_dataList = []
                for i in range(len(response)):
                    tempt = []
                    tempt.append(response[i]["SWE_id"])
                    tempt.append(response[i]["Name"])
                    tempt.append(response[i]["Avaliable capacity"])
                    print_dataList.append(tempt)
                print(tabulate(print_dataList,headers = ["SWE ID","Name","Avaliable Capacity"]))   
            elif:
                URL = "http://127.0.0.1:5000/api/project/availability/" + swe_id
                r = requests.get(URL)
                response = r.json()
                print_dataList = []
                for i in range(len(response)):
                    tempt = []
                    tempt.append(response[i]["SWE_id"])
                    tempt.append(response[i]["Name"])
                    tempt.append(response[i]["Avaliable capacity"])
                    print_dataList.append(tempt)
                print(tabulate(print_dataList,headers = ["SWE ID","Name","Avaliable Capacity"]))       
            return True
    elif option = "u":









            