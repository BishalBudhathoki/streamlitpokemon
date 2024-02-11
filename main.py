import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
from annotated_text import annotated_text

colours = {
	'normal': '#A8A77A',
	'water': '#6390F0',
	'fire': '#EE8130',
	'electric': '#F7D02C',
	'grass': '#7AC74C',
	'fighting': '#C22E28',
	'ice': '#96D9D6',
	'poison': '#A33EA1',
	'ground': '#E2BF65',
	'flying': '#A98FF3',
	'psychic': '#F95587',
	'bug': '#A6B91A',
	'rock': '#B6A136',
	'ghost': '#735797',
	'dragon': '#6F35FC',
	'dark': '#705746',
	'steel': '#B7B7CE',
	'fairy': '#D685AD',
}

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
    st.image(pokemon_data.get('sprites').get('front_default'))
    st.write('Pokemon weight:', pokemon_data.get('weight'))
    pokemon_type = pokemon_data.get('types')[0].get('type').get('name')
    annotated_text(
        (f'Pokemon Type: {pokemon_type}',"", colours[pokemon_type]),
    )
    



