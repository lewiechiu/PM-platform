import requests
from interfaces import *
from interfaces.order import *
from interfaces.swe import *

if __name__ == '__main__':
    while 1:
        print('''Project Management Software platform in command line version....
    p : project page
    sa: sales page
    sw: swe page
    o : order page
    Choose from the above:''')
        option = input("--> ")
        if option == "p":
            project()
        elif option == "sa":
            sales()
        elif option == "sw":
            swe()
        elif option == "o":
            order()
        else:
            print("invalid option, please try again !!!")
