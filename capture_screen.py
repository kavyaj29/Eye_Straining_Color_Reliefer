import cv2
import mss
import numpy as np
from replace_straining_colorss2 import replace_straining_colors

# Define a unique window title for the display window
WINDOW_TITLE = "Screen Capture (Filtered)"

def capture_full_screen():
    """
    Captures the entire primary monitor.
    
    NOTE: To prevent the 'infinite mirror' effect, please move or minimize
    the display window so it is not part of the capture area.
    """
    try:
        with mss.mss() as sct:
            # Get information of monitor 1 (the primary monitor)
            monitor = sct.monitors[1]

            print("Successfully started screen capture.")
            print("Capture started. Press 'e' in the display window to exit.")
            print("IMPORTANT: Move this window off-screen to avoid the mirror effect!")

            while True:
                # Grab a frame from the screen
                sct_img = sct.grab(monitor)

                # Convert to a NumPy array for OpenCV
                frame = np.array(sct_img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

                # Apply the color filter
                processed_frame = replace_straining_colors(frame)

                # Display the processed frame
                cv2.imshow(WINDOW_TITLE, processed_frame)

                # Exit loop if the 'e' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('e'):
                    break

    except Exception as e:
        print(f"An error occurred during screen capture: {e}")
    finally:
        # Clean up all OpenCV windows
        cv2.destroyAllWindows()
        print("Capture stopped and all windows have been closed.")

