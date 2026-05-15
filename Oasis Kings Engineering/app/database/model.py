from app import db
from flask_sqlalchemy import SQLAlchemy
class Users(db.Model):
  __tablename__ = "Users"
  name= db.Column(db.Text,primary_key=True)
  userid= db.Column(db.Integer,primary_key=True)
  email= db.Column(db.Text,nullable=False,unique=True)
  passw= db.Column(db.Text,nullable=False)
  posts= db.Relationship("Blog",backref="user",lazy=True)
  joined=db.Column(db.Date(), default=db.func.now())
  
  def dt(self):
    return {"name":self.name,"userid":self.userid,"email":self.email,"password":self.passw,"joined":self.joined,"posts":self.posts}

class Blog(db.Model):
  __tablename__ = "Blog"
  title= db.Column(db.String(),nullable=False)
  blogid= db.Column(db.Integer,primary_key=True)
  content= db.Column(db.String(),nullable=False)
#  passw= db.Column(db.Text(),nullable=False)
  user= db.Column(db.Integer, db.ForeignKey("Users.userid"), nullable=False)
  made=db.Column(db.Date(), default=db.func.now())
  
  def dt(self):
    return {"title":self.title,"blogid":self.blogid,"content":self.content,"user":self.user,"made":self.made}

