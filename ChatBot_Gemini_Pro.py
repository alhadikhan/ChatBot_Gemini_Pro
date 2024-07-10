import os
import google.generativeai as genai

# Load API key from environment variable
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

genai.configure(api_key=api_key)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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

def chatbot():
    chat_session = model.start_chat()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "goodbye"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_session.send_message(user_input)
        print("Chatbot:", response.text)

if __name__ == "__main__":
    chatbot()
