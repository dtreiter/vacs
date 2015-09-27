import os
import sys

from core import CoreInterpreter

class TmuxInterpreter(CoreInterpreter):
    def send_keystrokes(self, keys):
        os.system("tmux send-keys " + keys)
