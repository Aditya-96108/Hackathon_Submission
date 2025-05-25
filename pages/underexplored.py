import streamlit as st
import pandas as pd
import plotly.express as px
from visualizations import plot_state_map, plot_travel_modes
from data_processing import load_and_clean

def show_underexplored():
    with open("static/css/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown('<h1 class="header">Underexplored Cultural Gems</h1>', unsafe_allow_html=True)

    # Load datasets
    state_df = load_and_clean("India-Tourism-Statistics-statewise_2019-2020_domestic_foreign.csv")
    monument_df = load_and_clean("India-Tourism-Statistics-2021-monuments.csv")
    travel_modes_df = load_and_clean("Country Wise Visitors Ways.csv")

    # Underexplored States
    st.markdown('<h2 class="card">Underexplored States (2019)</h2>', unsafe_allow_html=True)
    underexplored_states = state_df.nsmallest(5, "Domestic -2019")[["States/UTs", "Domestic -2019", "Foreign - 2019"]]
    st.dataframe(underexplored_states)

    # Cultural Highlights
    cultural_highlights = {
        "Lakshadweep": "Lava and Kolkali dances, marine culture",
        "Mizoram": "Cheraw dance, Chapchar Kut festival",
        "Nagaland": "Hornbill Festival, Naga tribal art",
        "Arunachal Pradesh": "Monpa and Apatani crafts, Buddhist monasteries",
        "Manipur": "Manipuri dance, Ras Leela"
    }
    st.markdown('<h2 class="card">Cultural Highlights</h2>', unsafe_allow_html=True)
    st.json(cultural_highlights)

    # Underexplored Monuments
    st.markdown('<h2 class="card">Underexplored Monuments (2019-20)</h2>', unsafe_allow_html=True)
    underexplored_monuments = monument_df.nsmallest(5, "Domestic-2019-20")[["Name of the Monument", "Domestic-2019-20", "Foreign-2019-20"]]
    st.dataframe(underexplored_monuments)

    # Map of Underexplored States
    st.markdown('<h2 class="card">Map of Underexplored Regions</h2>', unsafe_allow_html=True)
    underexplored_map = state_df[state_df["States/UTs"].isin(underexplored_states["States/UTs"])]
    st.plotly_chart(plot_state_map(underexplored_map))

    # Travel Mode Challenges
    st.markdown('<h2 class="card">Travel Mode Challenges (2019)</h2>', unsafe_allow_html=True)
    country = st.selectbox("Select Country for Travel Mode Analysis", travel_modes_df['Country of Nationality'].unique())
    st.plotly_chart(plot_travel_modes(travel_modes_df, country))
    st.write("**Insight**: Countries like Nepal (10.2% land travel) face accessibility challenges to underexplored regions due to reliance on land routes, suggesting a need for better air connectivity.")