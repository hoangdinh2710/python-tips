import environ
import sqlalchemy

# Get environment variables
env = environ.Env()
environ.Env.read_env()

def load_to_sql_server(df,database_name,schema_name,table_name,load_type):
    """
    Load Pandas dataframe to a table in mssql

    Load Type: 
    - fail: Raise a ValueError.

    - replace: Drop the table before inserting new values.

    - append: Insert new values to the existing table.
    """
    # Get environment variables
    env = environ.Env()
    environ.Env.read_env()
    # Define value
    server_name = env('server_name')

    # Create engine for sql server
    engine = sqlalchemy.create_engine('mssql+pyodbc://'+server_name+'/'+database_name+'?driver=ODBC+Driver+17+for+SQL+Server')
    # Create connection
    connection = engine.connect()

    # Write the DataFrame to the database
    df.to_sql(schema=schema_name,name=table_name, con=connection, if_exists=load_type, index=False)

    # Close the connection
    connection.close()