from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index() :
    return "index"

@app.route("/login")
def login() :
    return "login"

@app.route('/user/<username>')
def profile(username) :
    return '{}\'s profile'.format(username)

@app.route('/url')
def url() :
    return f'''<p>{url_for('index')}</p>
    <p>{url_for('login')}</p>
    <p>{url_for('login', next='/')}</p>
    <p>{url_for('profile', username='John Doe')}</p>
    '''