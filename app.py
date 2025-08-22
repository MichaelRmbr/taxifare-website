import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

'''
# 🚕 TaxiFare
'''
'''
📍 Rides Parameters
'''

#date and time
date = st.date_input(
    "Date",
    datetime.date(2019, 7, 6))

time = st.time_input('What time is it ', datetime.time(8, 45))

pickup_datetime = f"{date} {time}"

#pickup longitude
pickup_longitude = st.number_input('Pickup longitude',format="%.6f",value=-73.950655)

# pickup latitude
pickup_latitude = st.number_input('Pickup latitude',format="%.6f", value=40.783282)

#dropoff longitude
dropoff_longitude = st.number_input('Dropoff longitude',format="%.6f",value=-73.984365)

# dropoff latitude
dropoff_latitude = st.number_input('Dropoff latitude',format="%.6f",value=40.769802)

# passenger count
passenger_count = st.number_input('Passenger count',step=0,format="%i",value=1)


url = 'https://taxifare.lewagon.ai/predict'



#dict parameters API
dico_params = {"pickup_datetime" : [pickup_datetime],
                          "pickup_longitude" : [pickup_longitude],
                          "pickup_latitude" : [pickup_latitude],
                          "dropoff_longitude" : [dropoff_longitude],
                          "dropoff_latitude" : [dropoff_latitude],
                          "passenger_count" : [passenger_count]}


prediction = requests.get(url=url, params=dico_params).json()

if st.button('💲Prediction price'):
    st.write('The prediction price is $',round(prediction['fare'],2))



def get_map_data():
    return pd.DataFrame(
        {
            'lat': [dropoff_latitude],
            'lon': [dropoff_longitude]
        }
    )
df = get_map_data()

if st.button('🗺️ Map'):
    st.map(df)
