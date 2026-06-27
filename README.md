# Fast Pixel Scanner

A highly optimized, cross-platform Python library for reading mouse positions and pixel colors on Windows and macOS.

## Installation

```bash
pip install fast-pixel
```

## Usage

### 1. Basic Tracking

Continuously track the mouse position and the color beneath it. (Note the use of `get_position_and_color` to do this in one call).

```python
import fast_pixel
import time

try:
    while True:
        (x, y), (r, g, b) = fast_pixel.get_position_and_color()
        print(f'X: {x} Y: {y} | RGB: ({r}, {g}, {b})', end = '\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nExiting...')
```

### 2. Waiting for a Color

Pause your script until a specific pixel turns a specific color.

```python
import fast_pixel

# Define your target: ((x, y), (R, G, B))
target = ((960, 700), (37, 74, 129))

print('Waiting for color...')
# Blocks until the color matches, checking every 0.05 seconds
if fast_pixel.wait_for_color(target, interval = 0.05):
    print('Color found!')
else:
    print('Timed out.')
```

## API Reference

* `get_position()`
Returns current mouse coordinates as a tuple: `(x, y)`.
* `get_color(x, y)` or `get_color((x, y))`
Returns the RGB color at the specified coordinates as a tuple: `(r, g, b)`.
* `get_position_and_color()`
Returns a nested tuple of the current position and color: `((x, y), (r, g, b))`.
* `wait_for_color(target, interval = 0.1)`
Blocks until the target coordinates match the target color. `target` can be passed as `((x, y), (r, g, b))`, `(x, y), (r, g, b)`, or `x, y, (r, g, b)`.
```