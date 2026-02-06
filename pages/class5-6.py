import openai
import streamlit as st

# 取得 session_state
ss = st.session_state

# 初始化
if "system_message" not in ss:
    ss.system_message = "請用繁體中文進行後續對話"

if "model" not in ss:
    ss.model = "gpt-5.1-chat-latest"

if "history" not in ss:
    ss.history = []

# 版面：系統訊息、模型、清除聊天
col1, col2, col3 = st.columns([4, 2, 1])

with col1:
    # 修改系統訊息（AI角色或規則）
    ss.system_message = st.text_input("系統訊息", ss.system_message)

with col2:
    # 選擇模型
    ss.model = st.selectbox(
        "模型",
        [
            "gpt-5.1-chat-latest",
            "gpt-5.1",
            "gpt-5",
        ],
    )

with col3:
    # 清除聊天記錄
    if st.button("🗑️ 清除聊天"):
        ss.history = []
        st.rerun()

for message in ss.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])

prompt = st.chat_input("請輸入你的對話內容")

if prompt:
    ss.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model=ss.model,
        messages=[{"role": "system", "content": ss.system_message}] + ss.history,
    )

    assistant_message = response.choices[0].message.content
    ss.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
