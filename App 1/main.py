
from flask import Flask,render_template,redirect

obj=Flask(__name__)

@obj.route("/")
def home():
    return redirect("login")

@obj.route("/login")
def login():
    return render_template("login.html")

@obj.route("/register")
def register():
    return render_template("register.html")

if __name__=="__main__":
    obj.run()