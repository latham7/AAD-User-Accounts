from flask import Flask, render_template, request, redirect
from flask.templating import render_template
import sys
import http.client
import json
from APIToken import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/aaduser")
def login():


    
    username = request.args.get('username')
    password = request.args.get('password')


    # Begin Postman Import || Create User Account

    conn = http.client.HTTPSConnection("support.cammit.co")
    payload = json.dumps({
    "username": username,
    "fullname": username,
    "title": "Integration",
    "email": "joesmith3435@gmail.com",
    "groups": [
        "6179f6af33a2d75c8ac7405a"
    ],
    "role": "6179f582c526d95beab4d393",
    "password": password,
    "passwordConfirm": password
    })
    headers = {
    'refreshtoken': refreshtoken,
    'Authorization': authorization,
    'Content-Type': 'application/json',
    'Cookie': 'connect.sid=s%3AxwyeTd9-2uzWf5FSIEMSgF5RiQ3vdxGx.yT04iEyKHuIz6nC6YaZ2KfhsrfGt5c%2B3owu6Cp8L4UE'
    }
    conn.request("POST", "/api/v2/accounts", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    # End Postman Config Import


    print(refreshtoken)
    

    return redirect("http://www.example.com", code=302)


if __name__ == '__main__':
    app.run()