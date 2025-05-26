import streamlit as st
import time

def countdown_timer(seconds):
    with st.empty():
        for i in range(seconds, 0, -1):
            st.markdown(f"<h4 style='color:#FF5722;'>⏳ Time Left: {i} seconds</h4>", unsafe_allow_html=True)
            time.sleep(1)
        st.markdown("<h4 style='color:red;'>⏰ Time's up!</h4>", unsafe_allow_html=True)
