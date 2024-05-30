from flask import Flask,request

app = Flask(__name__)

@app.get("/")
def form():
    html="""
    <form action="/" method="post">
        <input type='text' id="firstname" name="firstname">
        <input type='submit'>
    </form>
    """
    return html

@app.post("/")
def submit_form():
    firstname = request.form.get("firstname")
    return f"hello {firstname}"

