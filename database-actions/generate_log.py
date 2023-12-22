from datetime import datetime
import sqlalchemy
from sqlalchemy import text
import environ

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def generate_log(table_name,log_message, object_name):
    # Define value
    server_name = env('SERVER_NAME')
    database_name = env('DATABASE_NAME')
    current_timestamp = datetime.utcnow()

    # Create engine
    engine = sqlalchemy.create_engine('mssql+pyodbc://'+server_name+'/'+database_name+'?driver=ODBC+Driver+17+for+SQL+Server')
  
    # Execute merge statement
    sql_query = text(f'''
        INSERT INTO [{database_name}].[{table_name}]
        ( -- Columns to insert data into
        [LOG_DT]
        ,[LOG_MESSAGE]
        ,[OBJECT_NAME]
        )
        VALUES
        ( -- First row: values for the columns in the list above
        '{current_timestamp}', 
        '{log_message}', 
        '{object_name}'
        )
        '''
    )

    # Execute a raw SQL statement
    with engine.begin() as conn:
        conn.execute(sql_query)