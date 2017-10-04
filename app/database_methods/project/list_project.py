from app.config.utilities import *

def list_project():
  connection_to_db = connect()
  query = "select * from progetto;"
  all_projects = safety_get_query(connection_to_db,query,args=None)
  print(all_projects)
  return all_projects