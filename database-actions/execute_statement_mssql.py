import environ
import sqlalchemy
from sqlalchemy import text
import pandas as pd

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def execute_query():
    """
    Execute a SQL query in MS SQL
    """
    # Define value
    server_name = env('SERVER_NAME')
    database_name = env('DATABASE_NAME')

    # Create engine for sql server
    engine = sqlalchemy.create_engine('mssql+pyodbc://'+server_name+'/'+database_name+'?driver=ODBC+Driver+17+for+SQL+Server')
  
    # Execute merge statement
    sql_query = text('''
        STATEMENT
        )
        ''')

    # Execute a raw SQL statement (other than select statement)
    with engine.begin() as conn:
        conn.execute(sql_query)

