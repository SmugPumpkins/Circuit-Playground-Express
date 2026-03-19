# Lesson 13 - Outputs - Neopixels

## Overview

The Circuit Playground Express contains 10 built-in RGB NeoPixels arranged in a ring. Each NeoPixel can display a wide range of colors and can be controlled individually or all at once to create lighting effects and visual feedback.

## Brightness

NeoPixel brightness can be adjusted to control how bright the LEDs appear.

* `cp.pixels`: The NeoPixel object controlling the LED ring.
* `.brightness`: A value between `0.0` and `1.0` that controls overall brightness.
* Lower brightness values reduce power usage and glare.

This brightness is a good level for testing.

* `0.025`: A low brightness value that is comfortable when working close to the board.

```python
cp.pixels.brightness = 0.025
```

This brightness is a good level for presenting.

* `0.2`: A brighter value that is easier to see from a distance.

```python
cp.pixels.brightness = 0.2
```

## Change All Neopixels With `fill()`

The `fill()` method sets all NeoPixels to the same color at once.

* `cp.pixels.fill()`: Changes the color of every NeoPixel on the board.
* `(255, 0, 0)`: A tuple representing a color value.
* Each value corresponds to red, green, and blue intensity.

```python
cp.pixels.fill((255, 0, 0))
```

### RGB Values

RGB colors are defined using three numbers representing red, green, and blue intensity.

* `(R, G, B)`: A tuple containing red, green, and blue values.
* Each value ranges from `0` to `255`.
* `(255, 0, 0)`: Full red.
* `(0, 255, 0)`: Full green.
* `(0, 0, 255)`: Full blue.

```python
cp.pixels.fill((0, 255, 0))
```

### Hex Values

Colors can also be defined using hexadecimal values.

* `0xRRGGBB`: A hexadecimal representation of a color.
* `0xFF0000`: Red.
* `0x00FF00`: Green.
* `0x0000FF`: Blue.

```python
cp.pixels.fill(0x0000FF)
```

## Changing Individual Neopixels

Each NeoPixel can be controlled individually using its index.

* `cp.pixels[index]`: Accesses a specific NeoPixel.
* `index`: The position of the pixel (0–9).
* `(255, 255, 0)`: The color assigned to that pixel.

```python
cp.pixels[0] = (255, 255, 0)
```

## Example

This program turns all NeoPixels red.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Set brightness
cp.pixels.brightness = 0.025

# Turn all pixels red
cp.pixels.fill((255, 0, 0))
```

## Example - Change Brightness With Buttons

This program increases NeoPixel brightness when button A is pressed and decreases brightness when button B is pressed. The brightness value is clamped between `0.025` and `1`.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for button debounce
import time

# Set starting brightness
brightness = 0.2
cp.pixels.brightness = brightness

# Turn pixels on so brightness changes are visible
cp.pixels.fill((0, 255, 0))

# Main loop
while True:

    # Increase brightness with button A
    if cp.button_a:
        brightness += 0.05

        # Clamp to maximum brightness
        if brightness > 1:
            brightness = 1

        cp.pixels.brightness = brightness
        time.sleep(0.2)

    # Decrease brightness with button B
    if cp.button_b:
        brightness -= 0.05

        # Clamp to minimum brightness
        if brightness < 0.025:
            brightness = 0.025

        cp.pixels.brightness = brightness
        time.sleep(0.2)
```


## Example - Light Neopixels With Capacitive Touch

This program lights NeoPixels depending on which capacitive touchpad is touched.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Set brightness
cp.pixels.brightness = 0.025

# Main loop
while True:

    # Clear pixels
    cp.pixels.fill((0, 0, 0))

    # Check each capacitive touch pad
    if cp.touch_A1:
        cp.pixels[6] = (255, 0, 0)
        cp.pixels[7] = (255, 0, 0)

    if cp.touch_A2:
        cp.pixels[7] = (255, 128, 0)
        cp.pixels[8] = (255, 128, 0)

    if cp.touch_A3:
        cp.pixels[8] = (255, 255, 0)
        cp.pixels[9] = (255, 255, 0)

    if cp.touch_A4:
        cp.pixels[0] = (0, 255, 0)
        cp.pixels[1] = (0, 255, 0)

    if cp.touch_A5:
        cp.pixels[1] = (0, 255, 255)
        cp.pixels[2] = (0, 255, 255)

    if cp.touch_A6:
        cp.pixels[2] = (0, 0, 255)
        cp.pixels[3] = (0, 0, 255)

    if cp.touch_TX:
        cp.pixels[3] = (128, 0, 255)
        cp.pixels[4] = (128, 0, 255)

    # Small delay for stability
    import time
    time.sleep(0.05)
```

## Example - Stationary Rainbow

This program displays a rainbow pattern around the NeoPixel ring.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Set brightness
cp.pixels.brightness = 0.025

# Define rainbow colors
colors = [
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (128, 0, 255),
    (255, 0, 255),
    (255, 0, 128),
    (255, 255, 255)
]

# Assign colors to each pixel
for i in range(10):
    cp.pixels[i] = colors[i]
```
