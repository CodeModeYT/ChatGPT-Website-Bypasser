# ChatGPT-Website-Bypasser <img src="readme/openai.png" align="right" height="100px"/>
IMPORTANT: this project kind of got useless with OpenAI massively increasing the availability of ChatGPT. However, I'd still be happy if you could support this project by giving it a star :)
<hr>



Small side project used to bypass the website of ChatGPT by openAI to be able to use it even when the site iself is down. 
## How does it work?
It fetches the text from the input, generates the response by using the API and prints it out.
## Versions
There are currently two versions of his project available. The [simple version](#simple-version) and the [advanced version](#advanced-version), offering more possibilities.

Just click on the corresponding version to get to a tutorial explaining how to use the program and how to set it up.
<details> 
<!-- add open at the end of the tag to make it pre opened (future) -->
 <summary><h3>Simple version</h3></summary>
 For this version, we're only gonna use the main.py file in the 'Simple' folder.
 
 #### Setup:
 1. Clone the repository
 2. Run ```pip install openai``` in your Terminal
 3. Replace the API key in line 24 with [your own API key](#how-to-create-an-api-key)
 4. Run ```/Simple/main.py```
</details>
<details>
 <summary><h3>Advanced version</h3></summary>
 For the advanced version, we are using the files inside of the 'Advanced' folder. 
 This version offers colors in the console and an option to save the results in a text file (if you got any more suggestions, let me know! Create a pull requests or contact me on Discord: CodeMode#2888). 

 #### Setup:
 1. Clone the repository
 3. ```cd``` to folder you cloned the repo into
 2. Run ```pip install /Advanced/requirements.txt```
 4. Correct the path (marked in the file with comments) to the path you cloned the repo into
 5. Replace the API key in line 42 with [your own API key](#how-to-create-an-api-key)
 6. Run ```/Advanced/advanced.py```
 Information: the saved results will be saved as txt in ```/Advanced/Results/```
</details>

## Improvements and Information
If you have any ideas for improvements or other stuff, feel free to create a pull request.
Remember, this is nothing big, just a very small side project that I quickly coded to use ChatGPT whenever I need it.


As this repo is growing, I'd be very happy if you starred it. Like that, we can reach even more people and inspire them. 
### Please notice:
This project is NOT using the up-to-date version of ChatGPT we can find on the website, as the API wasn't released for it yet (this is soon to come). Instead it uses the API of an 'older version' of ChatGPT.
#
### How to create an API key:
Head over to [the API key management](https://platform.openai.com/account/api-keys), login/sign up, create a new API key and paste it into the file. (Never share your API key with anyone or anything!)
