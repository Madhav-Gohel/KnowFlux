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
    """
    Generate a response from the OpenRouter API based on the user prompt.
    :param user_prompt: The prompt to send to the OpenRouter API.
    :param model: The model to use for generation.
    :param system_prompt: The system prompt to set the context for the model.
    :return: The generated response from the OpenRouter API.
    """
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
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

