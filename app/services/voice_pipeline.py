from pathlib import Path
from uuid import uuid4

from google.genai import types
from app.services.gemini_client import (
    client,
    LLM_MODEL,
    TRANSCRIPTION_MODEL,
    TTS_MODEL,
    TTS_VOICE,
)

AUDIO_DIR = Path("data/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

SYSTEM_PROMPT = (
    "You are a helpful AI voice assistant for college students. "
    "Answer clearly and naturally. Keep responses concise enough to be comfortable when spoken aloud. "
    "Avoid unnecessary markdown and tables."
)


def transcribe_audio(audio_path: Path) -> str:
    audio_part = types.Part.from_bytes(
        data=audio_path.read_bytes(),
        mime_type="audio/webm",
    )

    response = client.models.generate_content(
        model=TRANSCRIPTION_MODEL,
        contents=[
            audio_part,
            "Transcribe the speech accurately. Return only the spoken words.",
        ],
    )

    if not response.text:
        raise RuntimeError("Gemini could not transcribe the audio.")

    return response.text.strip()


def answer_from_text(user_text: str) -> str:
    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=user_text,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
    )

    if not response.text:
        raise RuntimeError("Gemini could not generate an answer.")

    return response.text.strip()


def generate_speech(text: str) -> Path:
    response = client.models.generate_content(
        model=TTS_MODEL,
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=TTS_VOICE
                    )
                )
            ),
        ),
    )

    audio_data = response.candidates[0].content.parts[0].inline_data.data

    output = AUDIO_DIR / f"response_{uuid4().hex}.wav"
    output.write_bytes(audio_data)

    return output
