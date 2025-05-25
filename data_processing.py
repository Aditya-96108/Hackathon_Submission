import pandas as pd
import streamlit as st
from snowflake_connect import load_data

def load_and_clean(file_name, table_name=None):
    if table_name is None:
        table_name = file_name.replace('.csv', '').replace(' ', '_').upper()
    df = load_data(table_name, f"data/{file_name}")
    
    # Clean data
    df = df.dropna(how='all')
    df = df.fillna(0)
    
    # Convert numeric columns
    for col in df.columns:
        if col not in ['Country of Nationality', 'year', 'top1_state', 'top2_state', 'top3_state', 
                      'top4_state', 'top5_state', 'top6_state', 'top7_state', 'top8_state', 
                      'top9_state', 'top10_state', 'top1_country', 'top2_country', 'top3_country', 
                      'top4_country', 'top5_country', 'top6_country', 'top7_country', 'top8_country', 
                      'top9_country', 'top10_country']:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            except:
                pass
    
    return df