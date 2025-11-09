from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from config import DEVICE
from model.densenet_model import load_model
from utils.transforms import get_transform
from services.prediction_service import predict_image

app  = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model()
target_layer = model.features[-2]
transform = get_transform()
class_labels = ['Covid-19', 'Emphysema', 'Normal', 'Pneumonia-Bacterial', 'Pneumonia-Viral', 'Tuberculosis']

@app.get("/")
async def root():
    return FileResponse("template/index.html")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(DEVICE)
    return predict_image(model, image_tensor, image, class_labels, target_layer)
