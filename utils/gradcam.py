import numpy as np
import cv2
import torch

def compute_gradcam(model, image_tensor, target_layer):
    gradients, activations = [], []

    def forward_hook(module, input, output):
        activations.append(output)
    def backward_hook(module, grad_input, grad_output):
        gradients.append(grad_output[0])

    handle_fwd = target_layer.register_forward_hook(forward_hook)
    handle_bwd = target_layer.register_full_backward_hook(backward_hook)

    output = model(image_tensor)
    _, pred_class = torch.max(output, 1)
    model.zero_grad()
    output[0, pred_class].backward()

    handle_fwd.remove()
    handle_bwd.remove()

    grad = gradients[0].cpu().detach().numpy()
    act = activations[0].cpu().detach().numpy()
    weights = np.mean(grad, axis=(2, 3), keepdims=True)
    gradcam = np.sum(weights * act, axis=1)
    gradcam = np.maximum(gradcam, 0)[0]
    gradcam = cv2.resize(gradcam, (300, 300))
    gradcam = (gradcam - gradcam.min()) / (gradcam.max() - gradcam.min())

    return gradcam, pred_class.item()