from app.config.utilities import *
import pymysql as mysql

def delete_project(title):
  connection_to_db = connect()
  res = None
  msg = ''
  try:
      with connection_to_db.cursor() as cursor: #cursor.close() automatico alla fine del try o except...
          query = "delete from progetto where titolo=%s"
          try:
              cursor.execute(query,(title))
              connection_to_db.commit()
              msg = 'Deleted!'
              print(msg)
          except (mysql.err.IntegrityError,mysql.err.ProgrammingError) as err:
              print('Error! Closing connection...' + str(err))
              error = 'Something went wrong...check your logs...'
              print(error)
  finally:
      if connection_to_db is not None:
        connection_to_db.close()
      else:
          print("Is MySQL Server running ?")
          return "Is MySQL Server running ?"
  return msg