# -*- coding: utf-8 -*-

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

#DATABASE IMPORT AND PREPARATION
#Database containing region names
nuts = pd.read_excel("Regional Info DEF.xlsx")
nuts2 = nuts[["Region", "Region Name", "Country Name"]]
nuts2 = nuts2.rename(columns = {"Region":"NUTS 2 Code"})

#Database containing region values
dfn = pd.read_excel("FINAL Regional Vectors.xlsx")
regions = dfn["NUTS 2 Code"].tolist()
dfn = dfn.set_index("NUTS 2 Code")

#CONFIGURATOR
st.header("📊 REGION COMPARATOR")
st.write("This app evaluates 270 European regions in 21 socio-economic parameters. Use the *USER GUIDE* below to learn how to configure the search and interpret the results obtained.")
st.subheader("Which regions would you like to compare?")
reg = st.multiselect("", regions, "ES30")

#RESULTS
st.table(dfn.loc[reg].T)

#USER GUIDE
st.header("USER GUIDE")
tab1, tab2, tab3 = st.tabs(["Regions", "Parameters", "Scores"])
with tab1:
    st.subheader("Region codes and names:")
    st.table(nuts2)
with tab2:
    st.subheader("How to interpret the parameters displayed:")
    st.write(
    """
    - **AI**: Total value of AI (Artificial Intelligence) projects developed in the region.
    - **Big Data**: Total value of Big Data projects developed in the region.
    - **Computing**: Total value of Computing projects developed in the region.
    - **Cybersecurity**: Total value of Cybersecurityprojects developed in the region.
    - **Internet**: Total value of Internet projects developed in the region.
    - **IoT**: Total value of IoT projects developed in the region.
    - **Media & Communication**: Total value of Media & Communication projects developed in the region.
    - **Robotics**: Total value of Robotics projects developed in the region.
    - **Software**: Total value of Software projects developed in the region.
    - **SMEs**: Number of SMEs (Small and Mid-sized Enterprises) in a region (those with no more than 250 employees).
    - **LEs**: Number of LEs (Large Enterprises) in a region (those with more than 250 employees).
    - **Research**: Number of organizations focused on developing new technological offerings based on engineering innovation or scientific discoveries and advances (universities or other higher-level research institutions).
    - **Development**: Number of organizations focused on R&D, to build and enhance existing technologies (technological centers or research organizations).
    - **Integration**: Number entities dedicated to integrating existing technologies with products or services in order to expand business capabilities (firms).
    - **EU grants**: Total euro amount that the European Union has given to local entities through the Horizon2020 program.
    - **Capital**: Score calculated as the average of FDI (Foreign Direct Investments) & technology transfer, R&D expenditure (% of GDP) and venture capital availability.
    - **Unicorns**: Total valuation of all the unicorns in a region. Unicorns are start-up companies valued at more than a billion dollars, typically in the technology sector.
    - **Human Resources**: Score calculated looking at the researchers in R&D, university-industry collaboration, skillset of university graduates, extent of staff training, and the availability of scientists & engineers.
    - **Tech Hubs**: Number of tech hubs in each European region. A high number of tech hubs in a region is synonymous with it being a productive and proliferating location, given the abundance of opportunities and advantages for tech entities.
    - **Government**: Score calculated looking at how the government ensures policy stability, the legal frameworks' adaptability to digital business models, the efficiency in settling disputes, the efficiency in challenging regulations, the burden of governmental regulation, the number of days to start a business and e-Gov services.
    - **Infrastructure**: Score calculated by observing at each region's 4G coverage, fiber coverage, Internet bandwith per user, 5G commercial networks, number of Internet exchange points, the number and maturity of 5G pilots, the time to get electricity, 4G's launch year and 5G spectrum auction plans.
    """
    )

with tab3:
    st.subheader("How to read the scores obtained:")
    st.write("Standard scores are given in a -1 to 1 scale.")
    st.write("""
        - A score of 0 represents the mean score of the regions.
        - A score of -1 represents the region is in the lower 15.9% of the regions. Lower scores correspond to left outliers.
        - A score of 1 represents the region is in the top 15.9% of the regions. Higher scores correspond to right outliers.
    """)
    image = Image.open('normalstandard.jpg')
    st.image(image)
