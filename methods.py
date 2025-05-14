from openai import OpenAI
import os
from dotenv import load_dotenv
# Set the OpenRouter API key as an environment variable
load_dotenv()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate(user_prompt, model="cognitivecomputations/dolphin3.0-mistral-24b:free", system_prompt="You are a helpful assistant."):
    completion = client.chat.completions.create(
        extra_body={},
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    return completion.choices[0].message.content

