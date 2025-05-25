import streamlit as st
import pandas as pd
import plotly.express as px
from visualizations import plot_state_map, plot_travel_modes
from data_processing import load_and_clean

def show_cultural_hotspots():
    with open("static/css/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown('<h1 class="header">Cultural Hotspots in India</h1>', unsafe_allow_html=True)

    # Load datasets
    monument_df = load_and_clean("India-Tourism-Statistics-2021-monuments.csv")
    state_df = load_and_clean("India-Tourism-Statistics-statewise_2019-2020_domestic_foreign.csv")
    travel_modes_df = load_and_clean("Country Wise Visitors Ways.csv")

    # Top 5 Monuments
    st.markdown('<h2 class="card">Top Monuments by Visitors (2019-20)</h2>', unsafe_allow_html=True)
    top_monuments = monument_df.nlargest(5, "Domestic-2019-20")[["Name of the Monument", "Domestic-2019-20", "Foreign-2019-20"]]
    st.dataframe(top_monuments)

    # Art Forms
    art_forms = {
        "Taj Mahal": "Mughal Architecture, Pietra Dura",
        "Red Fort": "Mughal Architecture, Persian Inscriptions",
        "Qutub Minar": "Indo-Islamic Architecture",
        "Sun Temple, Konark": "Odishan Temple Architecture, Kalinga Art",
        "Ellora Caves": "Rock-cut Architecture, Buddhist and Jain Art"
    }
    st.markdown('<h2 class="card">Associated Art Forms</h2>', unsafe_allow_html=True)
    st.json(art_forms)

    # State-wise Map
    st.markdown('<h2 class="card">Tourism by State (2019)</h2>', unsafe_allow_html=True)
    st.plotly_chart(plot_state_map(state_df))

    # Travel Modes for Cultural Tourists
    st.markdown('<h2 class="card">How Tourists Reach Cultural Hotspots (2019)</h2>', unsafe_allow_html=True)
    country = st.selectbox("Select Country for Travel Mode", travel_modes_df['Country of Nationality'].unique())
    st.plotly_chart(plot_travel_modes(travel_modes_df, country))
    st.write("**Insight**: Most tourists (e.g., 98.97% from the USA) arrive by air, indicating strong international connectivity to cultural hotspots like the Taj Mahal.")