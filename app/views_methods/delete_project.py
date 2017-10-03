from flask import Flask,jsonify,render_template,url_for,request,session,redirect,abort
from app import app
from app.database_methods.project.delete_project import *
from app.config.utilities import *

def delete_proj(title):
  if request.method == "GET":
    response = delete_project(title)
    if response:
      return "<h1>Congratulations! You have deleted a project called: </h1>" + str(title)
    else:
      return "Something went wrong, check your logs..."
    
