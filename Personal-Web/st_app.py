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

st.title("💗 Welcome to my site!")
st.subheader("This is Carmen, a business strategist and data scientist aiming to lead the next generation of sustainable, data-driven organizations.")
st.write("In this website, you will find links redirecting to some **web applications** I have built, as well as my **resume** and **contact information**. *Enjoy!*")
st.markdown("""---""")

#Apps
st.subheader("Apps & Projects")

st.write("📈 **Predicting Building's Energy Consumption**")
st.write("I built a machine learning model to predict energy consumption in buildings with minimal data. I implemented an autoML system for time series (autoTS) and identified the ExtraTreeRegressor algorithm as the best-performing estimator. The resulting model, which was trained over a >1.4M records dataset, led to an accuracy of 83% (on R-squared score) on unseen data. This enabled the creation of a system that predicts the optimal energy load in a building and adjusts the temperature accordingly to avoid electricity waste.")
st.write("*This project won Schneider Electric's 'Cold Start Challenge at the **MIT Energy & Climate Hack 2023**.*")
st.write("")

st.write("🔍 **Location Recommendation Tool for Tech Businesses in Europe**")
st.write("This app aims to provide a decision-making support solution for entities operating in the ICT (Information and Communication Technologies) industry that are interested in locating their operations in Europe. It delivers a customized location recommendation based on industry needs and firm-specific characteristics. Additionally, the app can be configured to fit other purposes, like the search of specialized employment, the visualization of socio-economic data or the discovery of available capital funding.")
st.markdown("Check it out at: https://locationrecommender.streamlitapp.com/", unsafe_allow_html=True)
st.write("")

st.write("📊 **European Region Comparator**") 
st.write("This app can be employed to compare European regions in various socio-economic factors in a visual, user-friendly way. Any amount of regions from the 270 available can be selected to observe the differences and similarities in scores for 21 dimensions (including the technological infrastructure, the availability of qualified personnel or the easiness to open a business).")
st.markdown("Check it out at: https://europeanregioncomparator.streamlitapp.com/", unsafe_allow_html=True)
st.write("")

#st.write("✨ **K-Means Spherical Clusterer (Coming Soon)**") 
#st.write("This app will gather a user's selection of European regions and a number of groups (K) on which to perform a K-Means Spherical Clustering. As a result, a visual map will be returned to detect groups of locations with the most similar characteristics, potentially unveiling interesting relationships in the European territory.")
#st.markdown("Check the elementary program at: https://github.com/carmenpelayo/Carmen-Pelayo/tree/main/Clustering", unsafe_allow_html=True)
#st.markdown("""---""")

#Resume
st.subheader("Resume")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Education", "Work", "Activities", "Certifications", "Documentation"])
with tab1:
    st.write("❤️ **BOSTON UNIVERSITY** (2023-2024)")
    st.write("**Master of Science in *Data Science*.**")
    st.write("*Faculty of Computing and Data Sciences Merit Scholarship* recipient.")
    st.write("Coursework: *Machine Learning, Deep Learning, Reinforcement Learning, Cryptography, Time Series & Forecasting, Database Management Systems, Data Science Tools, AI Ethics*.")
    st.write("")
    
    st.write("💙 **UNIVERSIDAD CARLOS III DE MADRID** (2018-2022)")
    st.write("**Bachelor of Science in *Business Management and Technology* with a Minor Degree in *Economics*.**")
    st.write("Graduated with honors in *Fundamentals of Software Production* and *Environmental Economics*.")
    st.write("Bachelor Thesis: *Location Recommendation System for Businesses in the European ICT Industry* (Grade A+).")
    st.write("")
    
    st.write("❤️ **UNIVERSITY OF WISCONSIN - MADISON** (Study Abroad, 2021-2022)")
    st.write("Coursework: *Data Science Programming I, Data Science Programming II, Machine Learning, Strategic Management, Corporate Finance, Intermediate Microeconomic Theory, Intermediate Macroeconomic Theory, Quantitative Tools for Economics, Business Ethics.*")

with tab2:
    st.write("🤝🏼 **AVASANT**")
    st.write("**Associate Consultant**. April 2023-August 2023 in Madrid, Spain.")
    st.write("- Led the negotiation with workflow software providers for a major vaccine research and development NGO in the UK.")
    st.write("- Analyzed potential scenarios in the negotiation of a multi-million IT-offshoring contract for a major US healthcare provider.")
    st.write("")
    
    st.write("💻 **DELOITTE CONSULTING**")
    st.write("**Enterprise Technology & Transformation Analyst**. September 2022-March 2023 in Madrid, Spain.")
    st.write("- Assisted in the migration of two Salesforce systems to a unified instance after a multinational corporate merger.")
    st.write("- Designed and implemented customer journeys in Salesforce Marketing Cloud and analyzed the resulting customer data.")
    st.write("")
    
    st.write("⚙️ **SPECTRUM BRANDS**")
    st.write("**Enterprise Architecture Intern**. May-August 2022 in Middleton, Wisconsin, United States.")
    st.write("- Researched the potential implementation of blockchain in the organization’s supply chain. My findings escalated to the C-suit.")
    st.write("- Defined financial metrics to evaluate the economic impact of the Enterprise Architecture division in the business.")
    st.write("")
    
    st.write("📊 **CLEVER ADS**")
    st.write("**Product Management Intern**. June-Sept 2020 in Madrid, Spain.")
    st.write("- Researched the market to evaluate the feasibility of launching an SEM optimization tool in the hospitality sector.")
    st.write("- Learned about SEO techniques to maximize revenue in Google Ads and other online marketing platforms.")

