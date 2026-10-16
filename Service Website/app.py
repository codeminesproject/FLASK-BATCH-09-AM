from flask import Flask,render_template,request,redirect,session
from DBOperation import getSingleData,insert,getAllData,update,delete

obj = Flask(__name__)

obj.secret_key="Y29kZW1pbmVzX2NvbXB1dGVyX2luc3RpdHV0ZQ=="

@obj.route("/")
def home():
    about_submenu = getAboutSubMenu()
    return render_template("index.html",about_submenu=about_submenu)

def getAboutSubMenu():
    query = "select id,menu_name from about"
    response = getAllData(query)
    about_data = []
    if len(response)>0:
        for data in response:
            about_dict = {}
            about_dict["id"]=data[0]
            about_dict["name"]=data[1]
            about_data.append(about_dict)
    return about_data

@obj.route("/about")
def getAbout():
    about_submenu = getAboutSubMenu()
    id = request.args.get("id")
    if request.method=="GET":
        if int(id)>0:
            query = f"select * from about where id={id}"
            about_data = getSingleData(query)
            if about_data is not None:
                return render_template("about.html",menuname=about_data[1],menutitle=about_data[2],description=about_data[3],id=about_data[0],about_submenu=about_submenu)
            else:
                return render_template("manage-about.html",id=int(id))



@obj.route("/admin-login",methods=["GET","POST"])
def adminLogin():
    if request.method=="POST":
        username = request.form.get("txtUsername")
        password = request.form.get("txtPassword")

        query = f"select * from admin_login where username='{username}'"

        user_response = getSingleData(query)
        if user_response is not None:
            if user_response[3]==password:
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
    return render_template("dashboard.html",user_name=admin_user[1])

@obj.route("/admin-about")
def adminAbout():
    admin_user = session.get("admin_user")
    if admin_user is None:
        return redirect("admin-login")

    query = "select id,menu_name,menu_title,description from about"
    response = getAllData(query)
    about_data = []
    if len(response)>0:
        for data in response:
            about_dict = {}
            about_dict["id"]=data[0]
            about_dict["name"]=data[1]
            about_dict["title"]=data[2]
            about_dict["description"]=data[3]
            about_data.append(about_dict)
    return render_template("admin-about.html",user_name=admin_user[1],data = about_data)

@obj.route("/manage-about",methods=["GET","POST"])
def manageAbout():
    admin_user = session.get("admin_user")
    if admin_user is None:
        return redirect("admin-login")

    id = request.args.get("id")
    if request.method=="GET":
        if int(id)>0:
            query = f"select * from about where id={id}"
            about_data = getSingleData(query)
            if about_data is not None:
                return render_template("manage-about.html",menuname=about_data[1],menutitle=about_data[2],description=about_data[3],id=about_data[0])
        else:
            return render_template("manage-about.html",id=int(id))

    if request.method=="POST":
        id = request.form.get("id")
        name = request.form.get("menuname")
        title = request.form.get("menutitle")
        description = request.form.get("description")
        

        if int(id)>0:
            updated_by = admin_user[0]
            query = f"update about set menu_name='{name}',menu_title='{title}',description='{description}',updated_by={updated_by},edited_date=NOW() where id={id}"
            response = update(query)
        else:
            created_by = admin_user[0]
            query = f"insert into about(menu_name,menu_title,description,created_by) values('{name}','{title}','{description}',{created_by})"
            response = insert(query)
        if response==True:
            return redirect("admin-about")
        else:
            return render_template("manage-about.html",user_name=admin_user[1],message="Insert failed")
    

@obj.route("/delete-about",methods=["GET"])
def deleteAbout():
    id = request.args.get("id")
    if int(id)>0:
        query = f"delete from about where id={id}"
        response = delete(query)
        return redirect("admin-about")




@obj.route("/admin-logout")
def adminLogout():
    session.clear()
    return redirect("admin-login")

if __name__=="__main__":
    obj.run()