from calendar import c
import streamlit as st

uploaded_file = st.file_uploader("上傳照片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="已上傳的照片", width=300)
