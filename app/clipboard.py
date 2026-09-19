import pyperclip
import time

def get_clipboard():
    return pyperclip.paste()

def is_youtube_url(text):
    return "youtube.com/" in text or "youtu.be/" in text

def watch_clipboard(callback):
    last_clipboard = ""
    new_clipboard = False

    while True:
        current_clipboard = pyperclip.paste()

        if current_clipboard != last_clipboard:
            last_clipboard = current_clipboard
            new_clipboard = True

        if is_youtube_url(current_clipboard):
            if new_clipboard == True:
                callback(current_clipboard)
                new_clipboard = False

        time.sleep(0.5)