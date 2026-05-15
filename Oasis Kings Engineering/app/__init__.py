
from flask import Flask, jsonify, url_for, render_template, redirect, session, flash, request, Blueprint
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()
load_dotenv()
def server():
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config["SECRET_KEY"] = "q....,,,.,.,.,.,..,"
  
  db.init_app(app)
  
  from .blogr import blog
  from .contactr import pages
  
  
  with app.app_context():
    from .database import Users, Blog
    db.create_all()
  app.register_blueprint(pages,url_prefix="/")    
  app.register_blueprint(blog,url_prefix="/blog")    
  
  return app