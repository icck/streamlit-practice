import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# streamlit run streamlit_app.py

st.header("this is header")
st.subheader("A subheader with _italics_ :blue[colors] and emojis :sunglasses:")


st.write("hello *world!* emoji")

st.write(1234)

df = pd.DataFrame(
    {
        "first colmun": [1, 2, 3, 4],
        "second colmun": [10, 20, 30, 40],
    }
)

st.write(df)
st.divider()  # 👈 Draws a horizontal rule

st.write("Below is a DataFrame:", df, "Above is a dataframe.")

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = alt.Chart(df2).mark_circle().encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
st.write(c)
