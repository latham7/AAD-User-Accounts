from flask import Flask, render_template, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////dev.db'

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")





@app.route("/aaduser")
def login():

    username = request.args.get('username')
    print(username)
    password = request.args.get('password')
    print(password)

    return redirect("http://www.example.com", code=302)


if __name__ == '__main__':
    app.run()