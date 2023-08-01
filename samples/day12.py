import streamlit as st

st.header("st.checkbox")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("You selected ice cream")
if coffee:
    st.write("You selected coffee")
if cola:
    st.write("You selected cola")
