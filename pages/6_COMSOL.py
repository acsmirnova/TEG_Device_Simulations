import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import load_comsol_data, create_interactive_plot, display_metric_card

# Page configuration
st.set_page_config(
    page_title="COMSOL Simulations - TEG Analysis",
    page_icon="⚡",
    layout="wide"
)

# Title and introduction
st.title('COMSOL Simulation Analysis')
st.markdown("""
<div style="text-align: justify;">
COMSOL is a powerful simulation software that enables us to model and analyze complex physical phenomena. 
In our thermoelectric generator (TEG) project, we use COMSOL to simulate heat transfer, electric fields, 
and material properties to optimize our device design.
</div>
""", unsafe_allow_html=True)

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Material Properties", 
    "🌡️ Temperature Analysis", 
    "⚡ Voltage Analysis", 
    "📈 Results Comparison"
])

with tab1:
    st.header("Temperature-Dependent Material Properties")
    st.markdown("""
    <div style="text-align: justify;">
    We fit polynomial functions to experimental data to model how material properties change with temperature.
    This includes Seebeck coefficient, Thermal Conductivity, and Electrical Conductivity.
    </div>
    """, unsafe_allow_html=True)
    
    # Display polynomial fit
    st.image("ANN_dataset/polynomial_fits.png", caption="Polynomial fits for PbTe and SnSe", use_container_width=True)
    
    # Interactive plot of property vs temperature
    # TODO: Add interactive plot here

    # Display polynomial equations for each property for the selected material
    st.markdown("""
    #### Polynomial Fits for PbTe

    - **Electrical Conductivity:**
      $$\sigma(T) = -13.2 T^2 + 120.5 T + 23000$$
    - **Seebeck Coefficient:**
      $$S(T) = -0.02 T^2 + 1.5 T - 250$$
    - **Thermal Conductivity:**
      $$\kappa(T) = -0.0005 T^3 + 0.05 T^2 - 1.2 T + 2.1$$

    #### Polynomial Fits for SnSe

    - **Electrical Conductivity:**
      $$\sigma(T) = -10.1 T^2 + 90.3 T + 18000$$
    - **Seebeck Coefficient:**
      $$S(T) = -0.015 T^2 + 1.2 T - 200$$
    - **Thermal Conductivity:**
      $$\kappa(T) = -0.0004 T^3 + 0.04 T^2 - 1.0 T + 1.8$$
    """, unsafe_allow_html=True)

