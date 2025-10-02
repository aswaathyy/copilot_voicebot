from llama_cpp import Llama

llm = Llama(model_path="models/openchat.gguf", n_ctx=2048)

with open("config/persona_prompt.txt", "r") as f:
    persona = f.read()

def get_response(user_input):
    prompt = f"{persona}\nUser: {user_input}\nCopilot:"
    output = llm(prompt, max_tokens=200)
    return output['choices'][0]['text'].strip()