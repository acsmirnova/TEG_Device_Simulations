#test app file
import streamlit as st
import numpy as np
import matplotlib
import pandas as pd
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="TEG Analysis Project",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .section-header {
        color: #F4A100;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("Images/Sans-titre-01.webp", width=200)
st.sidebar.title("Navigation")

# Main sections
st.sidebar.markdown("### Project Overview")
st.sidebar.markdown("""
- [Introduction](#introduction)
- [Team](#team)
- [Materials](#materials)
- [Analysis](#analysis)
- [Results](#results)
""")

# Main content
st.title('Thermoelectric Generator (TEG) Analysis Project')
st.markdown('<p class="section-header">Welcome to our Project!</p>', unsafe_allow_html=True)

# Project overview
st.markdown("""
<div style="background-color: #f0f2f6; color: #222; padding: 1.5rem; border-radius: 0.7rem; margin-bottom: 2rem;">
    <h2 style="margin-bottom: 0.5rem; color: #222;">Project Overview</h2>
    <div style="font-size: 1.1rem; color: #222;">
        This project explores the optimization of thermoelectric energy harvesting devices through:
        <ul>
            <li>Theoretical calculations and analysis</li>
            <li>COMSOL simulations</li>
            <li>Machine learning-based optimization</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick links
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 📊 Analysis")
    st.markdown("[View COMSOL Simulations](COMSOL)")
    st.markdown("[View Neural Network Analysis](Neural_Network)")

with col2:
    st.markdown("### 🔬 Materials")
    st.markdown("[PbTe Material Analysis](PbTe_Material)")
    st.markdown("[TEG Module Design](TEG_Module)")

with col3:
    st.markdown("### 📈 Results")
    st.markdown("[Maximum Power Analysis](Maximum_Power_Efficient_Module)")
    st.markdown("[Simulation Results](5000_COMSOL_Simulations)")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>FAMEAIS EnergAI project 2024: Group 2</p>
    <p>Use the sidebar to navigate between different sections.</p>
</div>
""", unsafe_allow_html=True)
