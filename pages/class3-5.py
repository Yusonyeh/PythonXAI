import streamlit as st
import random
import time

ss = st.session_state

if "target" not in ss:
    ss.target = random.randint(0, 100)

if "min_val" not in ss:
    ss.min_val = 0

if "max_val" not in ss:
    ss.max_val = 100

st.title("猜數字遊戲")

num = st.number_input(
    f"請輸入{ss.min_val} 到 {ss.max_val}之間的正數:",
    min_value=ss.min_val,
    max_value=ss.max_val,
    step=1,
)

if st.button("提交答案"):
    if num < ss.target:
        st.success("太小了")
        ss.min_val = num + 1
    elif num > ss.target:
        st.success("太大了")
        ss.max_val = num - 1
    else:
        st.success("恭喜你猜對了!")
        st.balloons()
        # Reset the game
        ss.target = random.randint(0, 100)
        ss.min_val = 0
        ss.max_val = 100
    time.sleep(1)
    st.rerun()
