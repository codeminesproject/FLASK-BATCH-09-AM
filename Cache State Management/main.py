

from flask import Flask,render_template,request,session,redirect
from flask_caching import Cache

obj = Flask(__name__)

obj.config["CACHE_TYPE"]="SimpleCache"
obj.config["CACHE_DEFAULT_TIMEOUT"]=60
cache = Cache(obj)

@obj.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name = request.form.get("txtName")
        cache.set("user_name",name) # set cache
        return redirect("about")
    return render_template("index.html")

@obj.route("/about")
def about():
    p_name = cache.get("user_name") # get cache
    return render_template("about.html",name=p_name)

if __name__=="__main__":
    obj.run()