
import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome")
st.header(f'If You Wnna Drink🍻🥂🥃🍷🥤🍹 So Your Are In Righ Place.')
st.subheader("You can find the Pub 🏪 by selecting the local_authority and use you current latitude🌐 and longitude🌐 to find nearest Pub.")

data = pd.read_csv('data/use_full.csv')

st.subheader(f"Total #{data.shape[0]} Pub in city. ")

st.write(f"Total #{len(set(data.local_authority))} local_authority in city.")

