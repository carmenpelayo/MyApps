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


def main_page():
    st.title("Location Recommendation System for European Businesses in ICT")
    image = Image.open('MatchingProjects.jpg')
    st.image(image)
    st.write('This web was made by Carmen Pelayo Fernandez in 2022')


def page2():
    st.header("🏢 YOUR BUSINESS DIMENSIONS")
    
    #STEP 1: Creating the input vector (14 values)
    input_vector = []

    # DIMENSION 1: Tech areas
    st.subheader('Tech Areas')
    st.write('explain...')
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
    st.write('explain...: Small and Mid-Size Enterprise (SME), Large Enterprise (LE)')
    D2_val = ['Yes', 'No']
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
    st.write('explain...')
    D4_val = ['Integration', 'Development', 'Deep Tech']
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
    st.write('explain...')
    
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

    #RECOMMENDATION
    
    #Loading the dataframe containing the vectors on regional scores
    dfn = pd.read_excel('Regional Vectors.xlsx')
    regions = list(dfn.index)

    #Matchmaking algorithm
    def recommendation(input_vector, weights = None):
        #assert len(input_vector) == 14 #len(input_vector) must always be always 14 (1 value for each dimesion)
        matur_input = input_vector[-3:]
        input_vector.extend([0])
        if input_vector[10] == 1: #The user is a SME
            input_vector[11] = 0
            input_vector[-3:] = matur_input
        else: #The user is a Large Enterprise
            input_vector[11] = 1
            input_vector[-3:] = matur_input
        good_vals = [1] * 9 #the remaining (non-elective parameters) will be considered to have a value of 1 (the greater, the better)
        idx_yes = [i for i in range(len(input_vector)) if input_vector[i] == 1]
        input_vector.extend(good_vals)
        #Assigning weights of importance to each dimension
        if weights == None:
            weights = [1/8] * 8 
        #assert len(weights) == 8 #len(weights_list) must always be always 8 (1 value for each dimesion)
        #Weighting the input and master dataframe
        n_areas = sum(input_vector[:10])
        n_matur = sum(input_vector[12:15])
        #Non-weighted input vector and dataframe converted to arrays
        array = np.array(dfn)[:,1:]
        input_array = np.array(input_vector)
        #Getting the complete weights
        complete_weights = [0] * 24
        for i in range(len(weights)):
            if i == 0: #Weight of tech areas
                for j in range(10):
                    if j in idx_yes:
                        complete_weights[j] = weights[0] / n_areas             
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
                complete_weights[18:20] = [weights[4] / 2] * 2 
            elif i == 5: #Weight of innovative ecosystem
                complete_weights[20:22] = [weights[5] / 2] * 2 
            elif i == 6:
                complete_weights[22] = weights[6]
            elif i == 7:
                complete_weights[23] = weights[7]
        #Weighting
        weights_array = np.array(complete_weights).reshape(1, -1)
        weighted_regions = array * weights_array
        weighted_input = (input_array * weights_array)
        #Matchmaking (using cosine distances)
        distances = (1 - distance.cdist(weighted_regions, weighted_input, 'cosine')) * 100 
        match = pd.DataFrame(distances)
        match["Region"] = regions
        match.columns = ["Score", "Region"]
        match = match.sort_values(by = 'Score', ascending=False, ignore_index=True) #.set_index("Region")
        
        return match
    
    recommendation = recommendation(input_vector, weights_vector) 
    
    #Plotting results
    #best = recommendation.iloc[1:6]
    st.write(recommendation)
#     dfcoord = pd.read_excel('nuts2.xlsx')
#     bestcoord = pd.DataFrame()
#     for i in range(len(best)):
#         reg = best["Region"].iloc[i]
#         lon = dfcoord[dfcoord["NUTS_ID"] == REG]["lon"].iloc[0]
#         lat = dfcoord[dfcoord["NUTS_ID"] == REG]["lat"].iloc[0]
#         regcoord = {"Region": reg, "Lon": lon, "Lat": lat}
#         bestcoord.append(regcoord, ignore_index = True)
#     st.map(bestcoord, zoom=3) 
      

        
def page3():
    st.header("🏆 RECOMMENDATIONS")
    st.sidebar.markdown("🏆 RECOMMENDATIONS")

    # Ejemplo de representación en 'radar'. Habría que poner en r los valores de
    # las dimensiones obtenidas.
    df_radar = pd.DataFrame(dict(
        r=[1, 5, 2, 2, 3],
        theta=['Market areas','Capital Needs','Qualified personnel',
               'Technology Madurity', 'Networking']))
    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig, use_container_width=True)


    
    
    
# #     simil = np.random.rand(len(df)) # aquí habría que aplicar la similitud del coseno
# #     df['similitude'] = simil
# #     df_sel = df.iloc[1:6] # aquí habría que seleccionar los N de mayor similitud
# #     st.subheader('Similar regions:')
# #     st.dataframe(df_sel) # Habría que describir más datos
# #     #st.map(df_sel, zoom=3)



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
                 get_color='[200, 30, 0, 160]',
                 get_radius=90000,
             ),
         ],
     ))

page_names_to_funcs = {
    "Main Page": main_page,
    "Business Analysis": page2,
    "Recommendation": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()








