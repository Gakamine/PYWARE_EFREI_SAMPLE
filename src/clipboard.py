import pyperclip

def get_clipboard():
    clipboard = pyperclip.paste()
    clipboard = clipboard.replace('\r', '').replace('\n', '')
    return clipboard