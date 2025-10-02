from voice.speech_to_text import listen
from llm.local_llm import get_response
from voice.text_to_speech import speak

while True:
    query = listen()
    reply = get_response(query)
    speak(reply)