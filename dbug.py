import argparse
import sys
import openai
from dotenv import load_dotenv
import os
from rich.console import Console


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

def get_error_explanation(highlighted_text):
    prompt = f"Explain this error message: {highlighted_text}"
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024
    )
    return response.choices[0].text

args.text = "NameError: name 'foo' is not defined"

explanation = get_error_explanation(args.text)
console.print(explanation)

# This simply prints the highlighted text to the console.
print("Highlighted text: " + args.text)
