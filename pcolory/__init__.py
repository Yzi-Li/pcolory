# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: copyright.txt


from .pcolory import ColorPrint

__version__ = "0.1.0"

__all__ = [
    "cp",
    "colorprint",
    "config"
    ]

_colorprint = ColorPrint()
cp = colorprint = _colorprint
config = _colorprint.config
