from flask import Flask,render_template,request,session,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask

from flask_cors import CORS


app = Flask(__name__)

#enable cors
CORS(app)




app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:root@localhost/fsd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    age=db.Column(db.Integer)
    course=db.Column(db.String(100))

@app.route("/students",methods=["POST"])
def add_student():
    data=request.json
    student=Student(name=data["name"],age=data["age"],course=data["course"])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message":"Student added"})

@app.route("/students",methods=["GET"])
def show():
    students=Student.query.all()
    result=[]
    for s in students:
        result.append({
            "id":s.id,
            "name":s.name,
            "age":s.age,
            "course":s.course
        })
    return jsonify(result)

@app.route("/students/<int:id>",methods=["GET"])
def get_student(id):
    student=Student.query.get(id)
    if not student:
        return jsonify({"message":"Student not found"}),404
    return jsonify({
        "id":student.id,
        "name":student.name,
        "age":student.age,
        "course":student.course
    })

@app.route("/students/<int:id>",methods=["PUT"])
def update_student(id):
   student= Student.query.get(id)
   if not student:
        return jsonify({"message":"Student not found"}),404
   data=request.json
   student.name=data["name"]
   student.age=data["age"]
   student.course=data["course"]
   db.session.commit()
   return jsonify({"message":"Student updated"})

@app.route("/students/<int:id>",methods=["DELETE"])
def delete_student(id):
   student= Student.query.get(id)
   if not student:
        return jsonify({"message":"Student not found"}),404
   
   db.session.delete(student)
   db.session.commit()
   return jsonify({"message":"Student deleted"})

if __name__=="__main__":
    app.run(debug=True)

