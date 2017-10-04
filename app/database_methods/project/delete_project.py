from app.config.utilities import *
import pymysql as mysql

def delete_project(title):
  connection_to_db = connect()
  query = "delete from progetto where titolo=%s"
  response = safety_delete_query(connection_to_db,query,title)
  if response:
      return response
  else:
      return "Something went wrong..."
