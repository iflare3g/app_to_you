from flask import Flask,jsonify,render_template,url_for,request,session,redirect,abort
from app import app
from app.database_methods.project.create_task import *
from app.config.utilities import *

def create_tsk(name,project):
  if request.method == "GET":
    response = create_task(name,project)
    if response:
      return jsonify({'result':"'+"+str(response)+"'"})
    else:
      return jsonify("{'result':'Something went wrong, check your logs...'}")
  else:
    abort(403)
    
