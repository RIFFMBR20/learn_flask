from flask import Flask, make_response

app = Flask(__name__)  

@app.get("/")
def index():
    response = make_response('hello')
    response.status_code = 200
    return response
