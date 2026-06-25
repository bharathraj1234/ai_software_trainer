import requests
import json

# Store the entire conversation
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Reply in plain text without markdown."
    }
]

print("=" * 50)
print("        Gemma AI Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    # Get user input
    user_input = input("\nYou: how can i help you ")

    # Exit condition
    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    # Add user message to conversation
    messages.append(
        {
            "role": "user",
            "content": """
                        You are an AI Software Trainer.
                        Look at screenshots.
                        Guide users.
                        One step at a time.
                        try to respond in short instructions or ask more question no too much epxlanation needed
                        dont add * in the response""" + user_input
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

   

    # Save AI response
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )