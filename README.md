# pcolory

[![build](https://github.com/Yzi-Li/pcolory/actions/workflows/build.yaml/badge.svg)](https://github.com/Yzi-Li/pcolory/actions)
[![flake8](https://github.com/Yzi-Li/pcolory/actions/workflows/lint.yaml/badge.svg)](https://github.com/Yzi-Li/pcolory/actions?query=workflow%3ALint)
[![coverage](https://img.shields.io/codecov/c/github/Yzi-Li/pcolory)](https://codecov.io/gh/Yzi-Li/pcolory)
[![pypi](https://img.shields.io/pypi/v/pcolory.svg)](https://pypi.org/project/pcolory/)
[![support-version](https://img.shields.io/pypi/pyversions/pcolory)](https://img.shields.io/pypi/pyversions/pcolory)
[![license](https://img.shields.io/github/license/Yzi-Li/pcolory)](https://github.com/Yzi-Li/pcolory/blob/main/LICENSE)

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

<img src="./docs/images/output1.png" width=180px>

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

<img src="./docs/images/output2.png" width=180px>

## Bugs/Feature requests

Please send a bug report or feature requests through [github issue tracer](https://github.com/Yzi-Li/pcolory/issues).
