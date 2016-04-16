# VACS
**VACS**, the Voice Accessibility Control System, allows you to control a computer
by speaking. In particular, it is well suited to programming.

For example, speaking the following:
```
function word example next file entry directory next
loop directory next directories next
condition directory dot word contains call file next
print string say this directory contains the given file period
```

would produce the following python code:
```python
def example(file, dir):
    for dir in dirs:
        if dir.contains(file):
            print('This directory contains the given file.')
```

*or* the following JavaScript code:
```javascript
function example(file, dirs) {
    dirs.forEach(function(dir) {
        if (dir.contains(file)) {
            console.log('This directory contains the given file.');
        }
    });
}
```

Some interesting aspects of VACS are:
- Independent of the speech-to-text program used.
- Written entirely by voice using itself. This stands as a good usability
  benchmark.
- Can be used with just about any programming language or program with good
  keyboard shortcuts (i.e. web browsers).
- Allows you to type alongside speaking if desired.

## Grammars

What a spoken word does is controlled by a 'grammar'. A grammar is just a
dictionary mapping spoken words to keystrokes. For example:

```python
grammar = {
    "directory": "dir",
    "function": "func<alt>/"
}
```

The idea is to write grammars for common tasks. Some examples are a Python
grammar, JavaScript grammar, shell grammar, Vimium grammar (to control a web
browser), etc. Any keyboard oriented task can be easily done by speaking with a
well thought out grammar.

In general, grammars should try to only map words to keystrokes. More complex
things, like inserting code snippets, should be handled instead by whatever
editor you use. In the above example, to insert a snippet for a function you
just map "function" to `func<alt>/` -- where `<alt>/` is just a keyboard
shortcut to trigger snippet expansion.

For more complex things, VACS does allow for spoken words to map to arbitrary
Python code. Here's an example:

```
def lowercase(text):
    return text.lower()

grammar = {
    "lower": lowercase
}
```

This will take the rest of the spoken phrase following "lower" and make it
lowercase. Grammar functions can do a lot more and will be documented when VACS
is officially released.

VACS works by having an active 'mode', which is a collection of grammars. For
example, Python mode could have both the Python and shell grammars active, with
Python taking precedence over shell.

## Usage

VACS is still a work in progress. This is not an official release, so if you
need to use it be aware that things may change (though the format of the
grammars will stay the same). The main thing remaining before a beta release is
just packaging it up to be easily installed with the grammars in a manageable
location.

Also note that it has only been tested thoroughly on OS X. It should work fine
on Unix-like systems, such as Linux as well. Windows (Cygwin) support should be
straight forward, but I haven't had access to a Windows box to work with.

To use it currently:
- Get a speech to text program. OS X comes with a free real-time dictation
  program that works well.
- Make sure you have either Tmux or VirtualBox.
- Clone the repo and cd to it.
- Start running a Tmux session or VirtualBox VM in another window.
- Run `python vacs.py <target_type> <target_name>`, where target_type is one of
  `tmux` or `vbox` and target_name is the Tmux session or VirtualBox VM name.
- Start your speech to text program in this VACS window and you're good to go!

## License
GNU Affero GPL v3

Feel free to contact me if you'd like to discuss anything.
