import whisper

model = whisper.load_model("base")

def listen():
    print("Listening...")
    result = model.transcribe("mic")
    return result["text"]