import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("Hello! I'm Soul, your personal journaling chatbot. Ask me anything! I have access to all the notes you upload into the Notes page.")

st.chat_input("Say something")