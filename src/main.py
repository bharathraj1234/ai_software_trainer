import requests
import json

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": "How do I create a folder?",
        "stream": True
    },
    stream=True
)

full_answer = ""

for line in response.iter_lines():

    if line:

        data = json.loads(line)

        chunk = data.get("response", "")

        print(chunk, end="", flush=True)

        full_answer += chunk

print("\n\nFinal Answer:")
print(full_answer)