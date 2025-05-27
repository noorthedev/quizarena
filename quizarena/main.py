import streamlit as st
from db.db import init_db
from auth.auth import login, register
from game.game_logic import start_game


init_db()

st.set_page_config(page_title="QuizArena", layout="centered")

menu = st.sidebar.selectbox("Menu", ["Login", "Register", "Start Game"])

if menu == "Login":
    login()
elif menu == "Register":
    register()
elif menu == "Start Game":
    start_game()
