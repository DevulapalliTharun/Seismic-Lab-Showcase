import streamlit as st
import pandas as pd
import os
import pydeck as pdk

# Page Config
st.set_page_config(page_title="SeismicOS | Module MR", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #050505; color: white !important; }
    .stApp { background: radial-gradient(circle at top right, #1e3d59, #050505), #050505; }
    h1, h2, h3, p, span, div, li { color: white !important; }
    .glass-card { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 15px; padding: 25px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Relative Paths
CSV_PATH = "data/earthquakes.csv"
CHART_PATH = "charts/top10_by_earthquake_count.png"

st.title("🌩️ Module MR: Big Data Analysis")
st.write("Distributed MapReduce pipeline for global hazard assessment.")

st.markdown('<div class="glass-card"><h3>Global Hazard Risk Index</h3>', unsafe_allow_html=True)
data = {
    "Rank": [1, 2, 3, 4, 5],
    "Region": ["Russia", "Alaska", "Japan", "Indonesia", "Philippines"],
    "Risk Index": [0.803, 0.548, 0.255, 0.254, 0.221]
}
st.table(pd.DataFrame(data))
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)
with col1:
    if os.path.exists(CHART_PATH):
        st.image(CHART_PATH, use_container_width=True)
with col2:
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        st.pydeck_chart(pdk.Deck(
            layers=[pdk.Layer("HexagonLayer", data=df, get_position="[longitude, latitude]", radius=100000, extruded=True)],
            initial_view_state=pdk.ViewState(latitude=0, longitude=0, zoom=1, pitch=45),
            map_style="mapbox://styles/mapbox/dark-v9",
        ))

if st.button("← Back to Launchpad"):
    st.switch_page("app.py")
