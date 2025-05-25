import streamlit as st
import snowflake.connector
from snowflake.connector import DictCursor
from dotenv import load_dotenv
import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_snowflake_connection():
    load_dotenv()
    user = os.getenv('SNOWFLAKE_USER')
    password = os.getenv('SNOWFLAKE_PASSWORD')
    account = os.getenv('SNOWFLAKE_ACCOUNT')
    warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')

    if not all([user, password, account, warehouse]):
        logger.warning("Missing Snowflake credentials in .env file")
        return None

    try:
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database='TOURISM_STATISTICS',
            schema='PUBLIC'
        )
        return conn
    except Exception as e:
        logger.error(f"Snowflake connection failed: {e}")
        # Display error only once per session
        if 'snowflake_error_shown' not in st.session_state:
            st.session_state['snowflake_error_shown'] = True
            st.error("Failed to connect to Snowflake. Using local CSV files.")
        return None

def query_snowflake(query):
    conn = get_snowflake_connection()
    if conn:
        try:
            cursor = conn.cursor(DictCursor)
            cursor.execute(query)
            results = cursor.fetchall()
            df = pd.DataFrame(results)
            cursor.close()
            conn.close()
            return df
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return None
    return None

def load_data(table_name, csv_path):
    df = query_snowflake(f"SELECT * FROM {table_name}")
    if df is not None and not df.empty:
        return df
    else:
        try:
            logger.info(f"Loading {csv_path} from local storage")
            st.warning(f"Loading {csv_path} from local storage")
            return pd.read_csv(csv_path)
        except FileNotFoundError:
            logger.error(f"CSV file not found: {csv_path}")
            st.error(f"CSV file not found: {csv_path}")
            return pd.DataFrame()