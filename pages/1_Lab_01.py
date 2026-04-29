import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np

# Page Config
st.set_page_config(page_title="Seismic-Lab-Showcase | Module 01", layout="wide")

# Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #050505; color: white !important; }
    .stApp { background: radial-gradient(circle at top right, #1e3d59, #050505), #050505; }
    h1, h2, h3, p, span, div, li { color: white !important; }
    .glass-card { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 15px; padding: 25px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Relative Paths for Deployment
CSV_PATH = "data/earthquakes.csv"
GRAPH_PATH = "graphs/correlation_heatmap.png"

st.title("🏗️ Module 01: Data Engineering")
st.write("Exploration of the seismic pipeline foundations.")

tab1, tab2 = st.tabs(["📊 Analytics Lab", "⚙️ Engineering Details"])

with tab1:
    st.markdown('<div class="glass-card"><h3>Live Correlation Engine</h3>', unsafe_allow_html=True)
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        numeric_df = df.select_dtypes(include=[np.number])
        fig = px.imshow(numeric_df.corr(), text_auto=True, color_continuous_scale='RdBu_r')
        fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    if os.path.exists(GRAPH_PATH):
        st.image(GRAPH_PATH, caption="Static Feature Analysis")

with tab2:
    st.markdown("""
    <div class="glass-card">
    <h3>Technical Implementation</h3>
    <ul>
        <li><b>Multi-Format ETL:</b> Integrated JSON, XML, and HTML streams.</li>
        <li><b>Hybrid DB:</b> Implemented SQLite3 and MongoDB Atlas.</li>
        <li><b>Vectorization:</b> Achieved high performance using NumPy SIMD.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.code("""
# Vectorized Slicing Logic
magnitude = df['mag'].to_numpy()
mask = (df['depth'] > 100) & (magnitude > 5.0)
    """, language="python")

if st.button("← Back to Launchpad"):
    st.switch_page("app.py")
