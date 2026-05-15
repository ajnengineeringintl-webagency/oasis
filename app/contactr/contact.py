from flask import Flask, jsonify, url_for, render_template, redirect, session, flash, request, Blueprint

from app import db
pages=Blueprint("pages",__name__)

#
@pages.route("/")
def indexpage():
  return render_template("index.html")
@pages.route("/about")
def aboutpage():
  return render_template("about.html")
@pages.route("/contact")
def contactpage():
  return render_template("contact.html")
@pages.route("/projects")
def projectspage():
  return render_template("projects.html")
pages.route("/workflow")
def workflowpage():
  return render_template("workflow.html")
