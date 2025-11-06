import cv2
import mss
import numpy as np
import pygetwindow as gw
from replace_straining_colorss2 import replace_straining_colors
from replace_straining_colorsrgb import replace_straining_colors_rgb
def capture_window_seamlessly(window_title):
    """
    Captures the content of a specific window in real-time using MSS.
    NOTE: This method captures a region of the screen and will show any
    overlapping windows.
    """
    print(f"Attempting to capture window: '{window_title}'")
    
    try:
        # 1. Find the window by its title
        window = gw.getWindowsWithTitle(window_title)
        if not window:
             print(f"Error: Window with title '{window_title}' not found.")
             return
        window = window[0]
    except IndexError:
        print(f"Error: Window with title '{window_title}' not found.")
        return

    try:
        with mss.mss() as sct:
            print("Successfully attached to window. Press 'e' in the display window to exit.")
            while True:
                # 2. Check if the window was closed or minimized
                if not window.visible or window.isMinimized:
                    print(f"Window '{window_title}' is no longer visible or is minimized. Stopping capture.")
                    break

                # 3. Get the window's current bounding box on each frame
                # This ensures the capture follows the window if it's moved
                bbox = {
                    "left": window.left,
                    "top": window.top,
                    "width": window.width,
                    "height": window.height
                }
                
                # Ensure the bounding box has a valid size
                if bbox["width"] <= 0 or bbox["height"] <= 0:
                    cv2.waitKey(100) # Wait a moment and check again
                    continue

                # 4. Grab a frame from the window's location
                sct_img = sct.grab(bbox)
                
                # 5. Convert to a NumPy array for display
                frame = np.array(sct_img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                
                # 6. Apply the color filter
                #processed_frame = replace_straining_colors(frame)
                processed_frame = replace_straining_colors_rgb(frame)               
                # 7. Display the captured window content
                cv2.imshow(f"Mirroring: {window_title}", processed_frame)
            
                # Exit loop if the 'e' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('e'):
                    break
    
    except Exception as e:
        print(f"An error occurred during window capture: {e}")
    finally:
        # 8. Clean up all resources
        cv2.destroyAllWindows()
        print("Capture stopped and all windows have been closed.")

