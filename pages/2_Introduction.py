import streamlit as st
import numpy as np
import matplotlib
import pandas as pd
from PIL import Image

st.header('Introduction')

st.markdown(""" <div style="text-align: justify;">
The climate crisis has increased the demand for sustainable energy technologies. Thermoelectric energy generation is an efficient solution that converts waste heat directly into electrical energy, reducing reliance on fossil fuels and greenhouse gas emissions.
As a promising technology to aid in the coming energy transition, thermoelectrics enable waste heat recycling. 
</div>""", unsafe_allow_html=True)

st.subheader('How it works')
st.markdown(""" <div style="text-align: justify;">
Thermoelectric energy generation works due to temperature gradients and uses the Seebeck effect to produce electricity from heat. Thermoelectric generation occurs when there is a temperature gradient between two materials, causing the movement of particles (such as electrons) from the hot side to the cool side. To maintain the temperature gradient needed to generate energy, 
materials should have a balance of low thermal conductivity but high electrical conductivity. This is often a challenge as many materials, such as bismuth telluride, have high electricity conductivities but low thermal conductivities. A heat sink is also required to keep the temperature difference between the two sides to allow the thermoelectric device to work continuously. 
This electricity can be used to run devices or used to charge batteries, increasing the versatility of thermoelectric systems.\n
\n   </div>""", unsafe_allow_html=True)
st.markdown(""" \n """)
col1, col2 = st.columns(2)

with col1:
    st.image("images/XCPh9Vp.jpg", caption="Thermoelectric Generator, https://www.sciencedirect.com/science/article/pii/S2666523923000144", width=300)

with col2:
    st.image("images/1-s2.0-S0921510723008644-ga1_lrg.jpg", caption="TEG Couple Module, https://www.sciencedirect.com/science/article/abs/pii/S0921510723008644", width=350)

st.subheader('Types of Thermoelectric Material')
st.markdown("""
            <div style="text-align: justify;"> Thermoelectric materials are found in three classes: organic, inorganic, and organic-inorganic hybrid materials. Organic materials include conductive polymers (p or n type), nanotube-polymer composites, doped single-walled carbon nanotubes, nanotube yarns, and a variety of other carbon-based nanostructures. 
            The benefits of organic thermoelectrics are that they are lightweight, flexible, and have the potential to be mass-produced at a low cost (like plastic manufacturing). However, due to a lack of long-range order in polymeric and nanotube structures compared to inorganic crystals, they suffer from low conductivity. \n
            \n
            Another classification of thermoelectric materials concerns their dimensionality, namely 2D or 3D materials. 2D thermoelectric materials are only a few atomic layers thick (e.g., graphene and transition metal dichalcogenides). Low weights and large surface areas enable thermoelectric devices to operate in compact systems for applications in flexible electronics and sensors.
            On the other hand, materials that have a more ample volume are considered 3D thermoelectric materials, like bismuth telluride and lead telluride. </div>""", unsafe_allow_html=True)
st.subheader('Applications')
import streamlit as st

st.markdown(""" <div style="text-align: justify;">
            
#### Applications of Thermoelectric Generators

1. **Waste Heat Recovery**
   - **Industrial Waste Heat:** TEGs can harvest waste heat present in industries like steel, glass, cement, etc., and produce electricity for other applications.
   - **Automotive Waste Heat:** TEGs can be used for automotive exhaust systems to convert engine waste heat into electric power, maximizing fuel efficiency.

2. **Aerospace and Space Applications**
   - **Radioisotope Thermoelectric Generators (RTGs):** Used as power sources using radioactive decay heat in space missions (Voyager, Curiosity rover by NASA).
   - **Deep Space Probes:** TEGs provide reliable power for satellites and space exploration where solar panels are not useful.

3. **Renewable Energy Systems**
   - **Solar Thermoelectric Generators:** TEGs generate electricity using concentrated solar heat as an alternative to photovoltaic cells.
   - **Geothermal Energy:** TEGs can generate electricity using geothermal heat sources in remote, off-the-grid locations.

4. **Remote Power Generation**
   - **Off-grid Power Supply:** Used in remote areas without access to a normal power source, such as military sites and rural electrification.
   - **Wearable Power Generators:** Small TEGs can be integrated into clothing to generate power from body heat, ideal for medical and military applications.

5. **Electronics and IoT Devices**
   - **Self-Powered Sensors:** TEGs can power wireless sensors and IoT devices for smart homes, industry, and environmental monitoring.
   - **Thermal Management of Electronics:** Waste heat can be recovered using TEGs, enhancing battery life in electronic devices.

6. **Biomedical Applications**
   - **Implantable Medical Devices:** TEGs can provide continuous power from body heat for pacemakers and other medical implants.
   - **Thermal Energy Harvesting in Wearables:** Used in fitness trackers and smartwatches to generate power without frequent charging.
</div>""", unsafe_allow_html=True)


st.markdown(""" <div style="text-align: justify;">
The efficiency of this technology, combined with the low environmental impact, makes it interesting to convert waste heat—a typical unavoidable byproduct in industrial and automotive applications—into useful energy. Recent developments in nanotechnology and material science can continuously enhance thermoelectric performance, making it more applicable to various renewable energy systems and daily technologies.
</div>""", unsafe_allow_html=True)

st.markdown('### Bibliography')
st.markdown( """ <div style="text-align: justify;">
    
    **Article 1**: Sun et al., Pushing thermoelectric generators toward energy harvesting from the human body: Challenges and strategies, Materials Today 57, 121-145 (2022). \n
    \n
    **Article 2**: Wu et al., Thermoelectric converter: Strategies from materials to device application, Nano Energy 91, 106692 (2022). \n
    \n
    **Article 3**: Zhang et al., Flexible thermoelectric materials and devices: From materials to applications, Materials Today 46, 62-108 (2021). \n
    \n
    **Article 4**: Sanad et al., Thermoelectric Energy Harvesters: A Review of Recent Developments in Materials and Devices for Different Potential Applications, Topics in Current Chemistry 378, 48 (2020). \n
    \n
    **Article 5**: Petsagkourakis et al., Thermoelectric materials and applications for energy harvesting power generation, Science and Technology of Advanced Materials 19, 836-862 (2018).
    </div>""", unsafe_allow_html=True)

