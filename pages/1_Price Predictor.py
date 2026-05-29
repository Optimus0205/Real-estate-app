import gzip

import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Viz Demo')

st.title('Price Predictor :')

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with gzip.open('pipeline.pkl.gz','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs :')

#property_type
property_type=st.selectbox('Property Type :',['flat','house'])

#sector
sector=st.selectbox('Sector :',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom :',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms :',sorted(df['bathroom'].unique().tolist())))

balcony=st.selectbox('Balconies :',sorted(df['balcony'].unique().tolist()))

agePossession=st.selectbox('Property Age :',sorted(df['agePossession'].unique().tolist()))

built_up_area=float(st.number_input('Built Up Area :'))

servant_room = st.selectbox(
    'Servant Room :',
    options=[0.0, 1.0],
    format_func=lambda x: 'No' if x == 0.0 else 'Yes'
)

store_room = st.selectbox(
    'Store Room :',
    options=[0.0, 1.0],
    format_func=lambda x: 'No' if x == 0.0 else 'Yes'
)

furnishing_type=st.selectbox('Furnishing Type :',sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category :',sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category :',sorted(df['floor_category'].unique().tolist()))




if st.button('Predict'):

    #form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, agePossession, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)


    #predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.17694
    high = base_price + 0.17694

    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low, 2), round(high, 2)))