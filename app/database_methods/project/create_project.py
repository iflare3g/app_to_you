from app.config.utilities import *


def create_project(title):
    connection_to_db = connect()
    query = "insert into progetto(titolo) values (%s)"
    response = safety_insert_query(connection_to_db, query, title)
    if response:
        return response
    else:
        return "Something went wrong..."
