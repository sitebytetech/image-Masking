from PIL import Image
import base64
import io
from transformers import pipeline
from utils.usefull_function import invert_colors
semantic_segmentation = pipeline("image-segmentation", "facebook/maskformer-swin-large-ade")
async def process_image(file):
    image = Image.open(file.file)
    results = semantic_segmentation(image)
    base64_masks =[]
    index = 0
    for class_label in results:
        mask_image = class_label['mask']
        mask_label = class_label['label']
        
        # Invert the colors of the mask image
        inverted_mask_image = invert_colors(mask_image)
        
        # Convert inverted mask image to base64 format
        buffered = io.BytesIO()
        inverted_mask_image.save(buffered, format="PNG")
        base64_mask = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        # Append base64 encoded mask image to the list
        base64_masks.append({"index":index,"label": mask_label, "base64": base64_mask})
        index +=1
        # inverted_mask_image.save(f"images/inverted_mask_{mask_label}.png")
    return base64_masks

