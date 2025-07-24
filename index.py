from flask import Flask
from main import client

app = Flask(__name__)

@app.route("/")
def index():
    client.login("PUT THE TOKEN IN HERE")
    return "Running !"
