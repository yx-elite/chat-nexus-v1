import os
import openai
from dotenv import load_dotenv

def load_api_key():
    # Load environment variables
    load_dotenv()
    # Get the API key
    api_key = os.getenv("OPENAI_API_KEY")
    return api_key


def chat_connection(user_prompt):
    # Load the API key
    api_key = load_api_key()
    # Set the API key for OpenAI
    openai.api_key = api_key
    gpt_response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user', 'content':user_prompt}
        ],
        max_tokens=100
    )
    return gpt_response.choices[0].message.content.strip()


