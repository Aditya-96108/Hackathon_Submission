import streamlit as st
import pandas as pd
import plotly.express as px
from visualizations import plot_state_map, plot_travel_modes, plot_monthly_spending
from data_processing import load_and_clean

def show_dashboard():
    with open("static/css/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="header">India Tourism Dashboard</h1>', unsafe_allow_html=True)

    # Load datasets
    fta_df = load_and_clean("General Data 2014-2020.csv")
    state_df = load_and_clean("Top 10 State Visit.csv")
    travel_modes_df = load_and_clean("Country Wise Visitors Ways.csv")
    ffe_df = load_and_clean("Month Wise FFE Dollar.csv")

    # FTA Trend
    st.markdown('<h2 class="card">Foreign Tourist Arrivals (2014-2020)</h2>', unsafe_allow_html=True)
    fig = px.line(fta_df, x='year', y='noftaii', title='FTA Trend (Millions)')
    st.plotly_chart(fig)
    st.write("**Insight**: FTAs peaked at 10.93M in 2019 but dropped by 74.9% in 2020 due to the pandemic.")

    # Top States
    st.markdown('<h2 class="card">Top 5 States by Domestic Visitors (2019)</h2>', unsafe_allow_html=True)
    top_states = state_df[state_df['year'] == 2019][['top1_state', 'top1_ftv', 'top2_state', 'top2_ftv', 
                                                     'top3_state', 'top3_ftv', 'top4_state', 'top4_ftv', 
                                                     'top5_state', 'top5_ftv']]
    st.dataframe(top_states)
    st.plotly_chart(plot_state_map(load_and_clean("India-Tourism-Statistics-statewise_2019-2020_domestic_foreign.csv")))

    # Travel Modes
    st.markdown('<h2 class="card">Travel Modes (2019)</h2>', unsafe_allow_html=True)
    country = st.selectbox("Select Country", travel_modes_df['Country of Nationality'].unique())
    st.plotly_chart(plot_travel_modes(travel_modes_df, country))

    # Monthly Spending
    st.markdown('<h2 class="card">Foreign Exchange Earnings (2019)</h2>', unsafe_allow_html=True)
    st.plotly_chart(plot_monthly_spending(ffe_df))
    st.write("**Insight**: December 2019 had the highest FFE at $3.18B, reflecting peak tourist season.")