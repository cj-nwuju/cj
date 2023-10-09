from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>Hello, World! My first Flask App</h1>"