import streamlit as st

st.title("點餐機")

ss = st.session_state

if "oders" not in ss:
    ss.oders = []

col1, col2 = st.columns([9, 1])
input_food = col1.text_input("請出入點餐")
if col2.button("加入"):
    ss.oders.append(input_food)
    st.rerun()

st.write("### 購物籃")
for i in range(len(ss.oders)):
    col3, col4 = st.columns([9, 1])
    col3.write(ss.oders[i])
    if col4.button("刪除", key=f"del_{i}"):
        ss.oders.pop(i)
        st.rerun()
