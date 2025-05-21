import streamlit as st
import plotly.express as px

st.title("Mi segunda publicacion")
st.header("Introduccion")
st.write("Esta es la primera que me sale algo.")

fig = px.bar(x=["A","B","c"],
             y=[4,8,6])
st.plotly_chart(fig)