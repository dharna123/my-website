from flask import Blueprint,Flask,session,render_template,jsonify,request,redirect,url_for,make_response,request
from .models import Student
from . import db

student_bp=Blueprint("students",__name__)



@student_bp.route("/add",methods=["GET","POST"])
def add_student():
    if request.method=="POST":
        name=request.form["name"]
        course=request.form["course"]
        email=request.form["email"]
        student=Student(name=name,course=course,email=email)
        db.session.add(student)
        db.session.commit()
        return redirect("/")
    return render_template("add_student.html")


@student_bp.route("/")
def index():
    students=Student.query.all()
    return render_template("index.html",students=students)


@student_bp.route("/edit/<int:id>")
def edit_student(id):
    student=Student.query.get(id)
    return render_template("edit_student.html",student=student)



@student_bp.route("/update/<int:id>",methods=["POST"])
def update_student(id):
    student=Student.query.get(id)
    student.name=request.form["name"]
    student.course=request.form["course"]
    student.email=request.form["email"]
    db.session.commit()
    return redirect("/")

@student_bp.route("/delete/<int:id>")
def delete_student(id):
    student=Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect("/")