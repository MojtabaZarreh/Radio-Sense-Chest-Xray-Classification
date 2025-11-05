import os, uuid, cv2
import numpy as np
from PIL import Image
from fastapi.responses import JSONResponse
from config import STATIC_DIR
from utils.gradcam import compute_gradcam
from utils.image_tools import image_to_base64
from services.llm_service import get_medical_description

def predict_image(model, image_tensor, original_image, class_labels, target_layer):
    gradcam, pred_class = compute_gradcam(model, image_tensor, target_layer)
    label = class_labels[pred_class]

    heatmap = cv2.applyColorMap(np.uint8(255 * gradcam), cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(
        np.array(original_image.resize((300, 300))), 0.5,
        cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB), 0.5, 0
    )

    os.makedirs(STATIC_DIR, exist_ok=True)
    file_id = f"{uuid.uuid4()}.jpg"
    heatmap_path = os.path.join(STATIC_DIR, file_id)
    Image.fromarray(overlay).save(heatmap_path)

    encoded_image = image_to_base64(original_image)
    llm_info = get_medical_description(encoded_image, label)

    return JSONResponse({
        "class": label,
        "details": llm_info["details"],
        "gradcam_url": f"/static/images/{file_id}"
    })