with tab2:
    st.header("Temperature Distribution Analysis")
    st.markdown("""
    <div style="text-align: justify;">
    The temperature gradient across the thermoelectric module is crucial for power generation.
    We maintain a 100K temperature difference between hot and cold sides to drive the Seebeck effect.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.image("comsol/Tgradient.png", caption="Temperature Distribution", use_container_width=True)
    with col2:
        st.markdown("""
        <div style="text-align: justify;">
        <b>Key Observations</b><br>
        - Hot side temperature: 373K<br>
        - Cold side temperature: 273K<br>
        - Temperature gradient: 100K<br>
        - Uniform heat distribution across the device
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.header("Voltage Analysis")
    st.markdown("""
    <div style="text-align: justify;">
    The open circuit voltage (Voc) is generated when no current is drawn from the circuit.
    This represents the maximum possible voltage at a given temperature gradient.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.image("comsol/Vgradient.png", caption="Voltage Distribution", use_container_width=True)
    with col2:
        st.latex(r'''
        V_{\text{oc}} = \Delta T \cdot \left(S_{\text{p-type}} - S_{\text{n-type}}\right)
        ''')
        st.markdown("""
        <div style="text-align: justify;">
        <b>Theoretical vs Simulated Results</b><br>
        - Theoretical Voc: 0.059V<br>
        - Simulated Voc: 0.0584V<br>
        - Difference: 0.0006V (1.02%)
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.header("Results Comparison")
    st.markdown("""
    <div style="text-align: justify;">
    <b>Comparison Between Theory and Simulation</b><br>
    In our study of the PbTe–SnSe thermoelectric generator, we compared the predicted voltage from theory with the results from COMSOL simulation. The theoretical open-circuit voltage (Voc), calculated using the ideal Seebeck effect and a 100K temperature difference, was <b>0.059 V</b>. The COMSOL simulation gave a slightly lower value of <b>0.0584 V</b>. This small difference is normal and expected. Unlike the simplified formula, COMSOL takes into account more realistic factors, such as how the temperature changes inside the materials, how properties like the Seebeck coefficient vary with temperature, and the influence of electrical contacts. The temperature and electric potential plots from the simulation confirm these effects. Overall, the close match shows that our model is working well and that simulation helps capture real-world behavior more accurately than theory alone.
    </div>
    """, unsafe_allow_html=True)

    # Quick metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Theoretical Voc", "0.059 V")
    col2.metric("Simulated Voc", "0.0584 V")
    col3.metric("Difference", f"{0.059-0.0584:.4f} V")

    # Visual bar comparison
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Theory", "COMSOL Simulation"],
        y=[0.059, 0.0584],
        text=["0.059 V", "0.0584 V"],
        textposition='auto',
        marker_color=['#636EFA', '#EF553B']
    ))
    fig.update_layout(
        title="Open Circuit Voltage (Voc): Theory vs COMSOL",
        yaxis_title="Voc (V)",
        xaxis_title="Method",
        height=400
    )
    st.plotly_chart(fig, use_container_width=False)

    st.info("""
    **Why is the simulated Voc slightly lower?**
    - COMSOL accounts for temperature-dependent material properties.
    - Realistic boundary conditions and contact effects are included.
    - Theoretical formula assumes ideal, constant properties.
    """)

    # Advanced: Show raw data and scatter plot in an expander
    with st.expander("Show raw data and scatter plot"):
        comsol_data = load_comsol_data()
        if comsol_data is not None:
            st.dataframe(comsol_data.head())
            fig = px.scatter(
                comsol_data,
                x='Th (K)',
                y='Electric potential (V), Voc',
                color='FF',
                title='Temperature vs Open Circuit Voltage (Voc)',
                labels={'Th (K)': 'Temperature (K)', 'Electric potential (V), Voc': 'Voc (V)', 'FF': 'Fill Factor'},
                template='plotly_white',
                width=700,
                height=400
            )
            fig.update_layout(title_x=0.5, title_font_size=20, showlegend=True)
            st.plotly_chart(fig, use_container_width=False)

# Download section
st.markdown("---")
st.header("Download Resources")
col1, col2 = st.columns(2)
with col1:
    with open("comsol/teg1.mph", "rb") as file:
        st.download_button(
            label="Download Basic TEG Model",
            data=file,
            file_name="TEG_simulation.mph",
            mime="application/octet-stream"
        )
with col2:
    with open("comsol/TEGBestP.mph", "rb") as file:
        st.download_button(
            label="Download Optimized TEG Model",
            data=file,
            file_name="Max_Efficient_TEG.mph",
            mime="application/octet-stream"
        )

# Bibliography
st.markdown("---")
st.markdown("### Bibliography")
st.markdown("""
1. Singh, N. K.; Bathula, S.; Gahtori, B.; Tyagi, K.; Haranath, D.; Dhar, A. The Effect of Doping on Thermoelectric Performance of P-Type SnSe: Promising Thermoelectric Material. Journal of Alloys and Compounds 2016, 668, 152–158. https://doi.org/10.1016/j.jallcom.2016.01.190.

2. Cao, Y.; Bai, H.; Li, Z.; Zhang, Z.; Tang, Y.; Su, X.; Wu, J.; Tang, X. Zn-Induced Defect Complexity for the High Thermoelectric Performance of n-Type PbTe Compounds. ACS Appl. Mater. Interfaces 2021, 13 (36), 43134–43143. https://doi.org/10.1021/acsami.1c14518.
""")