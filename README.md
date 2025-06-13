# pcolory

A library that can make ```print()``` colorful.

## Why it called ```pcolory```?

It is ```p``` + ```color``` + ```y```.

## Install
```
pip install pcolory
```

## Usage

### ```colorprint()```

Use ```cp()``` or ```colorprint()``` to print colorful text.

```python
from pcolory.colors import FG_GREEN, BG_GREEN
from pcolory import colorprint

colorprint("Hello World!", fg=FG_GREEN)
colorprint("Hello World!", bg=BG_GREEN)
```
#### PowerShell Output
<span style="color: #13A10E; font-family: 'Consolas', 'Courier New', monospace; font-size: 1em; font-weight: normal;">Hello World!</span> <br> <span style="background-color: #13A10E; font-family: 'Consolas', 'Courier New', monospace; font-size: 1em; font-weight: normal;">Hello World!</span>

You can use it just like ```print()```.

```python
# multiple text
colorprint("Hello", "World!", fg=FG_GREEN)

# sep argument
colorprint("Hello", "World!", fg=FG_GREEN, sep=", ")

# end argument
colorprint("Hello", "World", fg=FG_GREEN, sep=", ", end="!")
```

### ```config()```

```config()``` will be applied globally. When both ```config()``` and ```colorprint()``` are set, ```colorprint()``` has a higher priority.

```python
from pcolory.colors import FG_GREEN, FG_RED
from pcolory import colorprint, config

config(fg=FG_GREEN)

colorprint("Hello World!")
colorprint("Hello World!", fg=FG_RED)
```

<span style="color: #13A10E; font-family: 'Consolas', 'Courier New', monospace; font-size: 1em; font-weight: normal;">Hello World!</span> <br> <span style="color: #C50F1F; font-family: 'Consolas', 'Courier New', monospace; font-size: 1em; font-weight: normal;">Hello World!</span>

## Bugs/Feature requests

Please send a bug report or feature requests through github issue tracer.
