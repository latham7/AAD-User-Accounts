from flask import Flask, render_template, request
from flask.templating import render_template
import sys

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")





@app.route("/login")
def login():

    username = request.args.get('username')
    password = request.args.get('password')
    
    print('username + password')


if __name__ == '__main__':
    app.run()