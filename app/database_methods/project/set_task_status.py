from app.config.utilities import *

def set_tsk_status(task,status):
    connection = connect()
    query = "update task set task.status=%s where task.nome = %s"
    set_status = safety_update_query(connection,query,[status,task])
    if set_status:
        return set_status