from openai import OpenAI
from config import config

client = OpenAI(
    api_key=config["openai_key"]
)

def completion_with_chatgpt(text: str, model: str = "gpt-4") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content

