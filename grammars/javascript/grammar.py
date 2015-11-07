from functions import *

def snippet(key):
    return key + "<alt>/"

grammar = {
    "another": "<esc>A;<enter>",
    "canvas": "canvas",
    "console": "<ctrl>J",
    "finish": "<esc>A;<esc>",
    "javascript": ".js",
    "js": "js",
    "log": "console.log();<left><left>",
    "new": "new ",
    "node": "node ",
    "package": "npm ",
    "regular": "//<left>",
    "this": "this",
    "variable": "var ",

    "function": snippet("vcfn"),
    "method": snippet("vcmt"),
    "object": snippet("vcob")
}
