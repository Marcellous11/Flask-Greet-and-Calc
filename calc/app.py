# Put your app in here.
# from requests import request
# from flask import request
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def landing():
    return 'This is where is all starts'

# @app.route('/math')
# def math_start():
#     return 'Here you can do some math operations'
# @app.route('/')
# def landing():
#     return 'This is where is all starts'

methods = {"add": add,
            "sub":sub, 
            "mult":mult,
            "div":div
            }

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  f'When you {operation} {a} and {b}, you get {methods[operation](a,b)}'

    return result
