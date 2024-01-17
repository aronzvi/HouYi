from openai import OpenAI
from config import config

client = OpenAI(
    base_url=config["knostic_gw_url"],
    api_key=config["openai_key"],
    default_headers={"x-knostic-api-key": config["knostic_key"]},
)

def completion_with_knostic_gw(text: str, model: str = "gpt-4") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content
