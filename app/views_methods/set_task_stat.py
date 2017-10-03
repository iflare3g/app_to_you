from app import app
from app.database_methods.project.set_task_status import *
from app.config.utilities import *

def set_task_status(task,status):
    ALLOWED_STATUS = ("true","false")
    if status in ALLOWED_STATUS:
        if status == "true":
            status = 0
        else:
            status = 1
        response = set_tsk_status(task,status)
        return response
    else:
        return "status not allowed!"