with tab3:
    st.write("**Undergraduate Research**. *Knowledge Reuse Group*, Universidad Carlos III de Madrid. September  2021–June 2022.")
    st.write("""For the development of my bachelor thesis, I collaborated with the Knowledge 
                Reuse Group, an initiative founded by UC3M's School of Computer Science and 
                Engineering to leverage data from multiple disciplines to develop scientific 
                solutions. During the academic year 2021-2022, I worked with Professor Jose 
                Maria Alvarez Rodriguez to create a tool that recommends technological entities 
                where to locate their operations in Europe, according to individual attributes 
                and market needs.""")
    st.write("")
    
    st.write("**Soft Skills and Professional Mentoring Seminar**. Universidad Politécnica de Madrid. February  2021–April 2022.")  
    st.write("""I participated in a 3-month seminar where they prepared students to
                succeed in their professional careers by training soft skills and getting
                in contact with successful professionals, like CEOs and members of the
                Spanish government. The final activity of the seminar consisted of
                giving a 10-minute presentation about our career path and future
                goals in front of the rest of participants and all the professionals. I was
                recognized as one of the best-performing presenters in the room,
                receiving special credit from WiBLE's founder Javier Martinez, and
                Madrid Assembly Representative Pilar Martinez.""")
    st.write("")
    
    st.write("**StartUp Program**. PwC & Junior Achievement. September 2019–May 2020.")
    st.write("")
    
    st.write("**Entrepreneurship Seminar** (30 hours). Universidad Carlos III de Madrid. September 2019–December 2019.")
    st.write("")
    
    st.write("**StartUp Yourself Brazil Scholarship**. AIESEC & BBVA. May 2019.")   
    st.write("""I was selected to intern at a marketing company in Brazil during the
                summer of my freshman year of college. To earn this scholarship, I had
                to prepare a video explaining why I wanted to do this internship, and
                my video was the most voted one.""")
    st.write("")
    st.write("**España Rumbo Al Sur Expedition**. Morocco Edition. August 2017.")
    st.write("**Troop Member**. Grupo Scout Eslabón. 2010-2013.")
      
with tab4:
    st.write("**Salesforce Administrator Certification**. Salesforce. January 2023.")
    st.write("**Introduction to Management Information Systems Certification**. EdX. April 2021.")
    st.write("**Google Ads Search Certification**. Google. June 2020")   
    st.write("**Fundamentals of Digital Marketing Certification**. Google. April 2020.")
    st.write("**Camp Counselor Certification**. Junta de Andalucía. February 2019.")
    st.write("**C1 Advanced English Certification**. University of Cambridge. November 2016.")
    st.write("**Grade 4 Piano Certification**. Associated Board of the Royal Schools of Music. 2013.")
             
with tab5:
    #Download Resume button
    st.write("You can download my one-page **resume** in PDF format here:")
    with open("Personal-Web/Resume-Dec2023-CarmenPelayo.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()
    st.download_button(label="Download Resume", data=PDFbyte, file_name="Personal-Web/CV_CarmenPelayo_Jan2023.pdf", mime='application/octet-stream')
    
    #Download Thesis button
    st.write("You can download my 84-page **bachelor thesis** in PDF format here:")
    with open("Personal-Web/BachelorThesis_CarmenPelayo.pdf", "rb") as pdf_file:
      PDFbyte = pdf_file.read()
    st.download_button(label="Download Bachelor Thesis", data=PDFbyte, file_name="Personal-Web/BachelorThesis_CarmenPelayo.pdf", mime='application/octet-stream')
    
st.markdown("""---""")

#Presentation Video
col1, col2 = st.columns(2)

with col1:
   video_file = open("Personal-Web/introvideo.mp4", 'rb')
   video_bytes = video_file.read()
   st.video(video_bytes)   

with col2:
   #Contact
   st.subheader("Contact")
   st.markdown("- **LinkedIn**: https://www.linkedin.com/in/carmenpelayofernandez/", unsafe_allow_html=True)
   st.markdown("- **GitHub**: https://github.com/carmenpelayo/", unsafe_allow_html=True)
   st.markdown("- **E-Mail**: carmenpelayofdez@gmail.com")
   st.markdown("- **Phone**: +34 685 33 88 17 / +1 617 206 7050")
   
   st.markdown("""---""") 
   
   #Intro Video
   st.subheader("Welcome Video")
   st.write("⬅️ **Put a face to this site by watching this 23-sec video of me presenting my website!**")
    
   #Signature
   st.write("**😊 Made with love by**")
   st.image("Personal-Web/signature.png", width=175)
    
   
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
   
