import os

import requests


def main() -> None:
    base_url = os.environ["OLLAMA_URL"]
    url = f"{base_url}/api/generate"

    payload = {
        "model": "llama3.2:3b",
        "prompt": "Explain what Python is in one sentence.",
        "stream": False,
    }

    response = requests.post(url, json=payload)
    data = response.json()

    print(data)


if __name__ == "__main__":
    main()