from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

from listen import listen_to_microphone
from respond import generate_response
from speak import speak_text

import os
from dotenv import load_dotenv


def get_huggingface_login_token():
    load_dotenv()

    huggingface_token = os.getenv("HUGGINGFACE_LOGIN")

    if huggingface_token is None:
        raise ValueError("HUGGINGFACE_LOGIN token not found. Make sure it's set in the .env file.")

    return huggingface_token


token = get_huggingface_login_token()

login(token)

model_name = "unsloth/Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

model = model.to("cpu")



while True:

    user_speech = listen_to_microphone()

    model_response = generate_response(tokenizer, model, user_speech)

    speak_text(model_response)