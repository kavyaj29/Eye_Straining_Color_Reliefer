import cv2
import numpy as np

def replace_straining_colors(image):
    """
    Transforms an image by desaturating highly saturated colors.
    """
    # 1. Convert the image from BGR to HSV
    # OpenCV's default color format is BGR, not RGB
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 2. Identify straining colors using a simple rule
    # The second channel in HSV (index 1) represents saturation.
    # We'll create a mask where saturation is above a certain threshold (e.g., 150)
    straining_mask = hsv_image[:, :, 1] > 150
    
    # 3. Apply the transformation to the identified pixels
    # We'll reduce the saturation of those pixels by 50%
    hsv_image[straining_mask, 1] = (hsv_image[straining_mask, 1] * 0.5).astype(np.uint8)
    
    # 4. Convert the image back to BGR before returning
    processed_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    
    return processed_image