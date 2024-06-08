<h1 align='center'>Keylogger with pynput</h1>

This Python script uses the `pynput` library to create a simple keylogger that captures and logs all keyboard inputs. Below is an explanation of how the code works:

## Importing the Necessary Libraries

  -   `pynput`: A library that allows you to control and monitor input devices.
  -   `pynput.keyboard`: Provides the `Key` and `Listener` classes to handle keyboard events.

## Global Variables

  -   `keys` : A list to store all the keys that are pressed.

## Defining the Event Handlers

  ### `on_press` Function :
  
  - `on_press(key)`: A function that is called whenever a key is pressed.
      -   It appends the key to the `keys` list.
      -   Calls the `key_write(keys)` function to write the keys to a file.
      -   Attempts to print the key character if it's an alphanumeric key; otherwise, it prints the special key.

  ### `key_write` Function :

  - `key_write(keys)`: A function that writes the logged keys to a file.
      -   Opens (or creates) `logs.txt` in write mode.
      -   Iterates over the `keys` list and writes each key to the file, replacing single quotes with empty strings.

  ### `on_release` Function :
  
  -   `on_release(key)`: A function that is called whenever a key is released.
      -   Prints the released key.
      -   If the `Esc` key is released, it prints "Program Exit" and returns `False` to stop the listener.

## Setting Up the Listener : 
  
  -   `Listener(on_press=on_press, on_release=on_release)`: Creates a `Listener` object that monitors keyboard events.
      -   `on_press`: The function to call when a key is pressed.
      -   `on_release`: The function to call when a key is released.
  -   `listener.join()`: Starts the listener and blocks the program, keeping it running to capture keyboard events.

### Summary

This script is a basic keylogger that logs every key press and release to a text file `logs.txt`. It captures both alphanumeric and special keys, prints them to the console, and writes them to the file. The logging stops when the `Esc` key is pressed.

## Requirements

-   Python 3.x
-   `pynput` library

You can install the `pynput` library using pip:

```
 pip install pynput
``` 

## Usage

1.  Clone the repository or download the script file.
2.  Ensure you have Python 3.x installed on your machine.
3.  Install the `pynput` library if you haven't already (see Requirements section).
4.  Run the script:

	```
	python keylogger.py
	```

6.  The script will start logging all key presses and releases. The log will be saved in a file named `logs.txt`.
7.  To stop the keylogger, press the `Esc` key.
