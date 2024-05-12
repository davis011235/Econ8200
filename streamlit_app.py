#Importing packages
import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/davis011235/Econ8200/main/df.csv"
data = pd.read_csv(url)

st.line_chart(data = data, x = "Year", y = "PEHRUSLT")
