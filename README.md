## LLMs Meet Speech – Gemini AI Voice Assistant

A voice-enabled AI assistant built with **FastAPI and Google Gemini**. It accepts text or voice input, generates AI responses, and converts responses into speech.

## Features

- Text-based AI conversations
- Voice recording and audio input
- Speech-to-text transcription using Gemini
- AI-generated responses using Gemini
- Text-to-speech audio generation
- FastAPI backend with API documentation

## Tech Stack

- Python
- FastAPI
- Google Gemini API (`google-genai`)
- HTML, CSS, JavaScript
- Uvicorn

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/tanvimathnikar/LLMs-Meet-Speech.git
cd LLMs-Meet-Speech
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your `.env` file or share your API key publicly.

### 5. Start the application

```bash
uvicorn app.main:app --reload
```

Open the application at:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/api/text` | Text-based interaction |
| `/api/voice` | Voice-based interaction |
| `/api/audio/{filename}` | Retrieve generated audio |

## Acknowledgement

This project builds upon the original [LLMs Meet Speech](https://github.com/thenitinsingh/LLMs-Meet-Speech) repository, with modifications including migration to Google's Gemini API.

## Future Improvements

- Improved error handling
- Better conversation history
- Deployment and production optimization
- Enhanced user interface
