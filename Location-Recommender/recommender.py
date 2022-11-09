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

st.title("Location Recommendation System for Businesses in the European ICT Industry")
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
st.write('**In which technological areas is your entity specialized?**')
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
st.write('**Is your entity a small/mid-sized enterprise (SME) or a large enterprise (LE)?**')
D2_val = ['Small/Mid-sized Enterprise (<= 250 employees)', 'Large Enterprise (>250 employees)']
D2 = st.radio("", tuple(D2_val), key=2, horizontal=True)
# Filling index 10 and 11 of the input_vector
if D2 == "SME":
    input_vector.append(1)
    input_vector.append(0)
else:
    input_vector.append(0)
    input_vector.append(1)

# DIMENSION 3: Technological Maturity
st.write('**Are you researching on new ICT advancements, developing ICTs or integrating technology into products/services?**')
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
st.write('**How important are the following business parameters in your location decision?**')
st.write('A score of 0 corresponds to *not important at all* and a score of 100 corresponds to *completely important*.')

dimensions = ["Presence of a specialized market in the selected technological areas.",
              "Abundance of companies of the same size (SMEs/LEs).",
              "Abundance of companies of the same working nature (research/development/integration).",
              "Availability of capital.",
              "Availability of qualified personnel.",
              "Existance of tech hubs.",
              "Favorable legal framework.",
              "Advanced technical infrastructure."]

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
nuts = pd.read_excel("Location-Recommender/Regional Info DEF.xlsx")
nuts2 = nuts[["Region", "Region Name", "Country Name"]]

#Database containing region values
dfn = pd.read_excel("Location-Recommender/FINAL Regional Vectors.xlsx")
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

    df = pd.read_excel('Location-Recommender/nuts2xy.xlsx')

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
    st.write("To get a new recommendation, just go back to the top and modify your preferences!")

    st.markdown("""---""")
         
    st.write('This program was made by Carmen Pelayo Fernández in 2022.')
