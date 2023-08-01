import streamlit as st

st.header("st.selectbox")

option = st.selectbox(
    "What is your favorite color?",
    ("Blue", "Green", "Red", "Pink", "Yellow", "Orange", "Purple", "Brown", "Gray", "Black", "White"),
)

st.write("You selected: ", option)
