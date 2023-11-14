import streamlit as st
import pandas
from sendingmails import send_email

df = pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_forms"):
    your_email = st.text_input("Your email address")

    opition = st.selectbox("What is your topics?",
                           df["topic"])

    row_message = st.text_area("your message")
    message = f"""\
Subject: New email from {your_email}
From: {your_email}
Topic: {opition}
{row_message}
        """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
