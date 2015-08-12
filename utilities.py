import os

def child_directories(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]

def dump_grammar(grammar, output_file):
    """
    Writes a given grammar file to output_file as a human readable dictionary.
    """
    dump = "grammar = {\n"
    for key in grammar:
        if callable(grammar[key]):
            value = grammar[key].__name__
        else:
            value = "\"" + grammar[key] + "\""
        dump += "    \"" + key + "\": " + value + ",\n"

    # Remove trailing comma
    dump = dump[:-2]
    dump += "\n}"
    output_file.write(dump)
