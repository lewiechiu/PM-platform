from flask import Flask, render_template, jsonify, request
import routing
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def starting():
    return render_template('main.html')

@app.route('/<pageName>', methods=['GET'])
def page(pageName):
    return render_template(pageName)

@app.route('/api/', methods=['POST'])
def receive():
    content = request.get_json()
    print(content)
    return jsonify({"type": "good"})

@app.route('/api/sale/', methods = ['POST'])
def sale_api():
    return jsonify({"status": 200})

@app.route('/api/swe/', methods = ['POST'])
def swe_api():
    return jsonify({"status": 200})


@app.route('/api/crew/', methods = ['POST'])
def crew_api():
    return jsonify({"status": 200})
    

if __name__ == '__main__':
    app.run(debug=True)
