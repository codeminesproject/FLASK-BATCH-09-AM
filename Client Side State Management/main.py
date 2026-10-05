
from flask import Flask,render_template,request,redirect

obj = Flask(__name__)

@obj.route("/")
def home():
    return render_template("index.html")

@obj.route("/about")
def about():
    q_name = request.args.get("name")
    q_mobile = request.args.get("mobile")
    q_address = request.args.get("address")
    return render_template("about.html",name=q_name,mobile=q_mobile,address=q_address)

@obj.route("/contact/<p_name>/<p_mobile>/<p_address>")
def contact(p_name,p_mobile,p_address):
    return render_template("contact.html",name=p_name,mobile=p_mobile,address=p_address)

@obj.route("/registration",methods=["GET","POST"])
def registration():
    if request.method=="POST":
        name = request.form.get("txtName")
        email = request.form.get("txtEmail")
        mobile = request.form.get("txtMobile")
        password = request.form.get("txtPassword")
        url = f"/dashboard?name={name}&email={email}&mobile={mobile}&password={password}"
        #url = f"/dashboard/{name}/{email}/{mobile}/{password}"
        return redirect(url)
    return render_template("registration.html")

@obj.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__=="__main__":
    obj.run()