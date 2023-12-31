import speech_recognition as sr
from gtts import gTTS
import playsound
import datetime
import os
import spacy

# Initialize spaCy NLP
nlp = spacy.load("en_core_web_sm")

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

# Function to recognize voice commands
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("User said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return ""

# Function to perform actions based on voice commands
def process_command(command):
    doc = nlp(command)
    intent = get_intent(doc)
    if intent == "schedule":
        schedule_event(command)
    elif intent == "reminder":
        set_reminder(command)
    elif intent == "query":
        answer_query(command)
    elif intent == "exit":
        exit()
    else:
        speak("I'm not sure how to respond to that.")

# Function to extract the intent from user input
def get_intent(doc):
    # Implement your logic here to determine the intent based on NLU
    # For simplicity, you can use keyword matching or more advanced techniques
    if "schedule" in doc.text:
        return "schedule"
    elif "reminder" in doc.text:
        return "reminder"
    elif "what is" in doc.text:
        return "query"
    elif "exit" in doc.text:
        return "exit"
    else:
        return "unknown"

# Function to schedule an event
def schedule_event(command):
    # Extract event details (date, time, description) from the command
    event_details = extract_event_details(command)
    if event_details:
        date, time, description = event_details
        # Implement your logic here to schedule the event
        # You can use a calendar library or external API for scheduling
        # For now, we'll print the event details as an example
        print(f"Event scheduled for {date} at {time}: {description}")
        speak("Event scheduled.")
    else:
        speak("I couldn't schedule the event. Please provide valid details.")

# Function to extract event details from user input
def extract_event_details(command):
    # Implement your logic here to extract event details
    # You can use regular expressions or spaCy's entity recognition
    # For simplicity, we'll use a placeholder function
    date = "2023-10-01"  # Replace with extracted date
    time = "15:00"       # Replace with extracted time
    description = "Meeting with John"  # Replace with extracted description
    return date, time, description

# Function to set a reminder
def set_reminder(command):
    # Extract reminder details (date, time, message) from the command
    # Implement your logic here
    speak("Reminder set.")

# Function to answer user queries
def answer_query(command):
    # Extract the user's query and provide a response
    # Implement your logic here
    response = "I don't have an answer to that right now."
    speak(response)

# ... (The rest of your code with calendar integration, notification, and personalization)

if __name__ == "__main__":
    while True:
        user_input = recognize_speech()
        if user_input:
            process_command(user_input)