import os
import sys

import globals
from base import BaseInterpreter

class TmuxInterpreter(BaseInterpreter):
    def send_keystrokes(self, keys):
        os.system("tmux send-keys -t " + globals.TARGET_NAME + " " + keys)
