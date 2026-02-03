import streamlit as st

st.title("排版練習")

coll, col2 = st.columns(2)
if coll.button("氣球按鈕"):
    coll.balloons()
if col2.button("雪花按鈕"):
    col2.snow()

col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("here is col3")
    st.button("按鈕1")
with col4:
    st.write("here is col4")
    st.button("按鈕2")
with col5:
    st.write("here is col5")
    st.button("按鈕3")

numCol = st.number_input("輸入欄位數量", min_value=1, max_value=5, value=3, step=1)
numBotton = st.number_input("輸入按鈕數量", min_value=1, max_value=5, value=3, step=1)
cols = st.columns(numCol)
for i in range(numBotton):
    cols[i % numCol].button(f"按鈕[{i+1}]")

st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.write("你輸入的文字是:" + text)
