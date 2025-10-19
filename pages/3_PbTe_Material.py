import streamlit as st
import numpy as np
import matplotlib
import pandas as pd
from PIL import Image

st.title('PbTe Material')
st.header('Introduction')
st.markdown(""" <div style="text-align: justify;">
 Lead telluride alloys were among the first materials to be investigated and used in thermoelectric generators for space crafts in the mid 20th century. However, their full potential in thermoelectric applications has only recently been recognized as far greater than previously believed. PbTe based alloy was chosen as the thermoelectric material to provide power to Nasa\'s MSL rover Curiosity, the most sophisticated Mars rover to date .\n\n
 PbTe is a Halite, rock salt structure (cubic face centered) and crystallizes in the cubic Fm̅3m space group. In this structure, Pb²⁺ ions are bonded to six equivalent Te²⁻ ions, forming a mixture of corner- and edge-sharing PbTe₆ octahedra. Similarly, each Te²⁻ ion is bonded to six equivalent Pb²⁺ ions, forming a similar PbTe₆ octahedra. The corner-sharing octahedra are not tilted and the Pb-Te bond lengths in the structure are 3.27 Å. The high symmetry and isotropy of the structure contributes significantly to PbTe\'s thermoelectric performance, including its low lattice thermal conductivity, which is advantageous for maintaining a temperature gradient across the material. \n\n
 </div>""", unsafe_allow_html=True)
st.image("Images/Pb1Te1-1314916.jpg", caption="https://www.webelements.com/compounds/lead/lead_telluride.html#google_vignette", width=400)
st.markdown(""" <div style="text-align: justify;"> PbTe is an intrinsic semiconductor material and possesses a narrow direct bandgap (approximately 0.31 eV at room temperature), which is ideal for achieving high Seebeck coefficients, especially at elevated temperatures. A higher Seebeck coefficient indicates higher performance of a thermoelectric material. Electronic properties of PbTe can be tuned through doping, typically with bismuth, sodium, or antimony, to enhance the carrier concentration and improve the power factor (S^2σ), where S is the Seebeck coefficient and σ is the electrical conductivity. Due to its low thermal conductivity, PbTe makes one of the finest thermoelectric materials. This low thermal conductivity, which decreases further at higher temperature, combined with favorable electrical properties, allows PbTe to achieve high thermoelectric efficiency.\n\n
A thermoelectric material's potential to convert heat into electricity is quantified by the thermoelectric figure of merit, zT. The figure of merit for PbTe increases significantly with increasing temperature. Recent studies including precise compositional control and modern characterization have revealed maximum zT values of ∼1.4 for PbTe. This value is intrinsic to this material for both n- and p-type. With PbTe based alloys a higher figure of merit can be achieved, where zT reaches a value of ∼1.8 for homogeneous PbTe-PbSe materials.\n\n
What puts PbTe in an advantageous position among other thermoelectric materials is its easy processability. It is comparatively soft due to its rock salt crystal structure with a higher degree of symmetry leading to relatively weak interatomic bonding. The thermal, electrical and mechanical properties of PbTe make it an attractive material for application thermoelectric energy conversion.
</div>""", unsafe_allow_html=True)


properties = {
    "Property": [
        "Crystal Structure",
        "Lattice Constant",
        "Bandgap",
        "Density",
        "Melting Point",
        "Seebeck Coefficient (S)",
        "Thermal Conductivity (κ)",
        "Electrical Conductivity (σ)",
        "Carrier Type",
        "Carrier Concentration",
        "Figure of Merit (ZT)",
        "Thermal Expansion Coefficient",
        "Elastic Modulus",
        "Thermoelectric Operating Range",
        "Phonon Scattering",
        "Processing"
    ],
    "Value/Description": [
        "Halite (rock salt) structure, cubic Fm3̅m space group",
        "6.46 Å",
        "~0.31 eV (direct, at room temperature)",
        "8.16 g/cm³",
        "~924 K (651°C)",
        "100–300 µV/K (varies with temperature and doping)",
        "~2 W/m·K at room temperature; decreases to ~1 W/m·K at high temperatures (700–900 K)",
        "Highly tunable via doping; ranges from ~100–10,000 S/m depending on carrier concentration",
        "Can be tuned to n-type or p-type through doping (e.g., with Bi, Sb, Na)",
        "~10¹⁸–10²⁰ cm⁻³ (typical range for optimized thermoelectric performance)",
        "~2 at 700–800 K",
        "~19 × 10⁻⁶ /K",
        "~50 GPa (low elastic modulus indicates softness and ease of processing)",
        "400–900 K (optimal performance)",
        "Strong due to heavy atoms (Pb, Te) and anharmonic bonding",
        "Relatively soft, easy to process and fabricate"
    ]
}

df = pd.DataFrame(properties)
st.header("Key Properties of Lead Telluride (PbTe)")

# Display the table
st.table(df)

st.subheader("Bibliography")
st.markdown(""" <div style="text-align: justify;">
            
1. LaLonde, A. D.; Pei, Y.; Wang, H.; Jeffrey Snyder, G. Lead Telluride Alloy Thermoelectrics. Materials Today 2011, 14 (11), 526–532. https://doi.org/10.1016/S1369-7021(11)70278-4.\n\n  
2. Ben-Ayoun, D.; Gelbstein, Y. Bismuth Telluride Solubility Limit and Dopant Effects on the Electronic Properties of Lead Telluride. In Advanced Thermoelectric Materials for Energy Harvesting Applications; Memon, S., Ed.; IntechOpen, 2019. https://doi.org/10.5772/intechopen.84602.\n\n
3. Materials Project. Materials Project. https://next-gen.materialsproject.org/materials/mp-20943?formula=TePb#properties.\n\n
4. Thermoelectric materials - Wikipedia. https://en.wikipedia.org/wiki/Thermoelectric_materials .

</div>""", unsafe_allow_html=True)