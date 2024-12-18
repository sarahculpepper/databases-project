from .sql_queries import *

def create_reporter_editor(username, id, role):
    name = username
    user_id = id
    role = role
    query = ""

    if (role == "reporter"):
        query = """
            INSERT INTO REPORTER (Name, UserID)
            VALUES (%s, %s)
        """
    if (role == "editor"):
        query = """
            INSERT INTO EDITOR (Name, UserID)
            VALUES (%s, %s)
        """
    # Execute the query
    with connection.cursor() as cursor:
        cursor.execute(query, [
            name, user_id
        ])
