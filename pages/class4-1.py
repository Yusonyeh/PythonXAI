import streamlit as st
import os

st.title("圖片元件")

st.image("image/wenby.png", width=300, caption="WENBY")
st.image("image/fox.png", width=300, caption="FOX")

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()
st.write(image_files)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, width=300)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, use_container_width=True)

st.title("下拉選單元件")

selected_image = st.selectbox("選擇圖片", image_files)
st.write("選擇的圖片是：", selected_image)
image_path = image_folder + "/" + selected_image
st.image(image_path, width=500)

import time

st.title("網頁訊息元件")

col1 = st.columns(4)

# success
if col1[0].button("success按鈕"):
    st.success("這是st.success訊息")
    time.sleep(1)
    st.rerun()

# error
if col1[1].button("error按鈕"):
    st.error("這是st.error訊息")
    time.sleep(1)
    st.rerun()

# warning
if col1[2].button("warning按鈕"):
    st.warning("這是st.warning訊息")
    time.sleep(1)
    st.rerun()

# info
if col1[3].button("info按鈕"):
    st.info("這是st.info訊息")
    time.sleep(1)
    st.rerun()
