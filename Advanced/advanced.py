# IMPORTANT:
# This is only the first version of the advanced code, the code in this version is not clean and NOT FINISHED yet!
import openai
import os
from colorama import Fore
from datetime import datetime

# Remove this if you want to
print(Fore.BLUE + "ChatGPT website bypasser - advanced version!")
print(Fore.RED + 'IMPORTANT: Read through the readme file on GitHub first and only run this file AFTER you ran setup.py!')
print(Fore.WHITE + "github.com/codemodeyt/chatgpt-website-bypasser")


def generate():    # Get the user input
    usrinput = input("Write your question and confirm with enter: ")

    # Set up the OpenAI API client
    openai.api_key = "API-key-here"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = usrinput

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    # Printing it out
    print("Response from API:")
    print(response)
    print("---------")
    #Create the filename
    now = datetime.now()
    currenttime = now.strftime("%d.%m.%Y %H.%M.%S")
    filename = f"ChatGPT at {currenttime}"
    results_path = f'D:\Path\to\project\Advanced\Results\{filename}.txt'
    # Creating and riting the file
    with open(results_path, 'w') as f:
        f.write(f"Result from the API: {response}")

#Running the function
generate()