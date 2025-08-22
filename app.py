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
pickup_longitude = st.number_input('Pickup longitude')

# pickup latitude
pickup_latitude = st.number_input('Pickup latitude')

#dropoff longitude
dropoff_longitude = st.number_input('Dropoff longitude')

# dropoff latitude
dropoff_latitude = st.number_input('Dropoff latitude')

# passenger count
passenger_count = st.number_input('Passenger count',step=0,format="%i")


url = 'https://taxifare.lewagon.ai/predict'


def get_map_data():
    return pd.DataFrame(
        {
            'lat': [dropoff_latitude],
            'lon': [dropoff_longitude]
        }
    )
df = get_map_data()
st.map(df)


#dict parameters API
dico_params = {"pickup_datetime" : [pickup_datetime],
                          "pickup_longitude" : [pickup_longitude],
                          "pickup_latitude" : [pickup_latitude],
                          "dropoff_longitude" : [dropoff_longitude],
                          "dropoff_latitude" : [dropoff_latitude],
                          "passenger_count" : [passenger_count]}


prediction = requests.get(url=url, params=dico_params).json()

st.write('The prediction is $', round(prediction['fare'],2))
