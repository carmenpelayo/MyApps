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



def main_page():
    st.title("Location Recommendation System for European Businesses in ICT")
    image = Image.open('MatchingProjects.jpg')
    st.image(image)
    st.write('This web was made by Carmen Pelayo Fernandez in 2022')
    


def page2():
    st.header("🏢 YOUR BUSINESS DIMENSIONS ")
    
 #CAPTURING INPUT

    #STEP 1: Creating the selection vector (14 values)
    input_vector = []

    # DIMENSION 1: Tech areas
    st.subheader('Tech Areas')
    st.write('In which technological areas are you interested?')
    areas = ['AI',
             'Big Data',
             'Computation',
             'Cybersecurity',
             'Internet',
             'IoT',
             'Media & Communication',
             'Other',
             'Robotics',
             'Software']
    D1 = st.multiselect("Market area: ", areas, areas)
    # Filling first 10 values of the input_vector 
    for a in areas:
        if a in D1:
            input_vector.append(1)
        else:
            input_vector.append(0)
            
    # DIMENSION 2: Company Size
    st.subheader('Company Size')
    st.write('Are you a small/mid-sized enterprise (SME) or a large enterprise (LE)?')
    D2_val = ['SME', 'LE']
    D2 = st.radio(
         'Is your business a SME?',
         tuple(D2_val), key=2, horizontal=True)
    # Filling index 11 of the input_vector
    if D2 == "Yes":
        input_vector.append(1)
    else:
        input_vector.append(0)
    
    # DIMENSION 3: Technological Maturity
    st.subheader('Technological Madurity')
    st.write('What is your dimension of technological specialization?')
    D4_val = ['Deep Tech', 'Development', 'Integration']
    D4 = st.multiselect(
         'What is your organization working on?', D4_val, 'Deep Tech')
    # Filling indexes 12, 13 and 14 of the input_vector
    for maturity in D4_val:
        if maturity in D4:
            input_vector.append(1)
        else:
            input_vector.append(0)
  

    #STEP 2: Creating the weights vector (8 values)
    st.markdown("""---""")
    weights = []
    st.subheader('Importance of the Dimensions')
    st.write('How important are the following business parameters in your location decision?')
    
    dimensions = ["Technological Areas",
                  "Company Size",
                  "Technological Maturity",
                  "Capital",
                  "Human Resources",
                  "Innovative Ecosystem",
                  "Legal Framework",
                  "Technological Infrastructure"]
    
    for d in dimensions:
        weight = st.slider(d, min_value=0, max_value=100, value=100)
        weights.append(weight)
    total_weight = sum(weights)
    weights_vector = []
    
    
    for w in range(len(weights)):
        weights_vector.append(weights[w]/total_weight)

 #DATABASE IMPORT AND PREPARATION
    
    # Regions
    projects = pd.read_excel('ICT_H2020.xlsx', 'Proyectos')
    projects['NUTS 2 Code'] = projects['NUTS 3 Code'].str[:4]
    regions = list(projects.groupby(by = "NUTS 2 Code").count().reset_index()["NUTS 2 Code"])
    regions = regions[1:]
    df_regions = pd.DataFrame({'NUTS2': regions}) # List of regions (with data)
    nuts2 = pd.read_excel("Regional Info DEF.xlsx")

    # Countries
    countries = nuts2[['Region','Country Name']]
    countries['Code'] = countries.Region.str[:2]
    countries = countries.rename(columns={'Region':'NUTS2', 'Country Name':'Country' }) 
    
    st.header("🗺  YOUR LOCATION RECOMMENDATION 🗺 ")
    
    #Loading the files needed to calculate the recommendation
    #dfn = pd.read_excel('Regional Vectors DEF.xlsx')
    #regions = list(dfn["Unnamed: 0"])
    #countries = pd.read_excel('Regional Info DEF.xlsx')
    
    # Regional Vectors (normalized)
    df = pd.read_excel('Regional Vectors DEF.xlsx')
    df = df.rename(columns={'Unnamed: 0':'NUTS2'})
    df_regvectors = pd.merge(df_regions, df, on='NUTS2', how='left') 
    df_regvectors.fillna(0, inplace = True)
    dfn = np.array(df_regvectors)[:,1:]
    
 #MATCHMAKING
    
    def recommendation(input_vector, weights = None):
        #Matchmaking algorithm
        assert len(input_vector) == 14 #len(input_vector) must always be always 8 (1 value for each dimesion)
        matur_input = input_vector[-3:]
        input_vector.extend([0])

        if input_vector[10] == 1: #The user is a SME
            input_vector[11] = 0
            input_vector[-3:] = matur_input
        else: #The user is a Large Enterprise
            input_vector[11] = 1
            input_vector[-3:] = matur_input

        good_vals = [1] * 8 #the remaining (non-elective parameters) will be considered to have a value of 1 (the greater, the better)
        idx_yes = [i for i in range(len(input_vector)) if input_vector[i] == 1]
        input_vector.extend(good_vals)

        #Assigning weights of importance to each dimension
        if weights == None:
            weights = [1/8] * 8 
        assert len(weights) == 8 #len(weights_list) must always be always 8 (1 value for each dimesion)

        #Weighting the input and master dataframe
        n_areas = sum(input_vector[:10])
        n_matur = sum(input_vector[12:15])

        #Non-weighted input vector and dataframe converted to arrays
        array = np.array(dfn)
        input_array = np.array(input_vector)

        #Getting the complete weights
        complete_weights = [0] * 23

        for i in range(len(weights)):
            if i == 0: #Weight of tech areas
                for j in range(10): #EPC
                    if j in idx_yes:
                        complete_weights[j] = weights[0] / n_areas    
                        #complete_weights[j] = weights[0] / 10      #EPC         
            elif i == 1: #Weight of SME/LE
                if input_vector[10] == 1:
                    complete_weights[10] = weights[1]
                    complete_weights[11] = 0
                else:
                    complete_weights[10] = 0
                    complete_weights[11] = weights[1]
            elif i == 2: #Weight of tech maturity
                for j in range(12,15):
                    if j in idx_yes:
                        complete_weights[j] = weights[2] / n_matur 
            elif i == 3: #Weight of capital
                complete_weights[15:18] = [weights[3] / 3] * 3                                   
            elif i == 4: #Weight of hhrr
                complete_weights[18] = weights[4]
            elif i == 5: #Weight of innovative ecosystem
                complete_weights[19:21] = [weights[5] / 2] * 2 
            elif i == 6:
                complete_weights[21] = weights[6]
            elif i == 7:
                complete_weights[22] = weights[7]

        #Weighting
        weights_array = np.array(complete_weights).reshape(1, -1)
        weighted_regions = array * weights_array
        weighted_input = (input_array * weights_array)

        #Matchmaking (using cosine distances)
        simil = (1 - distance.cdist(weighted_regions, weighted_input, 'cosine')) * 100 
        match = pd.DataFrame(simil)
        match["Region"] = regions
        match.columns = ["Score", "Region"]
        match = match.sort_values(by = 'Score', ascending=False, ignore_index=True)
        match = pd.merge(match, nuts2, how="inner", on="Region")
        match = match.fillna(0)

        return match[["Score","Region","Region Name","Country Name"]] #EPC

    
    match = recommendation(input_vector, weights_vector) 
   
