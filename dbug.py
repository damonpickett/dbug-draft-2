import argparse
import sys
import openai
from dotenv import load_dotenv
import os
from rich.console import Console
import re


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# This creates a new ArgumentParser object and adds a positional argument called "text" that represents the highlighted text from the terminal.
# The parse_args() method then reads the command-line arguments and returns a namespace object that contains the argument values.
parser = argparse.ArgumentParser()
parser.add_argument("text", help="the highlighted text from the terminal")
args = parser.parse_args()

console = Console()

if sys.version_info < (3, 7):
    console.print("[bold red]Error:[/bold red] DBUG requires Python 3.7 or higher to run.")
    console.print("Please update to a newer version of Python.\n")
    console.print("[bold]Suggestions:[/bold]")
    console.print("- Install the latest version of Python 3 from the official Python website (https://www.python.org/downloads/).")
    console.print("- Use a Python version manager like pyenv to easily switch between multiple versions of Python.\n")
    sys.exit(1)

def get_error_explanation(error_message):
    prompt = (f"Generate an explanation and solution for the following error message:\n\n{error_message}\n\n"
              "Explanation:\nSolution:")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response_text = response.choices[0].text.strip()
    explanation, solution = re.split('Explanation:|Solution:', response_text)
    return (explanation.strip(), solution.strip())

error_message = "[bold red]Error:[/bold red] DBUG requires Python 3.7 or higher to run. Please update to a newer version of Python."
explanation, solution = get_error_explanation(error_message)
print("Explanation:", explanation)
print("Solution:", solution)


