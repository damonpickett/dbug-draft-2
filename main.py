# imports
import openai
import argparse
from dotenv import load_dotenv
import os
from . import generate_text


# load env variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# API Call
def generate_text(text):
    prompt = text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Create CLI argument parser, run generate_text function
def main():
    parser = argparse.ArgumentParser(description="Generate text using GPT-3")
    parser.add_argument("text", help="The text to generate a response for")
    args = parser.parse_args()
    response = generate_text(args.text)
    print(response)



