

from flask import Flask,render_template,request,session,redirect

obj = Flask(__name__)

obj.secret_key="codemines_computer_institute"

@obj.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name = request.form.get("txtName")
        session["user_name"] = name # set session
        return redirect("about")
    return render_template("index.html")

@obj.route("/about")
def about():
    p_name = session.get("user_name") # get session
    return render_template("about.html",name=p_name)

if __name__=="__main__":
    obj.run()