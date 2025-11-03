# Eye-Straining Color Reliever

A real-time screen and window capturing tool that applies a color filter to reduce eye strain from overly saturated or bright colors.

## Overview

This application provides a simple and effective way to view content on your screen with reduced color intensity. It can capture either your entire screen or a specific application window, process the video feed in real-time to desaturate harsh colors, and display the filtered result. This is particularly useful for users who are sensitive to bright colors or work for long hours in front of a screen. The project features a Google Meet-style selection menu, allowing the user to easily choose what they want to share and filter.

## Features

- **Real-Time Color Filtering**: Applies a custom filter to reduce the saturation of straining colors on the fly
- **Google Meet-Style Selection UI**: A simple graphical user interface to choose between sharing the entire screen or a specific application window
- **Full Screen Capture**: Mirrors your entire primary monitor with the color filter applied
- **Application Window Capture**: Mirrors a specific window you select from a list of all open applications
- **Modular and Clean Codebase**: The project is structured into logical modules for easy understanding and modification

## Project Structure

The project is organized into the following Python files:

- **`app_launcher.py`**: The main entry point for the application. It launches a Tkinter GUI that allows the user to select their desired capture mode.
- **`capture_screen.py`**: Contains all the logic for capturing the entire screen using the `mss` library.
- **`capture_window.py`**: Contains the logic for capturing a specific application window, also using `mss` and `pygetwindow` to identify and track the window.
- **`replace_straining_colorss2.py`**: The core image processing module. It contains the `replace_straining_colors` function, which performs the color desaturation on each frame.

## Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

- Python 3.7 or higher
- Windows 10 or 11 (as `pygetwindow` works best on Windows)

### 2. Clone the Repository

Open your terminal or command prompt and clone your repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 3. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (on Windows Command Prompt)
venv\Scripts\activate.bat

# Or activate it (on Windows PowerShell)
venv\Scripts\Activate.ps1
```

### 4. Install Required Libraries

With your virtual environment activated, install all the necessary packages using pip:

```bash
pip install opencv-python mss pygetwindow numpy
```

## How to Use

1. **Launch the Application**: Run the `app_launcher.py` script from your terminal:
   ```bash
   python app_launcher.py
   ```

2. **Make a Selection**: A selection window will appear.
   - To share your entire screen, click the **"Share Screen"** button.
   - To share a specific window, click its name in the list and then click the **"Share Selected Window"** button.

3. **View the Filtered Stream**: A new window will appear, showing the captured content with the color filter applied.

4. **Stop the Capture**: To stop the stream, make sure the display window is active (click on it) and press the **'e'** key on your keyboard.

## Dependencies

This project relies on the following Python libraries:

- **`opencv-python`**: For displaying the video frames
- **`mss`**: For fast and efficient screen capturing
- **`pygetwindow`**: For finding and getting information about open windows
- **`numpy`**: For numerical operations on image data
- **`tkinter`**: (Built-in with Python) For the graphical user interface

## Known Limitations

- The window capture method uses `mss`, which takes a screenshot of a screen region. This means that if you move another window on top of the application you are capturing, the overlapping window will also be shown in the stream.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
