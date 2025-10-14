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
        window = gw.getWindowsWithTitle(window_title)
        if not window:
             print(f"Window with title '{window_title}' not found.")
             return
        window = window[0] # Get the actual window object
    except IndexError: # This is a bit redundant due to the check above, but safer
        print(f"Window with title '{window_title}' not found.")
        return

    # 2. Start the real-time capture
    with mss.mss() as sct:
        while True:
            try:
                # 3. Get the window's bounding box (coordinates and size)
                # Re-get the coordinates on every loop in case the window moved or was resized
                bbox = {
                    "left": window.left,
                    "top": window.top,
                    "width": window.width,
                    "height": window.height
                }
                
                # Check for window visibility: 
                # Relaxed check: Only stop if it's minimized. Maximize is fine.
                # The top > -1 and left > -1 check is generally good for visibility, 
                # but pygetwindow can sometimes return valid coordinates for minimized windows.
                # Checking isMinimized is usually sufficient for a simple stop condition.
                if window.isMinimized:
                    print(f"Window '{window_title}' is minimized, pausing capture.")
                    time.sleep(0.5) # Wait a bit before checking again
                    continue

                # Grab a frame from the window's location
                sct_img = sct.grab(bbox)
                
                # Convert to a NumPy array for display (note: mss returns BGRA, cv2 expects BGR/RGB)
                frame = np.array(sct_img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR) # Convert from BGRA to BGR
                
                # Use the imported function to process the frame
                processed_frame = replace_straining_colors(frame)
                
                # Display the captured window content
                cv2.imshow(f"Mirroring: {window_title}", processed_frame)
            
            except gw.PyGetWindowException:
                # This exception typically occurs if the window is closed while the loop is running
                print(f"Window '{window_title}' was closed. Exiting capture.")
                break
            except Exception as e:
                # Catch other potential errors, like mss failing on a momentarily hidden/invalid region
                # print(f"An error occurred during capture: {e}")
                time.sleep(0.1)
                continue # Try again
            
            # Exit loop if the 'e' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Change 'WhatsApp' to the title of the window you want to capture
    window_name = "WhatsApp"
    capture_window_by_title(window_name)