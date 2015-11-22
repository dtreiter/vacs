import os
import sys

from base import BaseInterpreter

class VboxInterpreter(BaseInterpreter):
    def send_keystrokes(self, keys):
        for scancode in keys.split(" "):
            os.system("VBoxManage controlvm SiftMri keyboardputscancode " + scancode)
