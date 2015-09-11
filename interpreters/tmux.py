import os
from core import CoreInterpreter

class TmuxInterpreter(CoreInterpreter):
    def process_words(self, words):
        """
        Loops over each word, stopping if a word is not in mode_grammar. If the
        rule's value is a function, call the function with the rest of the
        words. Otherwise send the rule's value.
        """
        for index, word in enumerate(words):
            if word in self.mode_grammar:
                if callable(self.mode_grammar[word]):
                    # Run the rest of the text through the function.
                    text = " ".join(words[index + 1:])
                    try:
                        result = self.mode_grammar[word](text)
                        os.system("tmux send-keys -l \"" + result + "\"")
                        print("FUNCTION " + word + " -> " + result + "\r")
                    except:
                        print("ERROR: Unexpected error in grammar function" + "\r")
                        print(str(sys.exc_info()[0]) + "\r")
                    break
                else:
                    keys = self.mode_grammar[word]
                    self.send_keystrokes(keys)
                    # The \r is needed when outputting in raw mode.
                    print(word + " -> " + keys + "\r")
            else:
                print("Unrecognized rule: " + word + "\r")
                break

    def send_keystrokes(self, keys):
        os.system("tmux send-keys " + keys)
