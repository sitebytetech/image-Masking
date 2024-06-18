# import cv2
# import numpy as np
# from PIL import Image
# import requests
# import base64
# import io
# import time
# from transformers import pipeline

# # Load the image
# image = Image.open("./demo-1.png")

# # Perform semantic segmentation
# semantic_segmentation = pipeline("image-segmentation", "facebook/maskformer-swin-large-ade")
# results = semantic_segmentation(image)

# # Function to invert the colors of an image
# def invert_colors(mask_image):
#     # Convert the mask image to a NumPy array
#     np_image = np.array(mask_image)
#     # Invert the colors
#     inverted_image = cv2.bitwise_not(np_image)
    
#     # Create alpha channel
#     alpha_channel = np.where(np_image == 0, 0, 255).astype('uint8')
    
#     # Add the alpha channel to the original image
#     rgba_image = cv2.cvtColor(inverted_image, cv2.COLOR_RGB2RGBA)
#     rgba_image[:, :, 3] = alpha_channel
    
#     # Convert back to PIL Image
#     inverted_pil_image = Image.fromarray(rgba_image)
#     return inverted_pil_image

# base64_masks = []
# for class_label in results:
#     mask_image = class_label['mask']
#     mask_label = class_label['label']
    
#     # Invert the colors of the mask image
#     inverted_mask_image = invert_colors(mask_image)
    
#     # Convert inverted mask image to base64 format
#     buffered = io.BytesIO()
#     inverted_mask_image.save(buffered, format="PNG")
#     base64_mask = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
#     # Append base64 encoded mask image to the list
#     base64_masks.append({"label": mask_label, "base64": base64_mask})
    
#     inverted_mask_image.save(f"images/inverted_mask_{mask_label}.png")



