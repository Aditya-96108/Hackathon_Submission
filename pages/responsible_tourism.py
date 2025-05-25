import streamlit as st
import pandas as pd
import plotly.express as px
from data_processing import load_and_clean
from visualizations import plot_monthly_spending

def show_responsible_tourism():
    with open("static/css/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown('<h1 class="header">Responsible Tourism in India</h1>', unsafe_allow_html=True)

    # Load datasets
    monument_df = load_and_clean("India-Tourism-Statistics-2021-monuments.csv")
    ffe_df = load_and_clean("Month Wise FFE Dollar.csv")

    # Guidelines
    st.markdown('<h2 class="card">Guidelines for Sustainable Travel</h2>', unsafe_allow_html=True)
    guidelines = [
        "Respect local customs, especially in tribal areas like Nagaland and Mizoram.",
        "Choose eco-friendly accommodations, such as homestays in Lakshadweep.",
        "Visit during off-peak seasons (Apr-Jun) to reduce overcrowding at sites like the Taj Mahal.",
        "Support local artisans by purchasing authentic crafts (e.g., Naga shawls, Odishan Pattachitra).",
        "Minimize environmental impact by avoiding single-use plastics."
    ]
    for guideline in guidelines:
        st.markdown(f"- {guideline}")

    # Data Insight
    st.markdown('<h2 class="card">Data-Driven Insights</h2>', unsafe_allow_html=True)
    top_monument = monument_df.nlargest(1, "Domestic-2019-20")[["Name of the Monument", "Domestic-2019-20"]].iloc[0]
    low_monument = monument_df.nsmallest(1, "Domestic-2019-20")[["Name of the Monument", "Domestic-2019-20"]].iloc[0]
    st.write(f"**Insight**: {top_monument['Name of the Monument']} saw {top_monument['Domestic-2019-20']:,} domestic visitors in 2019-20, while {low_monument['Name of the Monument']} had only {low_monument['Domestic-2019-20']:,}. Promoting undervisited sites can reduce overcrowding.")

    # Seasonal Spending
    st.markdown('<h2 class="card">Seasonal Spending Patterns (2019)</h2>', unsafe_allow_html=True)
    st.plotly_chart(plot_monthly_spending(ffe_df))
    st.write("**Insight**: High spending in December ($3.18B) indicates peak season pressure. Off-season travel (Apr-Jun) can support sustainable tourism.")