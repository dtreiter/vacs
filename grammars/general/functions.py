def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

def camelcase(text):
    output = ''.join(letter for letter in text.title() if letter.isalpha())
    return output[0].lower() + output[1:]

def spinecase(text):
    return "-".join(text.lower().split(" "))

def titlecase(text):
    return text[0].upper() + text[1:]

def dotcase(text):
    return ".".join(text.lower().split(" "))

def nospaces(text):
    return "".join(text.lower().split(" "))

def snakecase(text):
    return "_".join(text.lower().split(" "))

