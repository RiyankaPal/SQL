import streamlit as st
import sqlite3
import pandas as pd
import json
import os

st.set_page_config(page_title="SQL Demo App", layout="centered")

st.title("🧠 SQL Query Demo App")
st.write("Explore SQL queries on a sample database interactively!")

# Get absolute path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to queries.json
queries_path = os.path.join(BASE_DIR, 'queries', 'queries.json')

# Load queries
with open(queries_path, 'r') as f:
    queries = json.load(f)

# Path to SQLite DB
db_path = os.path.join(BASE_DIR, 'data', 'sample.db')

# Connect to DB
conn = sqlite3.connect(db_path)

# Dropdown to choose query
query_name = st.selectbox("Select a query to run:", list(queries.keys()))

# Handle parameterized query
if "?" in queries[query_name]:
    value = st.number_input("Enter salary threshold:", min_value=0, value=60000)
    sql = queries[query_name]
    params = (value,)
else:
    sql = queries[query_name]
    params = ()

# Show SQL text
with st.expander("Show SQL"):
    st.code(sql, language="sql")

# Button to execute
if st.button("Run Query"):
    try:
        df = pd.read_sql_query(sql, conn, params=params)
        st.success("✅ Query executed successfully!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Error: {e}")

conn.close()
