from django.db import connection

def execute_query(query, params=None):
    """
    Executes a raw SQL query and returns the results.
    """
    with connection.cursor() as cursor:
        cursor.execute(query, params or [])
        return cursor.fetchall()