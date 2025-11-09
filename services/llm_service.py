import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_medical_description(encoded_image: str, label: str) -> dict:
    prompt = f"You are a radiologist. This image is an example of a person with known {label}. Without further ado or introduction, explain why and interpret the image according to what was diagnosed and analyze it well."

    payload = {
        "model": "edwardlo12/medgemma-4b-it-Q4_K_M",
        "prompt": prompt,
        "images": [encoded_image],
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=240)
    except requests.exceptions.RequestException as e:
        return {
            "summary": f"Error connecting to MedGemma for {label}",
            "details": str(e)
        }

    full_text = ""
    try:
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    full_text += data["response"]
                if data.get("done"):
                    break
    except Exception as e:
        return {
            "details": str(e)
        }

    if not full_text.strip():
        full_text = "No valid description received from LLM."

    return {
        "details": full_text.strip()
    }