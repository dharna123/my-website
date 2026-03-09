from  . import admin
from .users.routes import users
from flask import render_template



@admin.route("/")
def dashboard():
    return render_template("admin/dashboard.html")

admin.register_blueprint(users)

