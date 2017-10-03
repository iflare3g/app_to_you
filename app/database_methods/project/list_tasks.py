from app.config.utilities import *
import pymysql as mysql

def list_tsk(nome_proj):
  connection_to_db = connect()
  query = "select task.nome from progetto,task where progetto.id = task.id_progetto and progetto.titolo=%s;"
  all_tasks = safety_get_query(connection_to_db,query,args=nome_proj)
  print(all_tasks)
  if all_tasks:
      return all_tasks
