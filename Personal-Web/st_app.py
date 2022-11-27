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

# Webpage
st.title("Welcome to my world!")
st.subheader("This is Carmen, a business strategist and data analyst looking for exciting new challenges to engage in.")

st.markdown("""---""")

#RESUME
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Education", "Work", "Additional", "Apps", "Contact"])
with tab1:
    st.subheader("Education")
    st.write("Academic exchange at **University of Wisconsin - Madison** (2021-2022)")
    st.write("B.S. in *Business Management and Technology*, **Universidad Carlos III de Madrid** (2018-2022)")
    st.write("Minor Degree in *Economics*, **Universidad Carlos III de Madrid** (2019-2022)")

with tab2:
    st.subheader("Work")
    st.write("Enterprise Architecture Internship, **Spectrum Brands, Inc.** (Middleton, WI, May-Aug 2022)")
    st.write("Product Management Internship, **Clever Ads** (Madrid, ES, June-Sept 2020)")

with tab3:
    st.subheader("Certifications, Awards and Publications")
    st.write("Bachelor Thesis: *Location Recommendation System for Businesses in the European ICT Industry*, July 2022. Grade 10/10.")
    st.write("Honors in *Environmental Economics* (June 2021)")
    st.write("Honors in *Fundamentals of Software Production for Digital Business* (June 2020)")

with tab4:
    st.subheader("Apps")
    location_recommender = "https://locationrecommender.streamlitapp.com/"
    st.markdown(location_recommender, unsafe_allow_html=True)
    region_comparator = "https://europeanregioncomparator.streamlitapp.com/"
    st.markdown(region_comparator, unsafe_allow_html=True)

with tab5:
    st.subheader("Contact")
    linkedin = 'https://www.linkedin.com/in/carmenpelayofernandez/'
    st.markdown(linkedin, unsafe_allow_html=True)
    st.write("carmenpelayofdez@gmail.com")
    
    #Download Resume button
    with open("Personal-Web/Resume_CarmenPelayo.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()
    st.download_button(label="Download Resume", data=PDFbyte, file_name="Personal-Web/Resume_CarmenPelayo.pdf", mime='application/octet-stream')
    
    #LinkedIn button
    #redirect("https://www.linkedin.com/in/carmenpelayofernandez/")
    #linkedin = st.button("LinkedIn")
    #if linkedin:
      #webbrowser.open("https://www.linkedin.com/in/carmenpelayofernandez/")

st.markdown("""---""")

#Presentation Video
col1, col2 = st.columns(2)

with col1:
   video_file = open("Personal-Web/introvideo.mp4", 'rb')
   video_bytes = video_file.read()
   st.video(video_bytes)   

with col2:
   st.subheader("Check my 30-sec presentation video!")
   st.image("Personal-Web/art3")
    
   
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
   
   
   
