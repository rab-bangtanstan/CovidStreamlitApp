import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go


# Title
st.title("COVID-19 Data Visualization")

# Sidebar
st.sidebar.header("Options")

# Function to load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df = pd.read_csv(url)
    return df

def process_data(data):
    data_long = data.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"],
                          var_name="Date", value_name="Confirmed")
    data_long["Date"] = pd.to_datetime(data_long["Date"])
    return data_long


# Function to select country
def select_country(data):
    return st.sidebar.selectbox("Select a country", data["Country/Region"].unique())

# Function to filter data by country
def filter_data_by_country(data_long, country):
    return data_long[data_long["Country/Region"] == country]

# Function to plot 3D scatter plot
def plot_3d_scatter(data, country):
    fig = px.scatter_3d(data, x='Date', y='Lat', z='Long', color='Confirmed',
                        title=f"3D Scatter Plot of COVID-19 Cases in {country}")
    st.plotly_chart(fig)

# Function to plot time series
def plot_time_series(data, country):
    fig2 = px.line(data, x="Date", y="Confirmed", title=f"COVID-19 Cases Over Time in {country}")
    st.plotly_chart(fig2)


def main():
    var =st.sidebar.checkbox("Show raw data")
    # var1 = st.sidebar.checkbox("Show procssed data")
    # st.write(var)
    data = load_data()
    if var:
        st.write(data)
    else:
        st.write('Processed Data:')
        processed_data = process_data(data)
        st.write(processed_data)

    country = select_country(data)
    processed_data = process_data(data)
    country_data = filter_data_by_country(processed_data, country)
    plot_3d_scatter(country_data, country)
    plot_time_series(country_data, country)







main()






