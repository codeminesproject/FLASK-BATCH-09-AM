from flask import Flask,render_template,request,redirect,session
from DBOperation import getSingleData

obj = Flask(__name__)

obj.secret_key="Y29kZW1pbmVzX2NvbXB1dGVyX2luc3RpdHV0ZQ=="

@obj.route("/admin-login",methods=["GET","POST"])
def adminLogin():
    if request.method=="POST":
        username = request.form.get("txtUsername")
        password = request.form.get("txtPassword")

        query = f"select * from admin_login where username='{username}'"

        user_response = getSingleData(query)
        if user_response is not None:
            if user_response[2]==password:
                session["admin_user"]=user_response
                return redirect("dashboard")
            else:
                message = "Invalid Password"
        else:
            message = "Incorect username"
        return render_template("admin-login.html",message=message)


    return render_template("admin-login.html")

@obj.route("/dashboard")
def dashboard():
    admin_user = session.get("admin_user")
    if admin_user is None:
        return redirect("admin-login")
    return render_template("dashboard.html")

if __name__=="__main__":
    obj.run()