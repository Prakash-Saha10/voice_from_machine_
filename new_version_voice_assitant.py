import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Library for speech recognition
import webbrowser  # Allows opening web pages
import datetime  # Handles date and time operations
import pyjokes  # Fetches random jokes
import os  # Provides access to operating system functionalities
import time  # Allows time-related operations like sleep
import random  # Enables working with random elements

# Initialize the text-to-speech engine globally to avoid multiple initializations
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[1].id)  # Set voice (0: Male, 1: Female)
engine.setProperty('rate', 150)  # Set speech speed


def speak_text(text):
    """Convert text to speech and make the assistant speak."""
    engine.say(text)
    engine.runAndWait()


def sptext():
    """Capture and recognize speech from the microphone."""
    recognizer = sr.Recognizer()  # Initialize speech recognizer
    with sr.Microphone() as source:  # Use the system microphone as an audio source
        print("Listening...")  # Indicate that the assistant is listening
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=8)  # Listen for speech with a timeout of 8 seconds
            print("Recognizing...")  # Indicate that recognition is in progress
            data = recognizer.recognize_google(audio)  # Convert speech to text using Google API
            print("You said:", data)  # Print recognized speech
            return data.lower().strip()  # Convert to lowercase and remove extra spaces
        except sr.UnknownValueError:  # Handle unrecognized speech
            print("Could not understand audio")
            speak_text("Sorry, I didn't catch that. Can you say it again?")
        except sr.RequestError:  # Handle internet connectivity issues
            print("Check internet connection")
            speak_text("Please check your internet connection.")
    return ""  # Return an empty string if recognition fails


# The main program starts here
if __name__ == '__main__':
    speak_text("Hello! How can I assist you today?")  # Assistant greeting message

    while True:  # Infinite loop to keep the assistant running
        data1 = sptext()  # Capture user input

        if not data1:  # If no valid input is captured, restart the loop
            continue

        elif "your name" in data1:  # If the user asks for the assistant's name
            speak_text("My name is Peter.")

        elif "how old are you" in data1:  # If the user asks for the assistant's age
            speak_text("I am two years old.")

        elif "time" in data1:  # If the user asks for the current time
            current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get current time in HH:MM AM/PM format
            speak_text(f"The current time is {current_time}")

        elif "youtube" in data1:  # If the user requests to open YouTube
            speak_text("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")  # Open YouTube in the web browser

        elif "web" in data1:  # If the user requests to open the Daraz website
            speak_text("Opening Daraz website")
            webbrowser.open("https://www.daraz.com")  # Open Daraz website

        elif "search" in data1:  # If the user wants to perform a Google search
            speak_text("What do you want to search for?")
            query = sptext()  # Capture the user's search query
            if query:  # If the user provided a search term
                search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"  # Create a search URL
                speak_text(f"Searching for {query} on Google.")
                webbrowser.open(search_url)  # Open the search results

        elif "joke" in data1:  # If the user asks for a joke
            joke = pyjokes.get_joke(language="en")  # Get a random joke in English
            print(joke)  # Print the joke
            speak_text(joke)  # Speak the joke

        elif "play song" in data1:  # If the user requests to play a song
            music_dir = "C:\\Users\\Public\\Music"  # Define the default music directory
            if os.path.exists(music_dir):  # Check if the directory exists
                songs = os.listdir(music_dir)  # Get a list of available songs
                if songs:  # If there are songs in the directory
                    song_to_play = random.choice(songs)  # Pick a random song
                    print(f"Playing: {song_to_play}")  # Display the selected song
                    speak_text(f"Playing {song_to_play}")
                    os.startfile(os.path.join(music_dir, song_to_play))  # Play the selected song
                else:
                    speak_text("No songs found in the directory.")  # Inform the user if no songs are available
            else:
                speak_text("Music folder not found.")  # Inform the user if the folder doesn't exist

        elif "exit" in data1:  # If the user wants to exit the assistant
            speak_text("Are you sure you want to exit?")  # Ask for confirmation
            confirm = sptext()  # Capture user confirmation

            # ✅ Fixed: Now checking if "yes", "sure", or "exit" is present in the response
            if "yes" in confirm or "sure" in confirm or "exit" in confirm:
                speak_text("Thank you! Goodbye.")  # Say farewell
                break  # Exit the loop and stop the program
            else:
                speak_text("Okay, continuing.")  # Continue the program if the user doesn't confirm

        time.sleep(2)  # Pause for 5 seconds before listening again
