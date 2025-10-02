# 🎙️ Copilot Voice Bot (Local, No API Key)

A fully local voice bot that mimics Microsoft Copilot’s personality—warm, intuitive, and insightful. It uses open-source tools for speech recognition, local LLM inference, and text-to-speech, with no need for an OpenAI API key.

---

##  Features

-  Voice input via Whisper or SpeechRecognition
-  Local LLM responses using `llama-cpp-python` (GGUF models like OpenChat)
-  Voice output via `pyttsx3`
-  Modular structure for easy customization
-  Runs entirely offline—no API key required

---

##  Project Structure

copilot_local_bot/ │ ├── main.py                     # Entry point ├── llm/ │   └── local_llm.py            # Loads and queries local GGUF model ├── voice/ │   ├── speech_to_text.py       # Converts speech to text │   └── text_to_speech.py       # Converts text to speech ├── config/ │   └── persona_prompt.txt      # Defines Copilot’s personality ├── models/ │   └── openchat.gguf           # Downloaded GGUF model (not tracked in Git) ├── requirements.txt            # Python dependencies ├── README.md                   # You’re reading it! └── .env                        # Optional: for paths or config

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/copilot_local_bot.git
cd copilot_local_bot