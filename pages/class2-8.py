import streamlit as st

ss = st.session_state

st.title("Session State 範例")

if "ans" not in ss:
    ss.ans = 0

if st.button("點我+1"):
    ss.ans += 1
    st.rerun()

st.write("ans=", ss.ans)
