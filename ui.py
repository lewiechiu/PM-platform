import requests
from interfaces import *

if __name__ == '__main__':
    app.run(debug=True)

    print('''
    DB 2019 final project....
    p : project page
    sa: sales page
    sw: swe page
    o : order page
    ''')
    option = input()
    if option == "p":
        project()
    elif option == "sa":
        sales()
    elif option == "sw":
        swe()
    else:
        order()
    return