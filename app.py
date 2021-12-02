#  _          _   _
# | |    __ _| |_| |__   __ _ _ __ ___   __  ___   _ ____
# | |   / _` | __| '_ \ / _` | '_ ` _ \  \ \/ / | | |_  /
# | |__| (_| | |_| | | | (_| | | | | | |_ >  <| |_| |/ /
# |_____\__,_|\__|_| |_|\__,_|_| |_| |_(_)_/\_\\__, /___|
#                                             |___/
# 
# Created by Matthew R. Latham | Latham.xyz
#

from flask import Flask, render_template, request, redirect
from flask.templating import render_template
import sys
import requests
import http.client
import json

from werkzeug.datastructures import Authorization
from APIToken import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/aaduser")
def login():


    
    username = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')



    # Postman || Get Auth Key
    url = getAuthTokenURL

    payload = json.dumps({
      "username": authUsername,
      "password": authPassword
    })
    headers = {
          'Content-Type': 'application/json',
  'Cookie': 'connect.sid=s%3AxwyeTd9-2uzWf5FSIEMSgF5RiQ3vdxGx.yT04iEyKHuIz6nC6YaZ2KfhsrfGt5c%2B3owu6Cp8L4UE'
    }

    # Parse token from API
    response = requests.request("POST", url, headers=headers, data=payload)
    tokenData = response.text
    parse_json = json.loads(tokenData)
    authorization = parse_json['token']

    newAuthor = 'Bearer ' + authorization

    #print(authorization)




    # Begin Postman Import || Create User Account

    conn = http.client.HTTPSConnection(baseURL)
    payload = json.dumps({
    "username": username,
    "fullname": username,
    "title": "Integration",
    "email": email,
    "groups": [
        "61a80a7c365f365048c1b4da"
    ],
    "role": "61a80a50bba0dd47e4efabc3",
    "password": password,
    "passwordConfirm": password
    })
    headers = {
    'refreshtoken': refreshtoken,
    'Authorization': newAuthor,
    'Content-Type': 'application/json',
    'Cookie': 'connect.sid=s%3AxwyeTd9-2uzWf5FSIEMSgF5RiQ3vdxGx.yT04iEyKHuIz6nC6YaZ2KfhsrfGt5c%2B3owu6Cp8L4UE'
    }
    conn.request("POST", "/api/v2/accounts", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    # End Postman Import
    

    return redirect("http://www.example.com", code=302)


if __name__ == '__main__':
    app.run()