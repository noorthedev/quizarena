import streamlit as st
from db.db import get_user, add_user

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user(username, password)
        if user:
            st.session_state["user"] = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

def register():
    st.title("Register")
    username = st.text_input("Choose username")
    password = st.text_input("Choose password", type="password")
    if st.button("Register"):
        if add_user(username, password):
            st.success("Registered! Please login.")
        else:
            st.warning("User already exists.")
