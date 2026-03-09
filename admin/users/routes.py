from flask import Blueprint,render_template

users=Blueprint('users',__name__,url_prefix='/users',template_folder='templates',static_folder='static')

@users.route("/")
def users_home():
    return render_template("users/list.html")

@users.route("/create")
def create_user():
    return "Create user"