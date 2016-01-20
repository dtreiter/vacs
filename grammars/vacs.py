import grammar_utilities

def python_mode(text):
    grammar_utilities.set_mode("python")

def javascript_mode(text):
    grammar_utilities.set_mode("javascript")

grammar = {
    "alias": "t]a, <quote><quote><left>",
    "aliases": "aliases",
    "compiler": "compiler",
    "config": "config",
    "control": "<lbracket>ctrl<rbracket>",
    "directory": "directory",
    "filter": "filter",
    "functions": "functions",
    "general": "general",
    "grammar": "grammar",
    "interpreter": "interpreter",
    "javascript": javascript_mode,
    "lexer": "lexer",
    "mode": "mode",
    "parser": "parser",
    "python": python_mode,
    "reinitialize": grammar_utilities.reload_grammars,
    "symbol": "symbol",
    "token": "token",
    "utilities": "utilities",
    "vacs": "vacs"
}
