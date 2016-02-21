import os
import sys

import globals
from base import BaseInterpreter

class VboxInterpreter(BaseInterpreter):
    def send_keystrokes(self, keys):
        for scancode in keys.split(" "):
            os.system("VBoxManage controlvm " + globals.TARGET_NAME + " keyboardputscancode " + scancode)
