

from flask import Flask,render_template,request,make_response,redirect

obj = Flask(__name__)

@obj.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name = request.form.get("txtName")
        resp=make_response(redirect("about"))
        resp.set_cookie("name",name,max_age=120)
        resp.set_cookie("address","Bhayander East")
        return resp
    
    return render_template("index.html")

@obj.route("/about")
def about():
    p_name = request.cookies.get("name")
    return render_template("about.html",name=p_name)

if __name__=="__main__":
    obj.run()