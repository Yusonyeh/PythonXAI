from openai import OpenAI
from dotenv import load_dotenv
import os

# 載入 .env
load_dotenv()

# 建立 client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    user_input = input("你: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後續對話"},
            {"role": "user", "content": user_input},
        ],
    )

    assistant_message = response.choices[0].message.content
    print("AI:", assistant_message)
