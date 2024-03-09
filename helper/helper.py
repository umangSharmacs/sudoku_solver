import streamlit as st
import time

def progress_bar(text: str):
    my_bar = st.progress(0, text=text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=text)