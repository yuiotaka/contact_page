import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book
"""
st.write(content)

st.subheader("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.write(row["first name"], row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.write(row["first name"], row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[9:12].iterrows():
        st.write(row["first name"], row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])