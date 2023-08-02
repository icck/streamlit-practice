import streamlit as st
import pandas as pd

st.title('st.file_uploader()')

st.subheader("Input CSV")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.subheader("Descriptive Statistics")
    st.write(df.describe())
else:
    st.info("Awaiting CSV file to be uploaded.")
