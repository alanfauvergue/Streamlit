import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot

st.title('Hello corrector, welcome to my application wich deals with car analysis !')

st.write("let's see some data about car from different region")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
df_car


viz_correlation = sns.heatmap(df_car.loc[:,df_weather.columns != "continent"].corr(), center=0, annot = True)

st.pyplot(viz_correlation.figure)

st.write("we can see a strong positive correlation beetween cylinders and weightlbs, hp, cubicinches.")
st.write("there is also a strong negative correlation beetween mpd and weightlbs, cubicinches, cylinders, hp.")
