import environ
from sqlalchemy import text
import oracledb
from sqlalchemy import create_engine

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def execute_query():
    """
    Execute a SQL query in Oracle db
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
    sql_query = text(f'''
        STATEMENT
    ''')

    # Execute a raw SQL statement (other than select statement)
    with engine.begin() as conn:
        conn.execute(sql_query)