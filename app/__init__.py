from flask import Flask,session,render_template,jsonify,request,redirect,url_for,make_response,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from .routes import student_bp
    app.register_blueprint(student_bp)
    return app
