from openai import OpenAI
from dotenv import load_dotenv
import os

# 載入金鑰
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 建立對話紀錄清單
messages = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

print("輸入 exit 或 quit 可離開")

while True:
    user_input = input("你: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    # 存使用者訊息
    messages.append({"role": "user", "content": user_input})

    # 傳送全部對話
    response = client.chat.completions.create(model="gpt-5.1", messages=messages)

    # 取得 AI 回答
    assistant_message = response.choices[0].message.content
    print("AI:", assistant_message)

    # 存 AI 回答
    messages.append({"role": "assistant", "content": assistant_message})
