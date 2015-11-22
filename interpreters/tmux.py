import os
import sys

from base import BaseInterpreter

class TmuxInterpreter(BaseInterpreter):
    def send_keystrokes(self, keys):
        os.system("tmux send-keys " + keys)
