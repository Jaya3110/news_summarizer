from gtts import gTTS
import os

try:
    text = "Testing Google Text to Speech API"
    tts = gTTS(text=text, lang='hi')
    tts.save("test_audio.mp3")
    print("✅ Audio generated successfully!")
    os.system("start test_audio.mp3")  # Opens audio file on Windows
except Exception as e:
    print(f"❌ Error: {e}")
