from flask import Flask, render_template, request
from flask.templating import render_template

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