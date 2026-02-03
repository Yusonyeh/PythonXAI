import streamlit as st

st.title("數字金字塔")
height = st.number_input("輸入一個整數1-20", min_value=1, max_value=20, value=5, step=1)
st.write(f"你輸入的數字是: {height}")
for i in range(1, height + 1):
    st.write(str(i) * i)

st.title("箭頭金字塔")
arrow_height = st.number_input(
    "輸入箭頭層數", min_value=1, max_value=10, value=5, step=1
)
st.write("金字塔箭頭:")
a = ""
for i in range(1, arrow_height + 1):
    a = a + (" " * (arrow_height - i) + "*" * (i * 2 - 1) + "\n")
for i in range(arrow_height):
    a = a + (" " * (arrow_height - 1) + "*" + "\n")
st.write(f"```\n\n{a}```")
