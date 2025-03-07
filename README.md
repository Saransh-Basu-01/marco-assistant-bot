# Marco - AI Voice Assistant

## Overview
Marco is a voice-activated AI assistant built with Python. It can open websites, play music from a predefined library, answer questions using OpenAI's ChatGPT API, and respond to voice commands.

## Features
- Voice recognition using `speech_recognition`.
- Text-to-speech functionality using `pyttsx3`.
- Open websites like Google, YouTube, LinkedIn, and Facebook.
- Fetch answers from OpenAI's ChatGPT API.
- Play music from a predefined `music_library`.
- Shutdown on command.

## Installation
### Prerequisites
Ensure you have Python installed (preferably Python 3.8+).

### Required Libraries
Install the dependencies using pip:
```sh
pip install speechrecognition pyttsx3 openai python-dotenv
```

### Setting Up OpenAI API Key
1. Create an `.env` file in the project directory.
2. Add the following line with your OpenAI API key:
   ```sh
   OPENAI_API_KEY=your-api-key
   ```

## Usage
Run the script using:
```sh
python script.py
```
Marco listens for the wake word **"Marco"** and responds with **"Yes boss, I'm listening."**. After that, you can give it voice commands.

### Available Commands
- "Open Google" - Opens Google in a web browser.
- "Open YouTube" - Opens YouTube.
- "Open Facebook" - Opens Facebook.
- "Open LinkedIn" - Opens LinkedIn.
- "Play [song name]" - Plays a song from the `music_library`.
- "What is [query]" or "Explain [query]" - Fetches answers from OpenAI.
- "Shutdown" or "Exit" - Terminates the assistant.

## Error Handling
- If the speech recognition service fails, Marco will notify the user.
- If an unknown command is received, Marco will prompt the user to try again.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features!


