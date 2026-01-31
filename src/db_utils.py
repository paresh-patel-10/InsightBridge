import sqlite3
import pandas as pd
from sqlalchemy import create_engine, text

def dataframe_to_database(uploaded_file, table_name):
    """
    Reads a CSV file and converts it to a local SQLite database.
    """
    # Read the CSV
    df = pd.read_csv(uploaded_file)
    
    # Create a lightweight database engine
    engine = create_engine("sqlite:///my_data.db")
    
    # Write data to SQL table
    df.to_sql(table_name, engine, index=False, if_exists='replace')
    
    return engine, df

def execute_sql_query(query, engine):
    """
    Helper to execute raw SQL (if needed for debugging).
    """
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()