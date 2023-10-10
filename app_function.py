import os
import openai
from dotenv import load_dotenv

def load_api_key():
    # Load environment variables
    load_dotenv()
    # Get the API key
    api_key = os.getenv("OPENAI_API_KEY")
    return api_key


def chat_connection():
    # Load the API key
    api_key = load_api_key()
    # Set the API key for OpenAI
    openai.api_key = api_key
    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        engine="text-davinci-003",
        message=[{'role': 'user', 'content': 'Chat with me like a human'}],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()


