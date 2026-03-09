from . import db


student_course=db.Table(
    "student_course",
    db.Column("student_id",db.Integer,db.ForeignKey("student.id")),
    db.Column("course_id",db.Integer,db.ForeignKey("course.id"))

)

class Student(db.Model):
    #__tablename__="students_"

    id=db.Column(db.Integer,primary_key=True)
    courses=db.relationship("Course",secondary=student_course,backref="students123")
    #name=db.Column(db.String(100))
    #courses=db.relationship("Course",backref="student",lazy=True)

   

    def __repr__(self):
        return f"{self.name} {self.course} {self.email}"
    
class Course(db.Model):
    __tablename__="courses"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    #course_name=db.Column(db.String(100))
    #student_id=db.Column(db.Integer,db.ForeignKey("students_.id"))

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile=db.relationship("Profile",backref="user",uselist=False)


class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"),unique=True)



