import os
import sys

from core import CoreInterpreter

class VboxInterpreter(CoreInterpreter):
    def send_keystrokes(self, keys):
        for scancode in keys.split(" "):
            os.system("VBoxManage controlvm SiftMri keyboardputscancode " + scancode)
