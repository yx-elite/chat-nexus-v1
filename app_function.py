import os
import openai
from dotenv import load_dotenv


def load_api_base_url():
    # Load environment variables
    load_dotenv()
    # Get the API endpoint
    api_base_url = os.getenv("OPENAI_API_BASE")
    return api_base_url


def load_api_key():
    # Load environment variables
    load_dotenv()
    # Get the API key
    api_key = os.getenv("OPENAI_API_KEY")
    return api_key


def chat_connection(user_prompt, max_token=500, temperature=0.8):
    # Load the API key
    api_key = load_api_key()
    api_base_url = load_api_base_url()
    # Set the API key for OpenAI
    openai.api_key = api_key
    openai.api_base = api_base_url
    gpt_response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user', 'content':user_prompt}
        ],
        max_tokens=max_token,
        temperature=temperature
    )
    # print(gpt_response)
    return gpt_response.choices[0].message.content.strip()


