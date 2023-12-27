import environ
import sqlalchemy
from sqlalchemy import text
import pandas as pd

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def select_query():
    """
    Run a select statement in MSSQL and return as dataframe
    """
    # Define value
    server_name = env('SERVER_NAME')
    database_name = env('DATABASE_NAME')

    # Create engine for sql server
    engine = sqlalchemy.create_engine('mssql+pyodbc://'+server_name+'/'+database_name+'?driver=ODBC+Driver+17+for+SQL+Server')
  
    # Execute merge statement
    sql_query = text('''
        SELECT STATEMENT
        )
        ''')

     # Execute query and save to Pandas dataframe
    df = pd.read_sql(sql_query,engine)

    return df
