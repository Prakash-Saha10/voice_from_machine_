🎙️ Voice Assistant Using Python
📌 Project Overview
This is a voice-controlled virtual assistant developed using Python. The assistant can understand voice commands, respond using speech, and perform various useful tasks like telling the time, opening websites, searching the web, telling jokes, and playing local music — all through natural voice interaction.

🔧 Features
🗣️ Speech Recognition
Listens to your voice commands using your microphone and converts them into text using Google Speech Recognition.

🧠 Smart Responses
Replies intelligently to questions like:

“What is your name?”

“How old are you?”

“What time is it?”

🌐 Web Control
Can open websites like:

YouTube

Daraz

Google Search (based on your query)

🎶 Music Playback
Plays a random song from your local music folder.

😂 Fun Mode
Tells you a random joke using the pyjokes library.

🛑 Exit Command
You can exit the assistant by saying "exit" and confirming the prompt.

🧰 Technologies & Libraries Used
Python 🐍

pyttsx3 – Text-to-speech engine

speech_recognition – For capturing and interpreting spoken commands

webbrowser – For opening websites

datetime – To fetch current time

pyjokes – To generate fun jokes

os, random, time – Core Python utilities

💡 How It Works
The assistant starts by greeting you with a voice message.

It then enters a loop, constantly listening for voice input.

Based on recognized commands, it performs appropriate actions.

The assistant continues running until you say "exit" and confirm.

