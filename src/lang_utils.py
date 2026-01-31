import os
import random
import pandas as pd
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_random_key():
    keys_string = os.getenv("GOOGLE_API_KEYS")
    if not keys_string:
        keys_string = os.getenv("GOOGLE_API_KEY")
    if not keys_string:
         raise ValueError("No keys found in .env file!")
    return random.choice(keys_string.split(",")).strip()

def get_sql_agent(db_uri):
    return DirectSQLChain(db_uri)

class DirectSQLChain:
    def __init__(self, db_uri):
        self.db_uri = db_uri
        self.db = SQLDatabase.from_uri(db_uri)
        # We need the engine to run pandas queries
        self.engine = self.db._engine 
        
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-flash-latest", 
            google_api_key=get_random_key(),
            temperature=0
        )

    def invoke(self, user_query):
        table_info = self.db.get_table_info()
        
        prompt = f"""
        You are an expert SQL Data Analyst.
        Given the following database schema:
        {table_info}
        
        Write a SQL query to answer this question: "{user_query}"
        
        IMPORTANT RULES:
        1. Return ONLY the SQL code. No markdown, no explanation.
        2. Do not start with ```sql. Just the raw query.
        """
        
        try:
            print(f"DEBUG: Sending request to Google...")
            response = self.llm.invoke(prompt)
            
            # Clean the SQL
            sql_query = response.content.strip().replace("```sql", "").replace("```", "").strip()
            print(f"DEBUG: Generated SQL -> {sql_query}")
            
            # --- THE FORMATTING UPGRADE ---
            # Instead of db.run(), we use Pandas to get a clean DataFrame
            df_result = pd.read_sql(sql_query, self.engine)
            
            return {"result": df_result, "sql": sql_query}

        except Exception as e:
            return {"error": str(e)}