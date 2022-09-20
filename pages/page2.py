import streamlit as st
import pandas as pd 
import numpy as np

df = pd.read_csv('data/use_full.csv')



chechk = st.checkbox('Search by postcode')

if chechk:
    bar_by_postcode = set(df.postcode)
    postcode = st.selectbox("select the postcode", bar_by_postcode)
    show_by_post= df[['name', 'address','postcode']]
    st.dataframe(show_by_post[show_by_post['postcode']==postcode])
    data = df[show_by_post['postcode']==postcode]
    st.header('map')
    st.map(data)
else:
    total_local_authority = set(df.local_authority)
    #select_box for local_authority
    st.write(f'total local Authority {len(total_local_authority)}')
    option = st.selectbox('Local_Authority',total_local_authority )

    # bar_by_authority = data['local_authority'].value_counts()["Leeds"]
    st.write(f"Total #{df['local_authority'].value_counts()[option]}  Pub in {option}")
    show_by_post= df[['name', 'address','local_authority']]
    st.dataframe(show_by_post[show_by_post['local_authority']==option])
    data = df[show_by_post['local_authority']==option]
    st.header('map')
    st.map(data)
