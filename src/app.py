import streamlit as st
import pandas as pd
from db_utils import dataframe_to_database
from lang_utils import get_sql_agent

# --- Page Setup ---
st.set_page_config(
    page_title="InsightBridge AI", 
    page_icon="🌉", 
    layout="centered"
)

st.title("🌉 InsightBridge")
st.caption("Bridging the gap between your Data and Answers with AI.")

# --- File Upload Section ---
st.sidebar.header("1. Upload Data")
uploaded_files = st.sidebar.file_uploader(
    "Upload CSV file(s)", 
    type=["csv"], 
    accept_multiple_files=True
)

if uploaded_files:
    # --- Step 1: Process Data ---
    st.sidebar.success(f"{len(uploaded_files)} file(s) uploaded!")
    
    # Load all files into the DB
    engine, preview_data = dataframe_to_database(uploaded_files)
    
    # --- DATA PREVIEW ---
    st.write("### 🔍 Data Preview")
    
    # Create tabs for each table so user can switch views
    tab_names = list(preview_data.keys())
    tabs = st.tabs(tab_names)
    
    for i, table_name in enumerate(tab_names):
        with tabs[i]:
            df = preview_data[table_name]
            st.caption(f"Table Name: **{table_name}**")
            st.table(df.head(5))
            
            if st.checkbox(f"Show Full {table_name}", key=table_name):
                st.dataframe(df, use_container_width=True, height=400)

    # --- Step 2: Chat with Data ---
    st.write("---")
    st.write("### 🤖 Ask Your Data")
    user_query = st.text_input("Type your question here:")

    if user_query:
        with st.spinner("Analyzing across tables..."):
            try:
                # Initialize Agent (It will see ALL tables automatically)
                agent = get_sql_agent("sqlite:///my_data.db")
                
                response = agent.invoke(user_query)
                
                if "error" in response:
                    st.error(f"⚠️ Error: {response['error']}")
                else:
                    result_df = response["result"]
                    sql_query = response["sql"]

                    st.write("### 💡 Answer:")
                    
                    if len(result_df) == 1 and len(result_df.columns) == 1:
                        final_value = result_df.iloc[0, 0]
                        col_name = result_df.columns[0]
                        st.metric(label=col_name, value=str(final_value))
                    elif result_df.empty:
                        st.warning("No data found.")
                    else:
                        st.dataframe(result_df, hide_index=True)

                    with st.expander("See generated SQL"):
                        st.code(sql_query, language="sql")
                
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

else:
    st.info("👈 Please upload at least one CSV file.")