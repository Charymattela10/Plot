import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import plotly.express as px

st.header("1. Altair Scatter Plot")
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ["a","b","c","d","e"])
chart = alt.Chart(chart_data).mark_circle().encode(x = "a", y = "b", size = "c",
                                                   tooltip = ["a","b","c","d","e"])
st.altair_chart(chart)

st.header("2. Interacting Charts")

st.subheader("2.1-Line Chart")
df = pd.read_csv(r"C:\Users\Chary Mattela\Desktop\Python\STREAMLIT\lang_data.csv")
lang_list = df.columns.to_list()
lang_choice = st.multiselect("Select your prefered languaga", lang_list)
new_df = df[lang_choice]
st.line_chart(new_df)

st.subheader("2.2-Area Chart")
st.area_chart(new_df)

st.header("3. Data Visualisation using Plotly")
st.subheader("3.1 Displaying the dataset")
df = pd.read_csv(r"C:\Users\Chary Mattela\Desktop\Python\STREAMLIT\tips.csv")
st.dataframe(df.head())

st.subheader("3.2. Pie Charts")
fig = px.pie(df, values = "total_bill", names = "day")
st.plotly_chart(fig)

st.subheader("3.3. Pie Charts with multiple parameters")
fig = px.pie(df, values = "total_bill", names = "day", color_discrete_sequence = px.colors.sequential.RdBu, opacity = 0.75)
st.plotly_chart(fig)




















