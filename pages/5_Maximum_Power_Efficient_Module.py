import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import create_interactive_plot, display_metric_card, create_parameter_slider

# Page configuration
st.set_page_config(
    page_title="Maximum Power Analysis - TEG Project",
    page_icon="⚡",
    layout="wide"
)

# Title and introduction
st.title("Maximum Power Analysis")
st.markdown("""
This page analyzes the maximum power efficiency achievable with different material combinations
in thermoelectric generator (TEG) modules.
""")

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs([
    "📊 Material Analysis", 
    "⚡ Power Calculation", 
    "📈 Comparison"
])

with tab1:
    st.header("Material Selection and ZT Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Figure of Merit (ZT)
        The ZT value is a key metric for thermoelectric materials, calculated as:
        """)
        st.latex(r"""
        \overline{ZT} = \frac{(S_p - S_n)^2 \overline{T}}{\left( (\rho_n \kappa_n)^{1/2} + (\rho_p \kappa_p)^{1/2} \right)^2}
        """)
        
        st.markdown("""
        Where:
        - Sp, Sn: Seebeck coefficients of p and n-type materials
        - ρp, ρn: Electrical resistivities
        - κp, κn: Thermal conductivities
        - T: Average temperature
        """)
    
    with col2:
        # Display material properties
        st.markdown("### Best Material Pair")
        best_pair = {
            "Material": ["(Cu₀.₀₀₃Pb₀.₉₉₇Te)(MnTe)₀.₀₃", "Al₀.₀₀₇₅Sb₀.₁Ge₀.₈₉₂₅Te"],
            "Type": ["p-type", "n-type"],
            "ZT at 823K": [0.82, 0.774],
            "Combined ZT": [1.594, 1.594]
        }
        st.dataframe(pd.DataFrame(best_pair))
        
        # ZT vs Temperature plot
        temperatures = np.linspace(300, 900, 100)
        zt_p = 0.82 * (temperatures/823) ** 0.5
        zt_n = 0.774 * (temperatures/823) ** 0.5
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=temperatures, y=zt_p, name="p-type"))
        fig.add_trace(go.Scatter(x=temperatures, y=zt_n, name="n-type"))
        fig.add_trace(go.Scatter(x=temperatures, y=zt_p + zt_n, name="Combined"))
        
        fig.update_layout(
            title="ZT vs Temperature",
            xaxis_title="Temperature (K)",
            yaxis_title="ZT",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Power Output Calculation")
    
    st.markdown("""
    ### Power Output Equation
    The power output of a TEG module is calculated as:
    """)
    st.latex(r'''P = \frac{\Delta T^2 (S_p - S_n)^2}{R_p + R_n}''')
    
    # Interactive parameter adjustment
    st.markdown("### Adjust Parameters")
    col1, col2 = st.columns(2)
    
    with col1:
        temp_diff = create_parameter_slider(
            "Temperature Difference (K)",
            50, 200, 100, 10
        )
        leg_height = create_parameter_slider(
            "Leg Height (mm)",
            0.5, 5.0, 2.5, 0.1
        )
    
    with col2:
        fill_factor = create_parameter_slider(
            "Fill Factor",
            0.1, 0.9, 0.5, 0.05
        )
        contact_resistivity = create_parameter_slider(
            "Contact Resistivity (Ω·m²)",
            1e-6, 1e-4, 1e-5, 1e-6
        )
    
    # Calculate and display results
    if st.button("Calculate Power Output"):
        # Simulate power calculation
        power = 0.011 * (temp_diff/100)**2 * (leg_height/2.5) * (fill_factor/0.5) * (1e-5/contact_resistivity)
        efficiency = power / (temp_diff * 0.1)  # Simplified efficiency calculation
        
        col1, col2 = st.columns(2)
        with col1:
            display_metric_card("Power Output", power, " W")
        with col2:
            display_metric_card("Efficiency", efficiency * 100, " %")

with tab3:
    st.header("Comparison with PbTe-SnSe Module")
    
    # Comparison metrics
    comparison_data = {
        "Metric": ["Power Output", "Efficiency", "ZT Value", "Temperature Range"],
        "Best Pair": ["0.011 W", "2.1%", "1.594", "300-900K"],
        "PbTe-SnSe": ["0.008 W", "1.8%", "1.2", "300-800K"],
        "Improvement": ["+37.5%", "+16.7%", "+32.8%", "+12.5%"]
    }
    st.dataframe(pd.DataFrame(comparison_data))
    
    # Comparison plot
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Best Pair",
        x=["Power", "Efficiency", "ZT"],
        y=[0.011, 2.1, 1.594],
        marker_color='#1f77b4'
    ))
    fig.add_trace(go.Bar(
        name="PbTe-SnSe",
        x=["Power", "Efficiency", "ZT"],
        y=[0.008, 1.8, 1.2],
        marker_color='#ff7f0e'
    ))
    
    fig.update_layout(
        title="Performance Comparison",
        barmode='group',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# Download section
st.markdown("---")
st.header("Download Resources")
col1, col2 = st.columns(2)
with col1:
    with open("cal.ipynb", "rb") as file:
        st.download_button(
            label="Download Calculation Notebook",
            data=file,
            file_name="power_calculation.ipynb",
            mime="application/x-ipynb+json"
        )
with col2:
    st.download_button(
        label="Download Material Data",
        data=pd.DataFrame(best_pair).to_csv(index=False),
        file_name="material_properties.csv",
        mime="text/csv"
    )