import streamlit as st
import numpy as np
import pandas as pd

st.title('Pokemon Data Visualiser tool')
st.divider()


#Load Data
@st.cache_data
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

#create a dataframe with pokemon data
df = pd.DataFrame(data)

#display the data
st.write(df)
