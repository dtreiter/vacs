import utilities

def jump(text):
    if text.isdigit():
        return text + "gg"
    else:
        utilities.log("ERROR: Non-digit argument provided to jump function")
        return ""
