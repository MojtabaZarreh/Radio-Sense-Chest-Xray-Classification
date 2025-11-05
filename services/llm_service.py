import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_medical_description(encoded_image: str, label: str) -> dict:
    # prompt = f"You are a radiologist. This image is an example of a person with known {label}. Without further ado or introduction, explain why and interpret the image according to what was diagnosed and analyze it well."

    # payload = {
    #     "model": "edwardlo12/medgemma-4b-it-Q4_K_M",
    #     "prompt": prompt,
    #     "images": [encoded_image],
    #     "num_predict": 50
    # }
    
    # try:
    #     response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=240)
    # except requests.exceptions.RequestException as e:
    #     return {
    #         "summary": f"Error connecting to MedGemma for {label}",
    #         "details": str(e)
    #     }

    # full_text = ""
    # try:
    #     for line in response.iter_lines():
    #         if line:
    #             data = json.loads(line.decode("utf-8"))
    #             if "response" in data:
    #                 full_text += data["response"]
    #             if data.get("done"):
    #                 break
    # except Exception as e:
    #     return {
    #         "details": str(e)
    #     }

    # if not full_text.strip():
    #     full_text = "No valid description received from LLM."

    # return {
    #     "details": full_text.strip()
    # }
    
    return {
        "details": "Based on the chest X-ray, the diagnosis is emphysema. The lungs appear significantly overinflated, indicating hyperinflation and air trapping. Lung markings, including blood vessels and airways, are more prominent than normal due to increased lung volume. The anteroposterior diameter of the chest is increased, and the diaphragm appears flattened. These findings are consistent with emphysema, where the alveoli in the lungs are damaged, leading to air trapping and hyperinflation. The presence of lines may suggest a previous surgery or medical intervention, and the overall appearance of the lungs indicates significant destruction of the alveolar walls."
    }