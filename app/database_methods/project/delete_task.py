from app.config.utilities import *

def delete_tsk(nome):
  connection_to_db = connect()
  connection_to_get_id = connect()
  get_id_query = "select id from task where nome=%s;"
  id_task_tmp = safety_get_query(connection_to_get_id,get_id_query,args=[nome])
  if id_task_tmp:
    id_task = id_task_tmp[0]["id"]
    query = "delete from task where nome=%s and id=%s;"
    deleted = safety_delete_query(connection_to_db,query,[nome,id_task])
    return deleted
  else:
    print("problem on getting id...")