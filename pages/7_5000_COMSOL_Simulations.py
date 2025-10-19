import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 

st.header('Using COMSOL to Predict Optimal Device Geometry')

st.write("In the last sections we used thermoelectric equations and one device geometry in COMSOL to predict an optimal device performance. Now we will try to predict an optimized device geometry by trying 5000 different device configurations. This approach is inspired by the paper: 'Artificial Neural Network Enabled Accurate Geometrical Design and Optimisation of Thermoelectric Generator' Zhu, Y.; Newbrook, D. W.; Dai, P.; de Groot, C. H. K.; Huang, R.  Applied Energy 2022, 305, 117800. https://doi.org/10.1016/j.apenergy.2021.117800.")

st.header('COMSOL Model Overview')
st.write("A three-dimensional thermoelectric generator (TEG) unit cell comprising a single p-n leg pair and interconnects was constructed in COMSOL Multiphysics (version 6.2) using the Heat Transfer in Solids and Electric Currents physics interfaces. The model simulates coupled thermal and electrical transport under a fixed hot-side temperature, following the modeling framework of Zhu et al. (2022). Each configuration corresponds to a unique TEG geometry and material/contact configuration, used to evaluate open-circuit voltage (Voc), power density (PDmax), and thermal input (Qin).")

st.header('Parameter Space and Random Sampling')
st.write("A total of 5000 unique parameter sets were generated using random sampling across physically realistic ranges. Each parameter set defines a distinct TEG geometry and interface property combination. The parameters and their physical meanings are summarized below:")

