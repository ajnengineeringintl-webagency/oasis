from flask import Flask, jsonify, url_for, render_template, redirect, session, flash, request, Blueprint
from app.database import Users, Blog

from app import db
blog=Blueprint("blog",__name__)

@blog.route("/")
def blogpage():
  return render_template("blog.html")
@blog.route("/user/login",methods=["GET","POST"])
def user_log():
  if request.method == "POST":
    email = request.form["email"]
    passw = request.form["passw"]
     
    user = Users.query.get_or_404(email=email)
    try:
      db.session.commit()
    
      if user is not None:
        #check(user.password,passw)
        if user.passw == passw:
          session["user"] = user.dt()
          print(user.dt())
          return redirect(url_for("blog.blogpage"))
        else:
          flash("you have wrong credentials")
          return redirect(url_for("blog.user_log"))
      else:
        flash("you have wrong credentials")
        return redirect(url_for("blog.user_log"))
    except Exception as e:
      flash("you have wrong credentials")
      return f'[{"err":{e}}]'
  return render_template("blog/blog.html")
  
@blog.route("/user/signup",methods=["GET","POST"])
def user_sup():
  if request.method == "POST":
    name = request.form["email"]
    email = request.form["email"]
    passw = request.form["passw"]
     
    user = Users(name=name,email=email,passw=passw)
    try:
      db.session.add()
      db.session.commit()
      return redirect(url_for("blog.blogpage"))
          
    except Exception as e:
      flash("something wrong ")
      return f'[{"err":{e}}]'
 
  return render_template("blog/blog.html")
  

  