import streamlit as st

# streamlit run main.py

st.title("數字輸入練習")
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=1)
st.write(f"你輸入的數字是: {number}")

st.title("成績等第判斷")
score = st.number_input("請輸入成績", min_value=0, max_value=100, value=0, step=1)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
st.write(f"你的成績等第是: {grade}")

st.title("氣球按鈕")
if st.button("click me", key="balloon"):
    st.balloons()

st.title("雪花按鈕")
if st.button("按我", key="snow"):
    st.snow()
