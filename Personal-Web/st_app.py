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
    st.write("**UNIVERSIDAD CARLOS III DE MADRID** (2018-2022)")
    st.write("**Bachelor of Science in *Business Management and Technology* with a Minor Degree in *Economics*.**")
    st.write("Inaugural Class. Taught in English. GPA: 3.62. Honors in *Fundamentals of Software Production* and *Environmental Economics*. Bachelor Thesis: *Location Recommendation System for Businesses in the European ICT Industry* (Grade A+).")
    st.write("")
    st.write("**UNIVERSITY OF WISCONSIN - MADISON** (Study Abroad, 2021-2022)")
    st.write("Coursebook: *Data Science Programming I, Data Science Programming II, Machine Learning, Strategic Management, Corporate Finance, Intermediate Microeconomic Theory, Intermediate Macroeconomic Theory, Quantitative Tools for Economics, Business Ethics.*")

with tab2:
    st.write("**DELOITTE CONSULTING. Enterprise Technology & Transformation Analyst**. Madrid, Spain. September 2022-Present.")
    st.markdown("- Defining triggers for the automation of database inserts and updates using Salesforce Apex.")
    st.markdown("- Building customer journeys for e-mail and SMS communications using Salesforce Marketing Cloud.")
    st.write("")
    st.write("**SPECTRUM BRANDS. Enterprise Architecture Intern**. Middleton, Wisconsin, United States. May-August 2022.")
    st.markdown("- Analyzed the potential implementation of blockchain technologies in the organization’s supply chain.")
    st.markdown("- Created a task assignment matrix for projects in the IT department.")
    st.write("")
    st.write("**CLEVER ADS. Product Management Intern**. Madrid, Spain. June-Sept 2020.")
    st.markdown("Studied the launch of a new niche product, Clever Hotel Ads.")
    st.markdown("Designed corporate e-mails and pop-up web notifications using WordPress.")


with tab3:
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
   
