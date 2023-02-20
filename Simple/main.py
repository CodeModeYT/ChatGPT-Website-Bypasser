import openai
import time
import os

# Remove this if you want to
print("""

 _______ _                    _______ ______ _______    ______                   _          _                ______                                          
(_______) |            _     (_______|_____ (_______)  (_____ \                 | |        (_)  _           (____  \                                         
 _      | |__  _____ _| |_    _   ___ _____) )  _ _____ _____) )   _  _  _ _____| |__   ___ _ _| |_ _____    ____)  )_   _ ____  _____  ___  ___ _____  ____ 
| |     |  _ \(____ (_   _)  | | (_  |  ____/  | (_____|_____ (   | || || | ___ |  _ \ /___) (_   _) ___ |  |  __  (| | | |  _ \(____ |/___)/___) ___ |/ ___)
| |_____| | | / ___ | | |_   | |___) | |       | |      _____) )  | || || | ____| |_) )___ | | | |_| ____|  | |__)  ) |_| | |_| / ___ |___ |___ | ____| |    
 \______)_| |_\_____|  \__)   \_____/|_|       |_|     (______/    \_____/|_____)____/(___/|_|  \__)_____)  |______/ \__  |  __/\_____(___/(___/|_____)_|    
                                                                                                                    (____/|_|                                
""")
print("github.com/codemodeyt/")
print('IMPORTANT: Read through the readme file on GitHub first, otherwise this file will NOT work')
print("github.com/CodeModeYT/ChatGPT-Website-Bypasser")
print("---------")
def start():    # Get the user input
    usrinput = input("Write your question and confirm with enter: ")

    # Set up the OpenAI API client
    openai.api_key = "API-key-here"

    # Setting up the model and prompt
    model_engine = "text-davinci-003"
    prompt = usrinput

    # Generating a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    # Print the response
    print("Response from API:")
    print(response)
    print("---------")

while True:
    start()
