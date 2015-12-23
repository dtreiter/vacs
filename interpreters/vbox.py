import os
import sys

import config
from base import BaseInterpreter

class VboxInterpreter(BaseInterpreter):
    def send_keystrokes(self, keys):
        for scancode in keys.split(" "):
            os.system("VBoxManage controlvm " + config.CONNECTION_NAME + " keyboardputscancode " + scancode)
