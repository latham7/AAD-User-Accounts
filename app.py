from flask import Flask, render_template, request
from flask.templating import render_template
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")




@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    return(username)


if __name__ == '__main__':
    app.run()