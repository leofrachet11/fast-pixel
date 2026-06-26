# Fast Pixel Scanner

A highly optimized, cross-platform mouse position and pixel color reader for Windows and macOS.

## Installation

```bash
pip install fast-pixel
```

## Usage

```python
import fast_pixel
import time

while True:
    x, y = fast_pixel.get_position()
    r, g, b = fast_pixel.get_color(x, y)
    print(f'X: {x} Y: {y} | RGB: {r}, {g}, {b}', end = '\r')
    time.sleep(0.1)
```