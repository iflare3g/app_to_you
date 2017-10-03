from flask import Flask,jsonify,render_template,url_for,request,session,redirect
from app import app
from app.config.utilities import *
from app.views_methods.create_project import *
from app.views_methods.delete_project import *
from app.views_methods.list_project import *
from app.views_methods.list_tasks import *
from app.views_methods.create_task import *
from app.views_methods.delete_task import *
from app.views_methods.set_task_stat import *


@app.route('/list/projects',methods = ['GET'])
def list_projects():
  return list_proj()
  
@app.route('/create/<title>',methods = ['GET','POST'])
def create(title):
  return create_proj(title)

@app.route('/delete/<title>',methods = ['GET'])
def delete(title):
  return delete_proj(title)
  
@app.route('/create/task/<title>/<project>',methods = ['GET'])
def create_tsk(title,project):
  return create_task(title,project)
  
@app.route('/delete/task/<title>',methods = ['GET'])
def delete_tsk(title):
  return delete_task(title)
  
@app.route('/list/tasks/<project>',methods = ['GET'])
def ls_tasks(project):
  return list_tasks(project)

@app.route('/status/<task>/<status>', methods = ['GET'])
def set_tsk_status(task,status):
  return set_task_status(task,status)