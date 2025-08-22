import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
#date and time
date = st.date_input(
    "Date",
    datetime.date(2019, 7, 6))
st.write('The date is:', date)

time = st.time_input('What time is it ', datetime.time(8, 45))
st.write('Time is', time)

pickup_datetime = f"{date} {time}"

#pickup longitude
pickup_longitude = st.number_input('Pickup longitude')
st.write('The pickup longitude number is ', pickup_longitude)

# pickup latitude
pickup_latitude = st.number_input('Pickup latitude')
st.write('The pickup latitude number is ', pickup_latitude)


#dropoff longitude
dropoff_longitude = st.number_input('Dropoff longitude')
st.write('The dropoff longitude number is ',dropoff_longitude)

# dropoff latitude
dropoff_latitude = st.number_input('Dropoff latitude')
st.write('The dropoff latitude number is ', dropoff_latitude)

# passenger count
passenger_count = st.number_input('Passenger count',step=0,format="%i")
st.write('The passenger count number is ', passenger_count)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

#dict parameters API

dico_params = {"pickup_datetime" : [pickup_datetime],
                          "pickup_longitude" : [pickup_longitude],
                          "pickup_latitude" : [pickup_latitude],
                          "dropoff_longitude" : [dropoff_longitude],
                          "dropoff_latitude" : [dropoff_latitude],
                          "passenger_count" : [passenger_count]}


prediction = requests.get(url=url, params=dico_params).json()

# print(prediction)
st.write('The prediction is', prediction['fare'])
