from flask import Flask, jsonify, render_template, url_for, request, session, redirect, abort
from app import app
from app.database_methods.project.list_tasks import *
from app.config.utilities import *


def list_tasks(proj):
    if request.method == "GET":
        response = list_tsk(proj)
        results = []
        if response is not None:
            for item in response:
                results.append(item['nome'])
            return render_template("tasks.html", results=results)
        else:
            return "Something went wrong, check your logs..."

