from gtts import gTTS
import os

def generate_hindi_audio(text, filename="hindi_summary.mp3"):
    tts = gTTS(text=text, lang='hi')  # 'hi' for Hindi language
    file_path = os.path.join("static", filename)
    tts.save(file_path)
    return file_path
