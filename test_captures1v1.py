#Entire Screen
import mss
import numpy as np
import cv2
from replace_straining_colorss2 import replace_straining_colors
def capture_and_display_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1] # Use the primary monitor

        while True:
            # Grab a frame from the screen
            sct_img = sct.grab(monitor)
            
            # Convert to a NumPy array
            frame = np.array(sct_img)

            #!!! After Changes
            # Use the imported function to process the frame
            processed_frame = replace_straining_colors(frame)
            
            # Display the frame in a window
            cv2.imshow("Screen Capture Test", processed_frame)
            
            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_display_screen()