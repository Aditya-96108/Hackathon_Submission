import streamlit as st
import pandas as pd
import plotly.express as px
from data_processing import load_and_clean
from recommendations import recommend_destinations

def show_recommendations():
    with open("static/css/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown('<h1 class="header">Personalized Travel Recommendations</h1>', unsafe_allow_html=True)

    # Load datasets
    state_df = load_and_clean("India-Tourism-Statistics-statewise_2019-2020_domestic_foreign.csv")
    travel_modes_df = load_and_clean("Country Wise Visitors Ways.csv")

    # User Input Form
    st.markdown('<h2 class="card">Tell Us Your Preferences</h2>', unsafe_allow_html=True)
    with st.form("recommendation_form"):
        art_form = st.selectbox("Preferred Art Form/Cultural Experience", ["Tribal", "Mughal", "Temple Architecture", "Dance", "Festivals"])
        season = st.selectbox("Preferred Season", ["Jan-Mar", "Apr-Jun", "Jul-Sep", "Oct-Dec"])
        crowd = st.selectbox("Crowd Preference", ["Low", "Moderate", "High"])
        travel_mode = st.selectbox("Preferred Travel Mode", ["Air", "Sea", "Land"])
        submit = st.form_submit_button("Get Recommendations")

    if submit:
        preferences = {"art_form": art_form, "season": season, "crowd": crowd, "travel_mode": travel_mode}
        recommendations = recommend_destinations(preferences, state_df, travel_modes_df)
        st.markdown('<h2 class="card">Recommended Destinations</h2>', unsafe_allow_html=True)
        if recommendations:
            for dest in recommendations:
                st.markdown(f"- {dest}")
        else:
            st.write("No destinations match your preferences. Try adjusting your selections.")
        st.write("**Insight**: Recommendations prioritize low-crowd, culturally rich destinations accessible via your preferred travel mode, supporting sustainable tourism.")