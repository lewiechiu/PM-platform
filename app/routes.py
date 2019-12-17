from app import app

@app.route('/')
@app.route('/index')
def greetings():
    return "Hi"