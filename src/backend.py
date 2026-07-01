import requests
import json
from pathlib import Path
import wave
from piper import PiperVoice
import subprocess

# Folder containing this script
BASE = Path(__file__).resolve().parent

# Tamil model
MODEL = BASE.parent / "models" / "piper" / "ta_IN-Valluvar-medium.onnx"

print("Loading model...")
voice = PiperVoice.load(str(MODEL))
print("Model loaded!")


# Store the entire conversation
messages = [
    {
        "role": "system",
        "content": """
        நீங்கள் ஒரு தமிழ் மென்பொருள் பயிற்றுவிப்பாளர்.
        முழுவதும் தமிழிலேயே பதிலளிக்கவும்.
        ஆங்கில எழுத்துகள், விளக்கங்கள், அடைப்புக்குறிப்புகள் அல்லது துணைப் பதிவுகள் எதையும் பயன்படுத்த வேண்டாம்.
        மிகச் சுருக்கமாகவும், ஒரு படி ஒரு படியாகவும் பதிலளிக்கவும்.
        no emoji
        clear all the * in the response             
        """
    }
]

print("=" * 50)
print("        Gemma AI Chatbot")
#   
print("=" * 50)





def speak(text):

    # Create output.wav
    with wave.open("output.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
        print("Done!")
        print("Saved as output.wav")
        subprocess.run(["aplay", "output.wav"])

def gemma_call(user_input):
 

    # Add user message to conversation
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send conversation to Ollama
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma3:4b",
            "messages": messages
        },
        stream=True
    )

    print("\nGemma: ", end="", flush=True)

    assistant_reply = ""

    # Read streamed response
    for line in response.iter_lines():

        if line:

            data = json.loads(line)

            if "message" in data:

                chunk = data["message"]["content"]

                print(chunk, end="", flush=True)

                assistant_reply += chunk
                 # Generation finished
                if data.get("done"):

                    print("\n\nGeneration Complete!")

                    # speak(assistant_reply)

   

    # Save AI response
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    return assistant_reply
