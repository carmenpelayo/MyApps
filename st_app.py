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

def home():
    st.title("Welcome to my world!")
    st.subheader("This is Carmen, a recently-graduated business strategist and program coder looking for exciting new challenges to engage in.")
    st.write('What brings you here?')
    mot_vals = ['Just curiosity.', 'Your profile seems interesting.', 'I want you in my team!']
    motivation = st.selectbox("Select your motivation.", mot_vals)

def main_page():
    st.title("Location Recommendation System for Businesses in the European ICT Industry")
    st.subheader('This program was made by Carmen Pelayo Fernandez in 2022')
    st.write("""Given the high importance of making the right business location choices, this tool aims to provide a decision-making support solution 
             for entities operating in the European ICT (Information and Communication Technologies) industry. It can also be configured to fit other purposes, 
             like the search of specialized employment, the visualization of socio-economic data or the discovery of available capital funding.
             """)
    image = Image.open('How-to-Find-the-Perfect-Location-for-Your-Small-Business.jpg')
    st.image(image)
    
def location_recommendation():
    st.title("Location Recommendation System for Businesses in the European ICT Industry")
    st.subheader('This program was made by Carmen Pelayo Fernandez in 2022')
    st.write("""Given the high importance of making the right business location choices, this tool aims to provide a decision-making support solution 
             for entities operating in the European ICT (Information and Communication Technologies) industry. It can also be configured to fit other purposes, 
             like the search of specialized employment, the visualization of socio-economic data or the discovery of available capital funding.
             """)
    st.header("🔎 CONFIGURE YOUR SEARCH")
    st.subheader("Step 1: Select your entity's attributes.")
    
 #CAPTURING INPUT

    #STEP 1: Creating the selection vector (14 values)
    input_vector = []

    # DIMENSION 1: Tech areas
    st.write('In which technological areas are you specialized/interested?')
    areas = ['AI',
             'Big Data',
             'Computation',
             'Cybersecurity',
             'Internet',
             'IoT',
             'Media & Communication',
             'Robotics',
             'Software']
    D1 = st.multiselect("", areas, areas)
    # Filling first 9 values of the input_vector 
    for a in areas:
        if a in D1:
            input_vector.append(1)
        else:
            input_vector.append(0)
            
    # DIMENSION 2: Company Size
    st.write('Are you a small/mid-sized enterprise (SME) or a large enterprise (LE)?')
    D2_val = ['Small/Mid-sized enterprise', 'Large Enterprise']
    D2 = st.radio("", tuple(D2_val), key=2, horizontal=True)
    # Filling index 10 and 11 of the input_vector
    if D2 == "SME":
        input_vector.append(1)
        input_vector.append(0)
    else:
        input_vector.append(0)
        input_vector.append(1)
    
    # DIMENSION 3: Technological Maturity
    st.write('Are you researching, developing or integrating technology?')
    D4_val = ['Research', 'Development', 'Integration']
    D4 = st.multiselect("", D4_val, 'Research')
    # Filling indexes 12, 13 and 14 of the input_vector
    for maturity in D4_val:
        if maturity in D4:
            input_vector.append(1)
        else:
            input_vector.append(0)
  

    #STEP 2: Creating the weights vector (8 values)
    st.markdown("""---""")
    weights = []
    st.subheader("Step 2: Configure your location preferences.")
    st.write('How important are the following business parameters in your location decision?')
    st.write('A score of 0 corresponds to *not important at all* and a score of 100 corresponds to *completely important*.')
    
    dimensions = ["Technological areas",
                  "Company size",
                  "Technological maturity",
                  "Capital",
                  "Human resources",
                  "Innovative ecosystem",
                  "Legal framework",
                  "Technological infrastructure"]
    
    for d in dimensions:
        weight = st.slider(d, min_value=0, max_value=100, value=100)
        weights.append(weight)
    total_weight = sum(weights)
    weights_vector = []
    
    for w in range(len(weights)):
        weights_vector.append(weights[w]/total_weight)

    st.markdown("""---""")

