# https://github.com/moses-palmer/pynput/issues/20

from pynput import keyboard
import pynput,time
import pyperclip

from PyQt5. QtCore import*
from PyQt5. QtGui import*
from PyQt5. QtWidgets import QApplication
import re

app= QApplication([])
clipboard=app.clipboard()

def on_press(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        # print('Start monitor')
        run_clipboard_monitor()
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    pass

def run_clipboard_monitor():
    data = clipboard.mimeData()
    if data.hasFormat('text/uri-list'):
        pass
    elif data.hasText():
        data = pyperclip.paste()
        data_ = str_formulate(data)
        pyperclip.copy(data_)
        listener.stop()
    else:
        pass

def str_formulate(data:str):
    return re.sub('[\r\n\s:]','_',data)


print("Program start now.")
while True:
    current = set()
    # print("Here i go .")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()