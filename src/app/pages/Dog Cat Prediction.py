
import streamlit as st

st.title("Dog Cat Classification")

image = st.file_uploader("Upload File", type=["png", "jpg"])
