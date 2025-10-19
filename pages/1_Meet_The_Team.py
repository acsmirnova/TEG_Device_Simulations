import streamlit as st
import numpy as np
import matplotlib
import pandas as pd
from PIL import Image
st.header('Team presentation')
st.write('**Web developper**') 
col1,col2=st.columns([0.3,0.7],gap='small',vertical_alignment='center')
with col1:
    #image=Image.open('.\images\test.jpeg') # For Linux
   st.image("Images/Hedir.jpeg", width=200)  
with col2:
    st.write('**Hedir OUARDI**')
    st.markdown( """ <div style="text-align: justify;">
                Hedir is the website manager. She is a second year french engineering student from Grenoble. Her task is to maintain the discipline of the website and to check the information uploaded by the different members of the group.
                </div>""", unsafe_allow_html=True) #Here is the place to put a few words of presentation


st.write('**Project manager**')
col1,col2=st.columns([0.3,0.7],gap='small',vertical_alignment='center')
with col1:
    st.image("Images/Anna.jpeg", width=200)
with col2:
    st.write('**Anna SMIRNOVA**')
    st.markdown( """ <div style="text-align: justify;">
                Anna is the Project Manager. She is from the US and is starting her first year at the TU Darmstadt. Her role is to delegate tasks, organize workflows and plan meeting agendas.
                </div>""", unsafe_allow_html=True) #Here is the place to put a few words of presentation

st.write('**Project supervisor**')
col1,col2=st.columns([0.3,0.7],gap='small',vertical_alignment='center')
with col1:
    #image=Image.open('.\images\test.jpeg') #for linux
    st.image("Images/Koly.jpg", width=200)    
with col2:
    st.write('**Tanzila Akter KOLY**')
    st.markdown( """ <div style="text-align: justify;">
                Tanzila is the project supervisor. She is a first year masters student in Grenoble INP-Phelma from Bangladesh. She is responsible for tracking if the work progresses as expected and reminding of deadlines.
                </div>""", unsafe_allow_html=True) #Here is the place to put a few words of presentation

