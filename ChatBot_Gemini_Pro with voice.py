import os
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Load API key from environment variable
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Selecting a female voice, adjust index as needed

# Create the model
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def listen_microphone():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)
        return user_input.strip().lower()  # Ensure the input is cleaned and normalized
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(message):
    engine.say(message)
    engine.runAndWait()

def chatbot():
    speak("Hello! I'm listening.")
    chat_session = model.start_chat()

    while True:
        user_input = listen_microphone()

        if not user_input:
            speak("I didn't catch that. Could you repeat?")
            continue
        
        if user_input in ["quit", "exit", "goodbye"]:
            speak("Goodbye!")
            break

        try:
            response = chat_session.send_message(user_input)
            speak(response.text)
            print("Chatbot:", response.text)
        except ValueError as e:
            print(f"Error processing input: {e}")
            speak("I'm sorry, I couldn't understand that.")

if __name__ == "__main__":
    chatbot()
