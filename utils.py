import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from PIL import Image

# Cache data loading functions
@st.cache_data
def load_comsol_data():
    """Load COMSOL simulation results."""
    try:
        return pd.read_csv('ANN_dataset/comsol_results_with_efficiency.csv')
    except FileNotFoundError:
        st.error("COMSOL results file not found. Please ensure the file exists in the ANN_dataset directory.")
        return None

@st.cache_data
def load_teg_data():
    """Load TEG parameter data."""
    try:
        return pd.read_csv('ANN_dataset/TEG_data.csv')
    except FileNotFoundError:
        st.error("TEG data file not found. Please ensure the file exists in the ANN_dataset directory.")
        return None

def create_interactive_plot(df, x_col, y_col, title, color_col=None):
    """Create an interactive Plotly plot."""
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        labels={x_col: x_col.replace('_', ' ').title(),
                y_col: y_col.replace('_', ' ').title()},
        template='plotly_white'
    )
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        showlegend=True
    )
    return fig

def format_number(value, decimals=2):
    """Format number with specified decimal places."""
    return f"{value:,.{decimals}f}"

def create_parameter_slider(param_name, min_val, max_val, default_val, step=None):
    """Create a standardized parameter slider."""
    return st.slider(
        param_name,
        min_value=float(min_val),
        max_value=float(max_val),
        value=float(default_val),
        step=float(step) if step else None,
        help=f"Adjust {param_name.lower()} parameter"
    )

def display_metric_card(title, value, unit="", delta=None):
    """Display a metric card with optional delta value."""
    # Use more decimal places for small values
    if abs(value) < 0.01:
        value_str = f"{value:,.6f}{unit}"
    else:
        value_str = f"{value:,.2f}{unit}"
    if delta is not None:
        if abs(delta) < 0.01:
            delta_str = f"{delta:+,.6f}{unit}"
        else:
            delta_str = f"{delta:+,.2f}{unit}"
    else:
        delta_str = None
    st.metric(
        label=title,
        value=value_str,
        delta=delta_str
    )

def load_image(image_path):
    """Load and display an image with error handling."""
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
        return None
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def create_download_button(df, filename, button_text):
    """Create a download button for dataframes."""
    csv = df.to_csv(index=False)
    st.download_button(
        label=button_text,
        data=csv,
        file_name=filename,
        mime='text/csv'
    ) 