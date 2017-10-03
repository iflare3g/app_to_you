from flask import Flask,jsonify,render_template,url_for,request,session,redirect,abort
from app import app
from app.database_methods.project.delete_task import *
from app.config.utilities import *

def delete_task(nome):
  if request.method == "GET":
    response = delete_tsk(nome)
    if response is not None:
      return "Deleted " + str(nome)
    else:
      return "Something went wrong, check your logs..."
    
