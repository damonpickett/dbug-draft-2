# imports
import openai
import argparse
from dotenv import load_dotenv
import os


# load env variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create CLI argument parser
parser = argparse.ArgumentParser(description="Generate text using GPT-3")
parser.add_argument("text", help="The text to generate a response for")
args = parser.parse_args()

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

response = generate_text(args.text)
print(response)

