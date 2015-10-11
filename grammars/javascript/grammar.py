from functions import *

def snippet(key):
    return key + "<alt>/"

grammar = {
    "another": "<esc>A;<enter>",
    "finish": "<esc>A;",
    "javascript": ".js",
    "js": "js",
    "this": "this",

    "function": snippet("vcfn"),
    "method": snippet("vcmt"),
}
