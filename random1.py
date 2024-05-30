from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    person = {
        'name' : 'john',
        'age' : '25',
        'city' : 'New York'
    }
    return "hello from " + person['city']