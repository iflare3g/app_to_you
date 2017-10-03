from flask import Flask,jsonify,render_template,url_for,request,session,redirect,abort
from app import app
from app.database_methods.project.list_project import *
from app.config.utilities import *

def list_proj():
  if request.method == "GET":
    response = list_project()
    results = []
    if response is not None:
      for item in response:
        results.append(item['titolo'])
      return render_template("projects.html",results=results)
    else:
      return "Something went wrong, check your logs..."
    
