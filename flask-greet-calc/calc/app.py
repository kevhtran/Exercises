# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    "add a and b parameters"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = add(a,b)
    return str(results)

@app.route("/sub")
def subtraction():
    "subtract b from a parameters"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = sub(a,b)
    return str(results)

@app.route("/mult")
def multiply():
    "multiply a and b parameters"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = mult(a,b)
    return str(results)

@app.route("/div")
def division():
    "divide a and b parameters"
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results = div(a,b)
    return str(results)