import streamlit as st
from pages.dashboard import show_dashboard
from pages.cultural_hotspots import show_cultural_hotspots
from pages.underexplored import show_underexplored
from pages.responsible_tourism import show_responsible_tourism
from pages.recommendations import show_recommendations

st.set_page_config(page_title="Cultural Odyssey India", layout="wide")

# Sidebar navigation
st.sidebar.title("Cultural Odyssey India")
page = st.sidebar.radio("Navigate", [
    "Dashboard",
    "Cultural Hotspots",
    "Underexplored Gems",
    "Responsible Tourism",
    "Personalized Recommendations"
])

# Display selected page
if page == "Dashboard":
    show_dashboard()
elif page == "Cultural Hotspots":
    show_cultural_hotspots()
elif page == "Underexplored Gems":
    show_underexplored()
elif page == "Responsible Tourism":
    show_responsible_tourism()
elif page == "Personalized Recommendations":
    show_recommendations()