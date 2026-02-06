import streamlit as st
import base64


def load_openai_api() -> str:
    openai_pi_key = st.secrets["OPENAI_API_KEY"]
    if not openai_pi_key:
        st.error("未找到 OpenAI API Key，請設置環境變數 OPENAI_API_KEY")
        st.stop
    return openai_pi_key


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