#RESULTS
    st.subheader('Recommended regions:')
    st.dataframe(match.head(nplot))
    
    # Plot
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
    #st.bar_chart(sel.Score)

        
# def page3():
#     st.header("🏆 RECOMMENDATIONS")
#     st.sidebar.markdown("🏆 RECOMMENDATIONS")

#     # Ejemplo de representación en 'radar'. Habría que poner en r los valores de
#     # las dimensiones obtenidas.
#     df_radar = pd.DataFrame(dict(
#         r=[1, 5, 2, 2, 3],
#         theta=['Market areas','Capital Needs','Qualified personnel',
#                'Technology Madurity', 'Networking']))
#     fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
#     st.plotly_chart(fig, use_container_width=True)


#     st.pydeck_chart(pdk.Deck(
#          map_style='mapbox://styles/mapbox/light-v9',
#          initial_view_state=pdk.ViewState(
#              latitude=46.9,
#              longitude=7.5,
#              zoom=3,
#              pitch=0,
#          ),
#          layers=[

#              pdk.Layer(
#                  'ScatterplotLayer',
#                  data=df_sel,
#                  get_position='[lon, lat]',
#                  get_color='[200, 30, 0, 160]',
#                  get_radius=90000,
#              ),
#          ],
#      ))

page_names_to_funcs = {
    "Home": main_page,
    "Find Your Optimal Location": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()







