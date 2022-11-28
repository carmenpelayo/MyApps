# # -*- coding: utf-8 -*-

# import module
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
from PIL import Image
import scipy
from scipy.spatial import distance
from scipy.stats import zscore
import webbrowser

st.title("Welcome to my world!")
st.subheader("This is Carmen, a business strategist and data analyst looking for exciting new challenges to engage in.")
st.markdown("""---""")

#Apps
st.subheader("Apps")
st.write("**Location Recommendation Tool for Tech Businesses in Europe**")
location_recommender = "https://locationrecommender.streamlitapp.com/"
st.markdown(location_recommender, unsafe_allow_html=True)

st.markdown("**European Region Comparator**")         
region_comparator = "https://europeanregioncomparator.streamlitapp.com/"
st.markdown(region_comparator, unsafe_allow_html=True)
st.markdown("""---""")

#Resume
st.subheader("Resume")
tab1, tab2, tab3, tab4 = st.tabs(["Education", "Work", "Additional", "Documentation"])
with tab1:
    st.write("**Universidad Carlos III de Madrid** (2018-2022)")
    st.write("Bachelor of Science in *Business Management and Technology*. Inaugural Class. Taught in English.")
    st.write("Minor Degree in *Economics*.")
    st.write("GPA: 3.62 (Converted from Spanish grading system using WES iGPA Calculator).")
    st.write("Honors in *Fundamentals of Software Production* and *Environmental Economics*.")
    st.write("**University of Wisconsin - Madison** (Study Abroad, 2021-2022)")
    st.write("Coursebook: Data Science Programming I, Data Science Programming II, Machine Learning, Strategic Management, Corporate Finance, Intermediate Microeconomic Theory, Intermediate Macroeconomic Theory, Quantitative Tools for Economics, Business Ethics.")

with tab2:
    st.write("Enterprise Architecture Internship, **Spectrum Brands, Inc.** (Middleton, WI, May-Aug 2022)")
    st.write("Product Management Internship, **Clever Ads** (Madrid, ES, June-Sept 2020)")

with tab3:
    st.write("Bachelor Thesis: *Location Recommendation System for Businesses in the European ICT Industry*, July 2022. Grade 10/10.")
    st.write("Honors in *Environmental Economics* (June 2021)")
    st.write("Honors in *Fundamentals of Software Production for Digital Business* (June 2020)")

with tab4:
    #Download Resume button
    with open("Personal-Web/Resume_CarmenPelayo.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()
    st.download_button(label="Download Resume", data=PDFbyte, file_name="Personal-Web/Resume_CarmenPelayo.pdf", mime='application/octet-stream')
    
st.markdown("""---""")

#Presentation Video
col1, col2 = st.columns(2)

with col1:
   video_file = open("Personal-Web/introvideo.mp4", 'rb')
   video_bytes = video_file.read()
   st.video(video_bytes)   

with col2:
   #Intro Video
   st.subheader("Put a face to this site!")
   st.write("**Watch a 23-sec video of me presenting my webpage :)**")
   
   #Contact
   st.subheader("Contact")
   st.markdown("- **LinkedIn**: https://www.linkedin.com/in/carmenpelayofernandez/", unsafe_allow_html=True)
   st.markdown("- **E-Mail**: carmenpelayofdez@gmail.com")
   st.markdown("- **Phone**: +34 685 33 88 17")
   
   #Signature
   st.subheader("**Much love,**")
   st.image("Personal-Web/art3.png", width=175)
    
   
#USER INTERACTION
#st.subheader('**What brings you here?**')
#mot_vals = ['Just curiosity.', 'I want you in my team!']
#counts_cur = 0
#counts_hire = 0
#motivation = st.radio("", tuple(mot_vals), key=3)
#if motivation == "I want you in my team!":
    #st.write("😁 Happy to hear that! You can contact me at:")
    #linkedin = 'https://www.linkedin.com/in/carmenpelayofernandez/'
    #st.markdown(linkedin, unsafe_allow_html=True)
    #st.write("[LinkedIn](%s)" % linkedin)
    #st.write("carmenpelayofdez@gmail.com")
    #counts_hire +=1
#elif motivation == "Just curiosity.":
    #st.write("😊 Sounds good!You can check my apps to get a sense of my work! To do so, select any of the apps I created in the menu above.")
    #counts_cur += 1
   
