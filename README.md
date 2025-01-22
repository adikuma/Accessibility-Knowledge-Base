# Accessibility-Knowledge-Base
A simple Streamlit application to test and demonstrate the functionality of our RAG (Retrieval-Augmented Generation) API.

## Overview
This application provides a chat interface for querying an accessibility knowledge base. It connects to a RAG API endpoint that retrieves and generates responses based on the user's questions.

## Features
- **Chat Interface**: User-friendly chat-style interaction
- **Real-time Responses**: Connects to the RAG API for instant answers
- **Conversation History**: Maintains context across multiple questions
- **Error Handling**: Gracefully handles API errors and timeouts

## Setup
### Prerequisites
- Python 3.8+
- Streamlit
- Requests

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/accessibility-chat.git
   cd accessibility-chat
   ```

2. Install dependencies:
   ```bash
   pip install streamlit requests
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

## Usage

1. Enter your question in the chat input at the bottom of the screen
2. The application will:
   - Show a "Searching documents..." spinner while processing
   - Display the API response in the chat window
   - Maintain conversation history

## API Details

The application connects to the following API endpoint:

- **URL**: `https://multi-document-agents.onrender.com/query`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "text": "Your question here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "Generated answer"
  }
  ```

## Customization

To modify the API endpoint or add features:

1. Edit `app.py`:
   - Change the API URL
   - Add custom headers or parameters
   - Modify the UI elements

2. Add environment variables for configuration:
   ```python
   import os
   API_URL = os.getenv("API_URL", "https://multi-document-agents.onrender.com/query")
   ```
4. Customization tips
5. Contribution guidelines

You can place this in your project root as `README.md`. It will help others understand and use your application effectively.
