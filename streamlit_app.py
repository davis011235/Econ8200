#Importing packages
import streamlit as st
import pandas as pd

url = "url = "https://raw.githubusercontent.com/davis011235/Econ8200/main/df.csv?token=GHSAT0AAAAAACRMRKOZ62D2RPU3CQ3IO4DKZSAC3WA""
data = pd.read_csv(url)

st.write(data)
