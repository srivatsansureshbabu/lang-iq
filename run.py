import asyncio
from pydub import AudioSegment
from pydub.playback import play
import io

async def main():
    # List available voices
    voices = await edge_tts.list_voices()
    tamil_voices = [v["ShortName"] for v in voices if "ta-" in v["ShortName"]]
    print("Available Tamil voices:", tamil_voices)

    if not tamil_voices:
        print("❌ No Tamil voices found.")
        return

    voice = tamil_voices[0]
    print(f"Using voice: {voice}")

    # Generate speech as a stream
    text = "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"
    tts = edge_tts.Communicate(text, voice)

    # Collect audio chunks and play immediately
    audio_bytes = b""
    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]

    # Convert raw audio to playable format
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
    play(audio)

# Run async
asyncio.run(main())
