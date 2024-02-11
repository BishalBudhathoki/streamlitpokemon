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

# get a random pokedex number
random_number = str(np.random.randint(1, 151))
random_number_2 = str(np.random.randint(1, 151))
st.write(random_number)
# fetch name of that random pokemon
def get_random_pokemon_name() -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon-species/'+random_number
        response = requests.get(url)
        data = response.json()
        # st.write(data)
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data.get('name')

# fetch name of that random pokemon
def get_random_pokemon_name_2() -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon-species/'+random_number_2
        response = requests.get(url)
        data = response.json()
        # st.write(data)
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data.get('name')


def get_pokemon_data(pokemon_name) -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon_name
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

pokemon_name = get_random_pokemon_name()
pokemon_name_2 = get_random_pokemon_name_2()

pokemon_data = get_pokemon_data(pokemon_name)
pokemon_data_2 = get_pokemon_data(pokemon_name_2)

if pokemon_data and pokemon_data_2:
    col1, col2 = st.columns(2)

    with col1:
        st.header(pokemon_data.get('name').capitalize())
        st.image(pokemon_data.get('sprites').get('front_default'))
        st.write('Pokemon weight:', pokemon_data.get('weight'))
        pokemon_type = pokemon_data.get('types')[0].get('type').get('name')
        annotated_text(
            (f'Pokemon Type: {pokemon_type}',"", colours[pokemon_type]),
        )

    with col2:
        st.header(pokemon_data_2.get('name').capitalize())
        st.image(pokemon_data_2.get('sprites').get('front_default'))
        st.write('Pokemon weight:', pokemon_data_2.get('weight'))
        pokemon_type = pokemon_data_2.get('types')[0].get('type').get('name')
        annotated_text(
            (f'Pokemon Type: {pokemon_type}',"", colours[pokemon_type]),
        )
    



