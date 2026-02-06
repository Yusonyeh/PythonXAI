import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是 AI 的訊息")

# 範例對話紀錄
history = [
    {"role": "user", "content": "你好，我是使用者"},
    {"role": "assistant", "content": "哈囉！有什麼我可以幫你的嗎？"},
    {"role": "user", "content": "請問 st.chat_message() 怎麼用？"},
    {
        "role": "assistant",
        "content": "st.chat_message() 可以用聊天泡泡方式顯示訊息喔！",
    },
]

# 用迴圈顯示對話紀錄
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
