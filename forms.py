from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class RegisterForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired(),Length(min=3)])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=5)])
    email=StringField("Email",validators=[DataRequired(),Email()])
   
class LoginForm(FlaskForm):
    password=PasswordField("Password",validators=[DataRequired(),Length(min=5)])
    email=StringField("Email",validators=[DataRequired(),Email()])