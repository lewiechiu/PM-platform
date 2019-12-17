
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def starting():
    return render_template('main.html')

@app.route('/<pageName>', methods=['GET'])
def page(pageName):
    return render_template(pageName)


if __name__ == '__main__':
    app.run(debug=True)
