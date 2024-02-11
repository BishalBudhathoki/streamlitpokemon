import streamlit as st
import numpy as np
import pandas as pd
import requests
import json

st.title('Pokemon Data Visualiser tool')
st.divider()


# #Load Data
# @st.cache_data
# def load_data():
#     data = pd.read_csv('pokemon.csv')
#     return data

# data = load_data()

# #create a dataframe with pokemon data
# df = pd.DataFrame(data)

# #display the data
# st.dataframe(df)

def get_pokemon_data() -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/ditto'
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

pokemon_data = get_pokemon_data()

if pokemon_data:
    st.header(pokemon_data.get('name').capitalize())
    st.subheader(pokemon_data.get('weight'))
    st.image(pokemon_data.get('sprites').get('front_default'))



