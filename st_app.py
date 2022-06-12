# -*- coding: utf-8 -*-

# import module
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
from PIL import Image


def main_page():
    st.title("Location Recommendation System for European Businesses in ICT")
    image = Image.open('MatchingProjects.jpg')
    st.image(image)
    #st.markdown("🇪🇺 Main page ")
    st.write('explain...DIMENSIONS')
    #st.sidebar.markdown("🇪🇺 Main page")

def page2():
    st.header("🏢 YOUR BUSINESS DIMENSIONS")
    #st.sidebar.markdown("🏢 YOUR BUSINESS DIMENSIONS")
    
    #STEP 1: Creating the input vector
    input_vector = []

    
    # DIMENSION 1: Tech areas
    st.subheader('Tech Areas')
    st.write('explain...')
    areas = ['AI',
             'Big Data',
             'Computation',
             'Cybersecurity',
             'Innovation',
             'Internet',
             'IoT',
             'Media & Communication',
             'Other',
             'Robotics',
             'SME',
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
  
    
    
#OTHER ELECTIVES
#     st.subheader('Capital Needs')
#     st.write('explain...')
#     D2_val = ['Low', 'High']
#     D2 = st.radio(
#          'Select your value in this dimension',
#          tuple(D2_val),key=2, horizontal=True)

#     st.subheader('Qualified personnel')
#     st.write('explain...')
#     D3_val=['Low', 'High/Engineers']
#     D3 = st.select_slider(
#          'Select desired qualification for your employees',key=3,
#          options=D3_val)

#     st.subheader('Networking')
#     st.write('explain...')
#     D5_val = ['Low', 'High']
#     D5 = st.select_slider(
#          'Select your value in this dimension',key=5,
#          options=D5_val)

    # Complete the bussiness vector (others)
#     vals = np.array(D2_val + D3_val + D4_val + D5_val)
#     sels = np.array([D2, D2, D3, D3, D4, D4, D4, D5, D5])
#     business2 = ( sels == vals)

#     st.markdown("""---""")
#     st.subheader('Importance')
#     st.write('Mark business dimensions to be taken int account to recommend a location')

#     D1_mask = st.checkbox('Market areas', value = True)
#     D2_mask = st.checkbox('Capital Needs', value = True)
#     D3_mask = st.checkbox('Qualified personnel', value = True)
#     D4_mask = st.checkbox('Technology Madurity', value = True)
#     D5_mask = st.checkbox('Networking', value = True)

#     st.subheader('Your business dimensions:')
#     business = np.append(business, business2).reshape((1,-1)) # Vector booleano
#     # Para operar con el como 'float' hay que multiplicarlo por 1.0
#     # Aqui lo saca como booleano. Se podría sacar también como números
#     st.write(business)

    st.markdown("""---""")

    
    weights_vector = []
    st.subheader('Importance of the Dimensions (0-100')
    st.write('explain...')
    
    dimensions = ["Technological Areas",
                  "Company Size",
                  "Technological Maturity",
                  "Capital",
                  "Human Resources"
                  "Innovative Ecosystem",
                  "Legal Framework",
                  "Technological Infrastructure"]
    
    for d in dimensions:
        weight = st.slider(d, min_value=0, max_value=100, value=100)
        weights_vector.append(weight)
    
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)
#     D1_weight = st.slider("Tech Areas", min_value=0, max_value=100, value=100)



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



    df = pd.read_excel('nuts2xy.xlsx')
    simil = np.random.rand(len(df)) # aquí habría que aplicar la similitud del coseno
    df['similitude'] = simil
    df_sel = df.iloc[1:6] # aquí habría que seleccionar los N de mayor similitud
    st.subheader('Similar regions:')
    st.dataframe(df_sel) # Habría que describir más datos
    #st.map(df_sel, zoom=3)



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








