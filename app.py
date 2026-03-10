from flask import Flask,render_template,request,session,redirect
from flask_migrate import Migrate
from decorators import access_control
from werkzeug.security import generate_password_hash,check_password_hash
from forms import RegisterForm,LoginForm
from flask import Flask
from models import db,User


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:root@localhost/fsd"
app.config["SECRET_KEY"]="secretkey"
db.init_app(app)
migrate=Migrate(app,db)

@app.route("/register",methods=["GET","POST"])
def register():
    
    form=RegisterForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password=form.password.data

        print(name,email,password)
    
    

        user=User.query.filter_by(email=email).first()
        if user:
            return "Email already exists"
        hashed_password=generate_password_hash(password)
        new_user=User(name=name,email=email,password=hashed_password,role="user")
        db.session.add(new_user)
        db.session.commit()
        return "Registeration success"
    else:
        print("FORM ERRORS:", form.errors)
    return render_template("register.html",form=form)

@app.route("/login",methods=["GET","POST"])   
def login():
    form=LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        user=User.query.filter_by(email=email).first()
        
        
        if user and check_password_hash(user.password,password):
            session["user_id"]=user.id
            session["role"]=user.role
            return redirect("/dashboard")

            
        else:
            return "Invalid email or password"
    return render_template("login.html",form=form)

@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/admin")
@access_control
def admin():
     if "user_id" not in session:
        return redirect("/login")
    
     users=User.query.all()
     return render_template("admin.html",users=users)

@app.route("/")
def home():
    return "Hello from Feature Branch"

'''@app.route("/make_admin/<int:id>") 
def make_admin(id):
    if session.get("role")!="admin":
        return "Access denied"
    user=User.query.get(id)
    user.role="admin"
    db.session.commit()
    return redirect("/admin")'''



if __name__=="__main__":
    app.run(debug=True)

