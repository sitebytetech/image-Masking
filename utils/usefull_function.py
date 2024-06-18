import cv2
import numpy as np
from PIL import Image
def invert_colors(mask_image):
    # Convert the mask image to a NumPy array
    np_image = np.array(mask_image)
    # Invert the colors
    inverted_image = cv2.bitwise_not(np_image)
    
    # Create alpha channel
    alpha_channel = np.where(np_image == 0, 0, 255).astype('uint8')
    
    # Add the alpha channel to the original image
    rgba_image = cv2.cvtColor(inverted_image, cv2.COLOR_RGB2RGBA)
    rgba_image[:, :, 3] = alpha_channel
    
    # Convert back to PIL Image
    inverted_pil_image = Image.fromarray(rgba_image)
    return inverted_pil_image
