#Importing packages
import streamlit as st
import pandas as pd

data_url = "https://raw.githubusercontent.com/davis011235/Econ8200/main/df.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

data = load_data(data_url)


x = st.sidebar.selectbox(
    'x variable',
    ('Year' , 'GTCBSA', 'PEHRUSLT' , ' PEDIPGED' , 'PECYC' , 'PEAFEVER' , 'PEAFNOW' , 'PEERNHRO', 'PEERNLAB', 'HEFAMINC', 'HRNUMHOU')
)
y = st.sidebar.selectbox(
    'y variable',
    ('None', 'Year' , 'GTCBSA', 'PEHRUSLT' , ' PEDIPGED' , 'PECYC' , 'PEAFEVER' , 'PEAFNOW' , 'PEERNHRO', 'PEERNLAB', 'HEFAMINC', 'HRNUMHOU')
)

#st.scatter_chart(data = data, x = x, y = y)




import plotly.express as px

@st.cache
def load_data():
    return pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")

df = load_data()

st.title("Air Travel Time Series Plot")

st.write("This chart shows the number of air passenger traveled in each month from 1949 to 1960")

fig = px.line(df, x="Month", y="Passengers", title="Air Passenger Travel")

st.plotly_chart(fig)
