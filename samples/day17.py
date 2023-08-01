import streamlit as st

st.title("st.secrets demo")

st.write(st.secrets["db_username"])
