
from flask import Flask, render_template
app = Flask(__name__, template_folder="template")

@app.route('/', methods=['GET', 'POST'])
def starting():
    return render_template('main.html')

@app.route('/salesman.html', methods=['GET'])
def sales_page():
    return render_template('salesman.html')

if __name__ == '__main__':
    app.run(debug=True)
