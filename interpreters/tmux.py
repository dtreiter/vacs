import os
import sys

import config
from base import BaseInterpreter

class TmuxInterpreter(BaseInterpreter):
    def send_keystrokes(self, keys):
        os.system("tmux send-keys -t " + config.TARGET_NAME + " " + keys)
