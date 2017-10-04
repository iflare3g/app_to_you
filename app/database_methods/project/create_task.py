from app.config.utilities import *

def create_task(name,project):
  connection_to_db = connect()
  connection_to_get_query = connect()
  get_id_proj = "select id from progetto where titolo=%s;"
  id_proj = safety_get_query(connection_to_get_query,get_id_proj,args=[project])
  id_real_of_proj = id_proj[0]['id']
  query = "insert into task(nome,id_progetto) values(%s,%s);"
  data_to_be_inserted = [name,id_real_of_proj]
  task = safety_insert_query(connection_to_db,query,data_to_be_inserted)
  return task