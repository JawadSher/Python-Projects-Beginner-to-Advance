import mss
import time
import os
import pyscreenshot as grabShot
import pygetwindow as grabWinShot
import ctypes
from PIL import Image
from datetime import datetime

def saveFile(save_Dir, shots_length, img, file_format):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screen_shot{shots_length}.{file_format}'
    filepath = os.path.join(save_Dir, filename)
    img.save(filepath, file_format.upper())
    print(f'Screenshot saved successfully! (Shots remaining: {shots_length - 1})')
    print(f'Saved image: {filepath}')

def full_Screen_Capture(monitorNum, file_format):
    save_Dir = input("Define Location to Save Images : ")
    shots_length = int(input("How many Number of Screen Shots : "))
    
    if not os.path.exists(save_Dir):
        os.makedirs(save_Dir)
    
    if shots_length <= 0 :
        print("Invalid Length of ScreenShots")
        return 

    while(shots_length):
        monitor = monitors[monitorNum]
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)

        saveFile(save_Dir, shots_length, img, file_format)
        shots_length -= 1

def bring_window_to_foreground(window):
    try:
        ctypes.windll.user32.SetForegroundWindow(window._hWnd)
        time.sleep(2)  # Wait a bit for the window to come to the foreground
        return True
    except Exception as e:
        print(f'Error bringing window to foreground: {e}')
        return False

def grabWindowShot(window_Title, file_format):
    save_Dir = input("Define Location to Save Images: ")
    shots_length = int(input("How many Number of Screen Shots: "))

    if shots_length <= 0:
        print("Invalid Length of ScreenShots")
        return

    while shots_length:
        windows = grabWinShot.getWindowsWithTitle(window_Title)
        if not windows:
            print(f'Window with Title "{window_Title}" not found')
            return

        if len(windows) > 1:
            print(f'Multiple Windows with Title "{window_Title}" found')
            for i, window in enumerate(windows):
                print(f'{i+1}. {window.title}')
            try:
                window_choice = int(input("Enter the number of the desired window: ")) - 1
                if window_choice < 0 or window_choice >= len(windows):
                    print("Invalid window selection")
                    continue
                window = windows[window_choice]
            except ValueError:
                print("Invalid input. Please enter a number: ")
                continue
        else:
            window = windows[0]

        try:
            print(f'Attempting to bring window "{window.title}" to the foreground')
            if not window.isMinimized:
                if bring_window_to_foreground(window):
                    print(f'Window "{window.title}" is in the foreground. Capturing screenshot...')
                    bbox = (window.left, window.top, window.right, window.bottom)
                    print(f'Window bounds: {bbox}')
                    
                    try:
                        img = grabShot.grab(bbox=bbox, backend="mss")
                        saveFile(save_Dir, shots_length, img, file_format)
                    except Exception as capture_error:
                        print(f'Error capturing screenshot with bbox {bbox}. Exception: {capture_error}')
                        return
                    
                else:
                    print(f'Failed to bring window "{window.title}" to foreground.')
                    return
            else:
                print(f'The window "{window.title}" is minimized. Please restore it and try again.')
                return

        except Exception as e:
            print(f'Error activating window: "{window_Title}". Exception: {e}')
            return

        shots_length -= 1


if __name__ == '__main__':
    print("******* Welcome to Screenshot Taking Application *******")
    execute = True
    while(execute):
        types = ['Full-Screen-Screenshot', 'Specific-Window-Screenshot']

        for index, val in enumerate(types):
            print(f'{index+1} - {val}')
        sel_type = int(input("Please Select an Option (1 or 2) : "))

        try:
            if(sel_type == 1):
                with mss.mss() as sct:
                    monitors = sct.monitors 
                    if (len(monitors) > 1):
                         chooseMonitor = int(input("Please Enter a Monitor No : "))
                         file_form = input("File format : ")
                         full_Screen_Capture(chooseMonitor, file_form)
                    elif(len(monitors) == 1):
                        file_form = input("File format : ")
                        full_Screen_Capture(1, file_form)

            elif(sel_type == 2):
                window_title = input("Window Title : ")
                file_form = input("File Format : ")
                grabWindowShot(window_title, file_form)
            else:
                print("Invalid Option Selected")
        
            execution = input("exit or continue : ")
            if(execution.lower() == 'exit'):
                execute = False
            elif(execution.lower() == 'continue'):
                execute = True
            else:
                print("Invalid Option Selected")

        except KeyboardInterrupt:
            print("Application Crash - Execute Again")
            exit()






