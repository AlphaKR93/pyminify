:information_source: Note that python-minifier depends on the python interpreter for parsing source code,
and will output source code compatible with the version of the interpreter it is run with.

This means that if you minify code written for Python 3.11 using python-minifier running with Python 3.12,
the minified code may only run with Python 3.12.
