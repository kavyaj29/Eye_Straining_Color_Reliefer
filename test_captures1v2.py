#Window
import mss
import numpy as np
import cv2
import pygetwindow as gw
import time
from replace_straining_colorss2 import replace_straining_colors
def capture_window_by_title(window_title):
    """
    Captures the content of a specific window in real-time.
    """
    # 1. Find the window by its title
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
    except IndexError:
        print(f"Window with title '{window_title}' not found.")
        return

    # 2. Get the window's bounding box (coordinates and size)
    bbox = {
        "left": window.left,
        "top": window.top,
        "width": window.width,
        "height": window.height
    }

    # 3. Start the real-time capture
    with mss.mss() as sct:
        while True:
            # Check if the window is still open
            if not window.isMaximized and not window.isMinimized and window.top > -1 and window.left > -1:
                # Update the bounding box in case the window moved
                bbox = {
                    "left": window.left,
                    "top": window.top,
                    "width": window.width,
                    "height": window.height
                }
                
                # Grab a frame from the window's location
                sct_img = sct.grab(bbox)
                
                # Convert to a NumPy array for display
                frame = np.array(sct_img)

                # Use the imported function to process the frame
                processed_frame = replace_straining_colors(frame)
                
                # Display the captured window content
                cv2.imshow(f"Mirroring: {window_title}", processed_frame)
            
            # Exit loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Change 'Untitled - Notepad' to the title of the window you want to capture
    window_name = "Snipping Tool"
    capture_window_by_title(window_name)