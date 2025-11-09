# 🩻 Chest X-ray Classification & Interpretation (RadioSense)

This project is an early prototype developed by **Team RadioSense**, which achieved **1st place** in the **Startup Weekend of Isfahan University of Medical Sciences**.


<img width="905" height="1280" alt="image" src="https://github.com/user-attachments/assets/12eddc85-7a15-44d7-95f9-a046898d688a" />


The application analyzes **chest X-ray images** and classifies them into the following medical categories:

| Label | Condition |
|:------|:-----------|
| 0 | Covid-19 |
| 1 | Emphysema |
| 2 | Normal |
| 3 | Pneumonia-Bacterial |
| 4 | Pneumonia-Viral |
| 5 | Tuberculosis |

> ⚠️ More classes will be added in the next versions as the dataset grows and model capabilities expand.

---

## 🚀 Overview

The system performs **automated diagnosis and visual explanation** of chest X-rays:

1. **Classification** : Uses a fine-tuned `DenseNet121` model trained on medical imaging datasets, achieving **93.26% accuracy** on the test set.  
2. **Interpretation** : Generates **Grad-CAM** visualizations to highlight regions influencing the diagnosis.  
3. **Report Generation** : Uses an integrated **medical language model (MedGemma 4B)** via [Ollama](https://ollama.ai) to produce preliminary diagnostic reports in natural language.


<img width="905" height="1280" alt="image" src="https://github.com/user-attachments/assets/776afbec-13de-4149-a97e-1a101880040f" />


---

## 🧠 Model Details

- **Architecture:** DenseNet121  
- **Framework:** PyTorch  
- **Accuracy:** 93.26% (on test data)  
- **Target Device:** CPU / CUDA  

The model classifies the uploaded X-ray image and produces both a **predicted label** and a **Grad-CAM heatmap** that visually explains the decision.


<img width="1212" height="683" alt="f69a45dc-62f3-4b14-9be8-c272c159cc4a" src="https://github.com/user-attachments/assets/9ac84bad-3931-4c4b-922f-8d3f3918414a" />


---

## 🗣️ AI Report Generation (MedGemma 4B)

To enhance interpretability, the project integrates **Google’s MedGemma-4B** vision-language model via **Ollama**.  
This component analyzes the classified image and provides a **radiology-style textual interpretation**.

> Note: This part is currently under improvement and still being optimized for better accuracy and relevance.

### 🧩 Setting up Ollama with Docker

You can run MedGemma locally using [Ollama](https://ollama.ai):

```bash
# 1. Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# 2. Pull the MedGemma model
ollama pull edwardlo12/medgemma-4b-it-Q4_K_M

# 3. Run the Ollama API service
ollama serve
```

## 🧩 Tech Stack

Backend: FastAPI

Model Inference: PyTorch

Visualization: Grad-CAM

AI Report: MedGemma via Ollama

Frontend Preview: Simple static HTML interface

Deployment: Docker-compatible


## 👥 Team RadioSense

Ghazal Norouzi,
Mohsaneh Rezaeian,
Mojtaba Zarreh,
Mohammad Jalali,
Sara Pourbafrani,
Farank Ghaffari

## 💬 Future Work

Expanding classification classes (e.g., fibrosis, COPD, etc.),
Improving the MedGemma report quality and medical relevance,
Building a clinical-friendly dashboard and analytics panel,
Adding multi-language support for medical summaries

© 2025 RadioSense — Diagnostic Intelligence for Medical Imaging