# Define the data
data = {
    "Parameter": ["LHT", "HIC", "w_p", "w_n", "FF", "ρ_c", "T_h"],
    "Symbol": ["HTE", "HIC", "Wp", "Wn", "FF", "rho_c", "Th"],
    "Description": [
        "Leg height",
        "Interconnect height",
        "Width of p-type leg",
        "Width of n-type leg",
        "Fill factor",
        "Contact resistivity",
        "Hot-side temperature"
    ],
    "Unit": ["m", "m", "m", "m", "–", "Ω·m²", "K"],
    "Range": [
        "0.5e−3 to 5e−3",
        "0.5e−3 to 3e−3",
        "0.5e−3 to 5e−3",
        "0.5e−3 to 5e−3",
        "0.05 to 0.95",
        "1e−9 to 1e−7",
        "300 to 500"
    ],
    "Sampling": ["Uniform", "Uniform", "Uniform", "Uniform", "Uniform", "Log-uniform", "Uniform"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table in Streamlit
st.dataframe(df, use_container_width=True)

st.image("ANN_dataset/teg_parameter_distributions.png", caption="Histograms of 5000 parameter distributions", use_container_width=True)

st.header('Model Configuration')

st.markdown("""
Each TEG configuration was modeled in COMSOL as follows:

- **Geometry**: The model comprises two thermoelectric legs (p-type and n-type) with square cross-sections of width `w_p` and `w_n`, respectively, and height `LHT`. Legs are separated by a pitch determined by `FF`. Top and bottom metal interconnects of height `HIC` are added to each leg.

- **Materials**: All legs use the temperature-dependent Seebeck coefficient, electrical conductivity, and thermal conductivity described on the previous COMSOL simulation page. The contact resistivity `ρ_c` is modeled via thin resistive layers at the interfaces.

- **Physics Coupling**: Fully coupled multiphysics (non-segregated) solution combining Joule heating, Seebeck effect, and Fourier conduction.

- **Boundary Conditions**:
    - Bottom boundary: `T = 300 K`
    - Top boundary: `T = Th` (parametrically varied)
    - Electrical ground applied to one terminal (`Vn`), while the other (`Voc`) is measured via boundary averaging.

- **Meshing**: Physics-controlled meshing with minimum element size adjusted to resolve small interconnects and thin legs. Named boundary selections were used for terminal surfaces to ensure robustness against geometry updates.
""")

st.header('Parametric Sweep Execution')
st.markdown("""<div style="text-align: justify;">
Simulations were performed using COMSOL's **Parametric Sweep** module with "Specified Combinations" mode enabled. The full 5000-set parameter list was imported from a CSV file. Solver settings were configured with:

- **Direct fully coupled solver** (AMG)
- **No solution reuse** between steps
- **"Skip over errors"** enabled to bypass non-converging or non-meshable geometries

Each simulation produced outputs including `Voc`, `Vn`, total heat input (`Qin` via surface integration of `-ht.nteflux`), and maximum theoretical power density:
</div>""", unsafe_allow_html=True)

# LaTeX for the equation
st.latex(r"""
PD_{\text{max}} = \frac{(V_{\text{oc}} - V_{\text{n}})^2}{4 \cdot R_{\text{int}} \cdot (w_p^2 + w_n^2)}
""")


st.header('Results: Calculated Performance Metrics')
st.markdown(""" 
<div style="text-align: justify;">

For each configuration, we extracted the following from the simulation:

- **Voltage Difference** (V_diff): The difference between `Voc` and `Vn`, representing the actual voltage drop across the TEG.  
- **Maximum Power Density** (PDmax): Based on the theoretical maximum using open-circuit voltage and fixed internal resistance assumptions. 
- **Power Output (Power_W)**: Calculated as the maximum power density times the hot-side area.  
- **Efficiency**: Calculated as the ratio of maximum power density to the thermal input power, defined as:
</div>
""", unsafe_allow_html=True)
 

st.latex(r"""
\eta = \frac{P_{\text{dmax}} \cdot A}{Q}, \quad \text{where } A = w_p^2 + w_n^2
""")


st.markdown(""" 
<div style="text-align: justify;">
Maximum power density varied widely across simulations, ranging from under 50 W/m² to over 700 W/m². It generally increased with smaller contact resistivity and optimized fill factor. Voltage difference across the TEG legs (V_diff) was tightly clustered around 58 mV across all simulations, showing little variation with geometry or temperature. Simulated efficiencies were consistently low, typically below 0.5%, reflecting realistic system-level losses such as thermal leakage, contact resistance, and unused heat flow beyond the thermoelectric junction. 

</div>
""", unsafe_allow_html=True)

# === Setup ===
st.subheader("Top TEG Configurations Summary")
# === Load your summary CSV directly ===

st.markdown(""" 
<div style="text-align: justify;">
The following tables summarize the top 3 configurations (unique device geometries and temperature conditions) for each of the four performance metrics described above.
</div>
""", unsafe_allow_html=True)

# Ensure this file is in the same folder as your .py file or provide full path
df = pd.read_csv("ANN_dataset/comsol_best_configs.csv")
df.columns = df.columns.str.strip()

# Optional: round display columns
cols_to_round = ['V_diff', 'PDmax', 'efficiency', 'Power_W']
df[cols_to_round] = df[cols_to_round].round(6)

# === Display with styling ===
for metric in ['V_diff', 'PDmax', 'Efficiency', 'Power_W']:
    st.markdown(f"### Top 3 by {metric}")
    group = df[df['Metric'] == metric].copy()
    group = df[df['Metric'] == metric].copy().drop(columns=['Config_ID'])
    group1 = group.drop(columns=['Metric'])
    st.dataframe(group1, use_container_width=True)

st.markdown(""" 
<div style="text-align: justify;">
The choice of performance metric to optimize depends on the application. 
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: justify;">

- **Voltage Difference (`V_diff`)**: Choose `V_diff` when your application requires a specific minimum voltage output to operate reliably, especially in low-power or voltage-sensitive systems.  
- **Maximum Power Density (`PD_max`)**: Prioritize `PD_max` when space or weight is limited and you need to generate the most power per unit area, such as in wearables or compact heat recovery devices.  
- **Efficiency (`η`)**: Focus on efficiency when the available heat is limited, expensive, or must be conserved, like in remote sensors or space applications.  
- **Power Output (`Power_W`)**: Maximize `Power_W` when your goal is to extract as much total electrical energy as possible from an abundant heat source, regardless of efficiency.

</div>
""", unsafe_allow_html=True)