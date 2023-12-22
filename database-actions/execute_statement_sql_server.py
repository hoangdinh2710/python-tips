import environ
import sqlalchemy
from sqlalchemy import text
import pandas as pd

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def execute_query():
    # Define value
    server_name = env('SERVER_NAME')
    database_name = env('DATABASE_NAME')

    # Create engine for sql server
    engine = sqlalchemy.create_engine('mssql+pyodbc://'+server_name+'/'+database_name+'?driver=ODBC+Driver+17+for+SQL+Server')
  
    # Execute merge statement
    sql_query = text('''
        SELECT * FROM TABLE A
        )
        ''')

    # Execute a raw SQL statement (other than select statement)
    with engine.begin() as conn:
        conn.execute(sql_query)

    # Execute select statement and save to Pandas dataframe
    df = pd.read_sql(sql_query,engine)

