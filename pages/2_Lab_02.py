import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Page Config
st.set_page_config(page_title="Seismic-Lab-Showcase | Module 02", layout="wide")

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
REG_PATH = "graphs/magnitude_prediction.png"
CLUSTER_PATH = "graphs/earthquake_clusters.png"

st.title("🧠 Module 02: Seismic AI")
st.write("Predictive modeling and geospatial clustering intelligence.")

t1, t2 = st.tabs(["📈 Regression Modeling", "📍 Geospace Clusters"])

with t1:
    st.markdown('<div class="glass-card"><h3>Magnitude Prediction (Supervised)</h3>', unsafe_allow_html=True)
    if os.path.exists(REG_PATH):
        st.image(REG_PATH, use_container_width=True)
    st.write("Ordinary Least Squares (OLS) used for predicting magnitude from depth and coordinates.")
    st.markdown('</div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="glass-card"><h3>Tectonic Clustering (K-Means)</h3>', unsafe_allow_html=True)
    if os.path.exists(CLUSTER_PATH):
        st.image(CLUSTER_PATH, use_container_width=True)
    st.success("K-Means++ successfully partitioned the 17,959 events into the San Andreas, Caribbean, and Kamchatka plate boundaries.")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("← Back to Launchpad"):
    st.switch_page("app.py")
