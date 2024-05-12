#Importing packages
import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/davis011235/Econ8200/main/df.csv"
data = pd.read_csv(url)

x = st.sidebar.selectbox(
    'x variable',
    ('Year' , 'GTCBSA', 'PEHRUSLT' , ' PEDIPGED' , 'PECYC' , 'PEAFEVER' , 'PEAFNOW' , 'PEERNHRO', 'PEERNLAB', 'HEFAMINC', 'HRNUMHOU')
)
y = st.sidebar.selectbox(
    'y variable',
    ('Year' , 'GTCBSA', 'PEHRUSLT' , ' PEDIPGED' , 'PECYC' , 'PEAFEVER' , 'PEAFNOW' , 'PEERNHRO', 'PEERNLAB', 'HEFAMINC', 'HRNUMHOU')
)
st.scatter_chart(data = data, x = x , y = y)