#DATABASE IMPORT AND PREPARATION
    
    #Database containing region names
    nuts = pd.read_excel("Regional Info DEF.xlsx")
    nuts2 = nuts[["Region", "Region Name", "Country Name"]]
    
    #Database containing region values
    dfn = pd.read_excel("FINAL Regional Vectors.xlsx")
    regions = dfn["NUTS 2 Code"].tolist()
    
    result = st.button('Recommend me!')
    
 #MATCHMAKING
    def recommendation(input_vector, weights_vector = None):
        
        assert len(input_vector) == 14 #len(input_vector) must always be always 13 (one value for each dimesion)
        idx_yes = [i for i in range(len(input_vector)) if input_vector[i] == 1]
        good_vals = [1] * 7 #the remaining (non-elective parameters) will be considered to have a value of 1 (the greater, the better)
        input_vector.extend(good_vals)

        #Assigning weights of importance to each dimension
        if weights_vector == None:
            weights_vector = [1/8] * 8 
        assert len(weights_vector) == 8 #len(weights_vector) must always be always 8 (1 value for each evaluation block)

        #Weighting the input and master dataframe
        n_areas = sum(input_vector[:8])
        n_matur = sum(input_vector[11:13])

        #Non-weighted input vector and dataframe converted to arrays
        array = np.array(dfn)
        input_array = np.array(input_vector)

        #Getting the complete weights
        complete_weights = [0] * 21

        for i in range(len(weights_vector)):
            if i == 0: #Weight of tech areas
                for j in range(9):
                    if j in idx_yes:
                      complete_weights[j] = weights_vector[0] / n_areas        

            elif i == 1: #Weight of SME/LE
                if input_vector[9] == 1:
                    complete_weights[9] = weights_vector[1]
                    complete_weights[10] = 0
                else:
                    complete_weights[9] = 0
                    complete_weights[10] = weights_vector[1]

            elif i == 2: #Weight of tech maturity
                for j in range(11,14):
                    if j in idx_yes:
                        complete_weights[j] = weights_vector[2] / n_matur 

            elif i == 3: #Weight of capital
                complete_weights[14:17] = [weights_vector[3] / 3] * 3

            elif i == 4: #Weight of hhrr
                complete_weights[17] = weights_vector[4] 

            elif i == 5: #Weight of innovative ecosystem
                complete_weights[18] = weights_vector[5] 

            elif i == 6: #Weight of government
                complete_weights[19] = weights_vector[6]

            elif i == 7: #Weight of tech infrastructure
                complete_weights[20] = weights_vector[7]

        #Weighting
        weights_array = np.array(complete_weights).reshape(1,-1)
        array = array[:,1:]
        weighted_regions = array * weights_array
        weighted_input = (input_array * weights_array)

        #Matchmaking (using cosine distances)
        simil = (1 - distance.cdist(weighted_regions, weighted_input, 'cosine')) * 100 
        match = pd.DataFrame(simil)
        match["Region"] = regions
        match.columns = ["Score", "Region"]
        match = match.sort_values(by = 'Score', ascending=False, ignore_index=True)
        match = pd.merge(match, nuts2, how="inner", on="Region")

        return match

 #LOADING...
    
    if result:
        match = recommendation(input_vector, weights_vector) 
        st.balloons()
    
    #RESULTS!
        st.header("🏆 YOUR LOCATION RECOMMENDATIONS")
        
        # Dataframe showing scores
        st.table(match.head(10))
    
        # Map
        nplot = 10
        topplot = 3
        sel=match.head(nplot).set_index('Region') 

        df = pd.read_excel('nuts2xy.xlsx')

        df_sel = df[df['NUTS_ID'].isin(list(match.head(topplot).Region))]
        df_sel2 = df[df['NUTS_ID'].isin(list(match.head(nplot).Region))]

        st.pydeck_chart(pdk.Deck(
           map_style='mapbox://styles/mapbox/light-v9',
           initial_view_state=pdk.ViewState(
               latitude=46.9,
               longitude=7.5,
               zoom=3,
               pitch=0,
           ),
           layers=[

               pdk.Layer(
                   'ScatterplotLayer',
                   data=df_sel,
                   get_position='[lon, lat]',
                   get_color='[200, 30, 0, 254]',
                   get_radius=90000,
               ),

               pdk.Layer(
                   'ScatterplotLayer',
                   data=df_sel2,
                   get_position='[lon, lat]',
                   get_color='[200, 30, 0, 150]',
                   get_radius=50000,
               ),
           ],
        ))
        st.subheader("To make a new search, just go back to the top and modify your configuration!")

def comparator():
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
    st.subheader("Which regions would you like to compare?")
    reg = st.multiselect("", regions, "ES30")
    
    #RESULTS
    st.table(dfn.loc[reg].T)
    
    #Results interpretation
    st.subheader("How to read the scores obtained:")
    st.write("Standard scores are given in a -1 to 1 scale.")
    st.write(
        """
        - A score of 0 represents the mean score of the regions.
        - A score of -1 represents the region is in the lower 15.9% of the regions. Lower scores correspond to left outliers.
        - A score of 1 represents the region is in the top 15.9% of the regions. Higher scores correspond to right outliers.
        """
    )
    image = Image.open('normalstandard.jpg')
    st.image(image)
    
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
    st.subheader("Region codes and names:")
    st.table(nuts2)
    
page_names_to_funcs = {
    "👩 Introduction": home,
    "🖥️ My apps": main_page,
    "📍 Business location recommender": location_recommendation,
    "🇪🇺 European region comparator": comparator
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()







