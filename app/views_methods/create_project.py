from flask import Flask,jsonify,render_template,url_for,request,session,redirect,abort
from app import app
from app.database_methods.project.create_project import *
from app.config.utilities import *

def create_proj(title):
  if request.method == "GET":
    response = create_project(title)
    if response:
      return "<h1>Congratulations! You have created a project called: </h1>" + str(title)
    else:
      return "Something went wrong, check your logs..."
    
