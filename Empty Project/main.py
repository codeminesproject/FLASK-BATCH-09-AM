"""
to setup flask app first install package pip install flask
"""

# import Flask
from flask import Flask,render_template

# create object of class with parameter __name__
# when we run program, value of __name__: __main__ is passed as a parameter
# object of Flask is created as obj
obj = Flask(__name__)

@obj.route("/")
def home():
    return render_template("index.html")

# first check if value of name is __main__ then only flask app will run on borwser
if __name__=="__main__":
    # it run flask app and open page on browser
    obj.run()