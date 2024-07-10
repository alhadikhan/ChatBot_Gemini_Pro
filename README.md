# ChatBot_Gemini_Pro
A powerful voice-activated chatbot using Google Generative AI and Google Search API. It listens, responds, and searches the web for you.

# Voice-Activated Chatbot with Google Generative AI and Search Capabilities

This project is an advanced voice-activated chatbot that leverages Google Generative AI and the Google Search API to provide intelligent responses and web search capabilities. The chatbot listens to user input, generates responses using the Google Generative AI model, speaks the responses back, and performs Google searches when requested.

## Features

- **Voice Recognition**: Uses the `speech_recognition` library to capture and process user speech.
- **Text-to-Speech**: Utilizes the `pyttsx3` library to convert text responses into speech, providing a seamless conversational experience.
- **Generative AI Responses**: Employs the Google Generative AI model (`gemini-1.5-pro`) to generate intelligent and context-aware responses.
- **Google Search Integration**: Incorporates the Google Search API to search the web for user queries and present summarized results.

## Setup and Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/voice-activated-chatbot.git
    cd voice-activated-chatbot
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. Then, install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Environment Variables**:
    Create a `.env` file in the root directory of the project and add your API keys:
    ```sh
    GOOGLE_API_KEY=your_google_api_key
    GOOGLE_SEARCH_API_KEY=your_google_search_api_key
    ```

4. **Run the Chatbot**:
    ```sh
    python chatbot.py
    ```

## Usage

- **Starting the Chatbot**:
  Run the chatbot script to start the voice-activated chatbot. The chatbot will greet you and indicate that it's listening.
  
- **Interacting with the Chatbot**:
  Speak naturally to the chatbot. It can understand and respond to a variety of queries. To perform a web search, include the word "search" followed by your query.

- **Exiting the Chatbot**:
  To exit, simply say "quit," "exit," or "goodbye."

## Example Conversation

Chatbot: Hello! I'm listening.
You: What's the weather like today?
Chatbot: I'm sorry, I couldn't understand that. (Example response from AI model)
You: Search latest news on AI
Chatbot: I found these results for latest news on AI: "AI Breakthrough in Machine Learning" - New AI model surpasses previous benchmarks.
You: Goodbye
Chatbot: Goodbye!

## Current Status

The first project involving a basic voice-activated chatbot with generative AI responses is fully completed.
The current project extending the chatbot with Google Search capabilities is still in progress. Further enhancements and features are planned.

## Future Enhancements

- **Improved Natural Language Understanding**: Enhance the chatbot's ability to understand and respond to more complex queries.
- **Context-Aware Conversations**: Implement features to maintain context across multiple interactions.
- **Additional APIs**: Integrate other APIs to provide more comprehensive information and services.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any features, bug fixes, or improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

