import json
import requests
from tabulate import tabulate

def sales():
    while True:
        print('''
        Salesman view....
        c : Create
        r : Read
        u : Update
        ''')
        option = input()

        if option == "":
            print("return to main")
            break
        elif option == "c":
            print("hi")
        elif option == "r":
            print('''
            Read mode....
            e : show the experience of a salesman
            t : who has this talent
            at : get all the talent from every salesman
            i : get salesman's information
            c : get the customer that the salesman has
            ''')
            R_option = input()
            if R_option == "c":
                print("Please enter Salesman ID : ")
                salesman_id = input()
                URL = "http://127.0.0.1:5000/api/salesman/get_customer/" + salesman_id
                r = requests.get(URL)
                response = r.json()
                print("CompanyName : ",response[0]["CompanyName"])
                print("CustomerName : ",response[0]["CustomerName"])
            
