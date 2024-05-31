# Screenshot Taking Application

Welcome to the Screenshot Taking Application, a Python-based utility for capturing screenshots. This application allows users to take full-screen screenshots or specific window screenshots, save them in a specified directory, and choose the desired file format for the screenshots.

## Features

- **Capture Full-Screen Screenshots**: Capture the entire screen from any connected monitor.
- **Capture Specific Window Screenshots**: Capture screenshots of specific windows based on their title.
- **Save in Various Formats**: Save screenshots in multiple formats such as PNG, JPEG, BMP, and more.
- **User-Friendly Prompts**: Easily specify directory location, number of screenshots, and file format through interactive prompts.

## Dependencies

The application relies on the following Python libraries:
- **`mss`**: A cross-platform screenshot module for capturing full-screen images.
- **`pyscreenshot`**: A module for capturing screenshots of specific regions or windows.
- **`pygetwindow`**: A module for getting and manipulating windows by title.
- **`ctypes`**: A foreign function library for Python, used here for interacting with Windows API functions.
- **`PIL (Pillow)`**: The Python Imaging Library, used for image manipulation and saving.
- **`datetime`**: A module for handling dates and times, used for timestamping screenshots.

Ensure these libraries are installed before running the application:
```bash
pip install mss pyscreenshot pygetwindow pillow
