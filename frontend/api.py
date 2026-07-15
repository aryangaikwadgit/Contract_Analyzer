import requests

BASE_URL = "http://127.0.0.1:8000"


def analyze_contract(file):

    files = {"file": (file.name, file.getvalue(), "application/pdf")}

    response = requests.post(f"{BASE_URL}/analyze", files=files)

    return response.json()

def ask_question(question):

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "question": question
        }
    )

    response.raise_for_status()

    return response.json()