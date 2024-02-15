
import streamlit as st

st.title("Dog Cat Classification")

uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

def display_image(image_data):
    st.image(image_data, caption=image_data.name, use_column_width=True)

if uploaded_image is not None:
    display_image(uploaded_image)

    abspath = st.write(f"**Image path:** {uploaded_image.name}")

if st.button("Submit"):
    st.success("Prediction: **Dog**")
