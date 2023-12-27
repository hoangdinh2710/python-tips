import environ
import sqlalchemy
from sqlalchemy import text
import pandas as pd
import oracledb
from sqlalchemy import create_engine

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def select_query():
    """
    Run a select statement in Oracle and return as dataframe
    """
    # Get oracle client for thick connection
    oracledb.init_oracle_client()

    # Define parameter
    host = env('HOST')
    port = env('PORT')
    service_name = env('SERVICE_NAME')
    db_username = env('DB_USERNAME')
    db_password = env('DB_PASSWORD')

    # Authenticate using service name, username and password
    engine = create_engine(
        f'oracle+oracledb://{db_username}:{db_password}@{host}:{port}/?service_name={service_name}')

    # Define SQL Query
    sql_query = text('''
        SELECT * FROM TABLE A
    ''')

    # Execute query and save to Pandas dataframe
    df = pd.read_sql(sql_query,engine)

    return df