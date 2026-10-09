
from flask import Flask,render_template,redirect,request
from DBOperation import insert,getSingleData

obj=Flask(__name__)

@obj.route("/")
def home():
    return redirect("login")

@obj.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form.get("txtUsername")
        password = request.form.get("txtPassword")
        user_data = getEmailData(email)
        if user_data!=None:
            if password==user_data[4]:
                message = "login successfull"
            else:
                message = "invalid username or password"
            return render_template("login.html",message = message)
        else:
            return render_template("login.html",message = "No user found")
    return render_template("login.html")

def getEmailData(email):
    query = f"select id,name,email,mobile,password from student_details where email='{email}'"
    student_data = getSingleData(query)
    return student_data

def getMobileData(mobile):
    query = f"select id,name,email,mobile,password from student_details where mobile='{mobile}'"
    student_data = getSingleData(query)
    return student_data

@obj.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name = request.form.get("txtName")
        email = request.form.get("txtEmail")
        mobile = request.form.get("txtMobile")
        password = request.form.get("txtPassword")
        c_password = request.form.get("txtCPassword")

        email_data = getEmailData(email)
        if email_data!=None:
            return render_template("register.html",message="Email already exist")

        mobile_data = getMobileData(mobile)
        if mobile_data!=None:
            return render_template("register.html",message="Mobile already exist")

        if password!=c_password:
            return render_template("register.html",message="Password and confirm password should be same")

        query = f"insert into student_details(name,email,mobile,password) values('{name}','{email}','{mobile}','{password}')"
        response = insert(query)
        if response==True:
            message = "Account Created Successfully"
        else:
            message = "Account Creation Failed"
        return render_template("register.html",message=message)
    
    return render_template("register.html")

if __name__=="__main__":
    obj.run()