from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome"



@app.route('/welcome/<direction>')
def welcome_home(direction):
    if direction == "home":
        return "Welcome home"
    else:
        return f"Welcome back"

# @app.route('/welcome/<back>')
# def welcome_back(back):
#     return 

