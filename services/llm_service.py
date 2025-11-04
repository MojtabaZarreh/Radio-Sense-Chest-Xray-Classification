import requests, json, base64, io
from PIL import Image

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_medical_description(image_path: str, label: str) -> dict:
    img = Image.open(image_path).convert("RGB")
    img = img.resize((512, 512))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    encoded_image = base64.b64encode(buf.getvalue()).decode("utf-8")

    prompt = (
        f"You are an expert radiologist. "
        f"The following image is of a patient diagnosed with {label}. "
        f"Without introduction, describe the radiological findings and explain how they indicate {label}."
    )

    payload = {
        "model": "alibayram/medgemma:4b",
        "prompt": prompt,
        "images": [encoded_image],
        "stream": False,
        "num_predict": 120
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        response.raise_for_status()
        data = response.json()
        if "response" in data:
            return {"details": data["response"].strip()}
        return {"details": "No valid description received from the model."}
    except requests.exceptions.RequestException as e:
        return {"summary": f"Error connecting to MedGemma for {label}", "details": str(e)}