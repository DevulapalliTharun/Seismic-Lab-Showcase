import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SeismicOS | Intelligence Portal",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- TRENDING UI / GLASSMORPHISM STYLING ---
def apply_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #050505;
        }

        .stApp {
            background: radial-gradient(circle at top right, #1e3d59, #050505),
                        radial-gradient(circle at bottom left, #111, #050505);
            color: white !important;
        }

        h1, h2, h3, p, span, div, li { color: white !important; }
        
        .hero-container {
            padding: 100px 20px;
            text-align: center;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 50px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }

        .hero-title {
            font-size: 5rem;
            font-weight: 800;
            letter-spacing: -2px;
            background: linear-gradient(to right, #fff, #666);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0px;
        }

        .lab-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 40px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            height: 350px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .lab-card:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: scale(1.02);
            border-color: #ff6e40;
        }

        .telemetry {
            display: inline-block;
            padding: 6px 15px;
            background: rgba(0, 255, 127, 0.1);
            color: #00ff7f !important;
            border: 1px solid rgba(0, 255, 127, 0.2);
            border-radius: 50px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .muted { color: #888 !important; font-size: 1.1rem; }
        
        [data-testid="stSidebar"] {
            background-color: rgba(0,0,0,0.8) !important;
            backdrop-filter: blur(10px);
        }
        
        .stButton button {
            background: rgba(255,255,255,0.1) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            border-radius: 10px !important;
        }
        .stButton button:hover {
            border-color: #ff6e40 !important;
            background: rgba(255, 110, 64, 0.1) !important;
        }
        </style>
        """, unsafe_allow_html=True)

apply_style()

# --- HERO SECTION ---
st.markdown("""
    <div class="hero-container">
        <div class="telemetry">● System Telemetry: 17,959 Live Nodes</div>
        <h1 class="hero-title">SeismicOS</h1>
        <p class="muted">Next-Gen Earthquake Intelligence & Risk Modeling Portal</p>
        <div style="margin-top: 30px;">
            <span style="color: #888;">Built by</span> <b>Devulapalli Tharun</b> 
            <span style="color: #444; margin: 0 15px;">|</span> 
            <span style="color: #888;">Verified for</span> <b>NITK Submission</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; margin-bottom: 40px;'>Mission Modules</h3>", unsafe_allow_html=True)

# Helper function to switch pages robustly
def go_to(page_name):
    try:
        st.switch_page(page_name)
    except Exception as e:
        st.error(f"Navigation Error: {e}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="lab-card"><div style="font-size: 4rem;">🏗️</div><h2>Data Engine</h2><p class="muted">Lab 01: Engineering Foundations</p></div>""", unsafe_allow_html=True)
    if st.button("🚀 Launch Module 01", use_container_width=True):
        go_to("pages/1_Lab_01.py")

with col2:
    st.markdown("""<div class="lab-card"><div style="font-size: 4rem;">🧠</div><h2>Seismic AI</h2><p class="muted">Lab 02: Predictive Intelligence</p></div>""", unsafe_allow_html=True)
    if st.button("🚀 Launch Module 02", use_container_width=True):
        go_to("pages/2_Lab_02.py")

with col3:
    st.markdown("""<div class="lab-card"><div style="font-size: 4rem;">🌩️</div><h2>MapReduce</h2><p class="muted">Big Data Hazard Pipeline</p></div>""", unsafe_allow_html=True)
    if st.button("🚀 Launch Module MR", use_container_width=True):
        go_to("pages/3_MapReduce.py")

st.markdown("""
    <div style="margin-top: 50px; padding: 40px; text-align: center;">
        <p style="color: #666 !important;">© 2026 SeismicOS Engineering | NITK Surathkal</p>
    </div>
    """, unsafe_allow_html=True)
