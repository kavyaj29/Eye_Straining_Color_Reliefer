import cv2
import numpy as np

def replace_straining_colors_rgb(image: np.ndarray) -> np.ndarray:
    """
    Transforms an image by desaturating highly vibrant colors using only the BGR 
    (RGB) color space.

    NOTE: This approach is a replacement for the HSV logic and attempts to mimic 
    desaturation by pulling the R, G, and B components closer to the pixel's average 
    brightness (Luminance).

    Args:
        image: A NumPy array representing the image frame in BGR format (cv2 standard).

    Returns:
        A NumPy array of the processed image frame in BGR format.
    """

    # 1. Convert BGR to float32 for precise calculation
    # The image is expected to be in BGR format (standard for OpenCV).
    bgr_float = image.astype(np.float32)

    # Separate channels
    B, G, R = cv2.split(bgr_float)

    # 2. Calculate a simple measure of "saturation" in the RGB space
    # Saturation in RGB can be approximated by the difference between the max 
    # and min channels (Chroma).
    chroma = np.max(bgr_float, axis=2) - np.min(bgr_float, axis=2)

    # 3. Calculate the Luminance (Average Brightness)
    # This value acts as the gray target we want to pull the colors towards.
    luminance = (R + G + B) / 3.0

    # 4. Identify "straining" (highly vibrant) pixels
    # We use a threshold on the Chroma value (high chroma = high vibrancy)
    # ADJUSTED: Raised the threshold to target only the MOST vivid colors (less dulling overall).
    CHROMA_THRESHOLD = 150.0
    straining_mask = chroma > CHROMA_THRESHOLD

    # 5. Define the Reduction Factor
    # ADJUSTED: Reduced the factor for a gentler desaturation effect.
    DESATURATION_FACTOR = 0.5   
    
    # 6. Apply the transformation to the identified pixels

    # Formula for desaturation: New_Channel = Old_Channel + Factor * (Luminance - Old_Channel)
    R[straining_mask] = R[straining_mask] + DESATURATION_FACTOR * (luminance[straining_mask] - R[straining_mask])
    G[straining_mask] = G[straining_mask] + DESATURATION_FACTOR * (luminance[straining_mask] - G[straining_mask])
    B[straining_mask] = B[straining_mask] + DESATURATION_FACTOR * (luminance[straining_mask] - B[straining_mask])

    # 7. Merge channels and clip values
    processed_image = cv2.merge([B, G, R])
    
    # Ensure all values are within the valid 0-255 range and convert back to uint8
    processed_image = np.clip(processed_image, 0, 255).astype(np.uint8)

    return processed_image