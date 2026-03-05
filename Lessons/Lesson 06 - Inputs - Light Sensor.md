# Lesson 06 - Inputs - Light Sensor (Photoresistor)

## Overview

The Circuit Playground Express includes a built-in light sensor that measures the brightness of the surrounding environment. Programs can read this value and use it to react to changes in lighting.

## Syntax

This syntax reads the current light level detected by the Circuit Playground Express light sensor.

* `cp`: The Circuit Playground Express object that gives access to the board’s sensors and hardware.
* `.light`: A property that reads the current brightness level from the built-in light sensor.
* `light_value`: A variable used to store the measured light level so it can be used later in the program.
* The returned number increases as the environment becomes brighter.

```python
# Read the current light level from the sensor
light_value = cp.light
```

## Using the Numerical Values

The light sensor returns a number representing the brightness of the environment, which can be used in conditions or calculations.

* `light_level`: A variable that stores the current brightness value from the sensor.
* `cp.light`: Reads the brightness detected by the sensor.
* `if light_level > 200`: Checks if the environment is bright.
* `print()`: Displays a message depending on the brightness level.

```python
# Store the current light level
light_level = cp.light

# Check if the environment is bright or dark
if light_level > 100:
    print("It is bright!")
else:
    print("It is dark!")
```

## Example

This program continuously reads the light sensor and prints the brightness value to the serial console.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time so we can pause between readings
import time

# Continuously read the light sensor
while True:

    # Read the current light level from the sensor
    light_level = cp.light

    # Print the light value to the serial console
    print("Light Level:", light_level)

    # Pause briefly before taking the next reading
    time.sleep(0.5)
```

## Example - Neopixel Light Loader

This program uses the light sensor to determine how many NeoPixels should turn on. Brighter environments will light more pixels, while darker environments will light fewer.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time so the program doesn't update too quickly
import time

# Set the NeoPixel brightness
cp.pixels.brightness = 0.02

# Continuously check the light level
while True:

    # Read the brightness from the light sensor
    light_level = cp.light

    # Convert the light level into a number of pixels to light
    # The value is scaled so brighter light turns on more pixels
    pixels_to_light = light_level // 25

    # Limit the number of pixels so it never exceeds 10
    if pixels_to_light > 10:
        pixels_to_light = 10

    # Turn all pixels off first
    cp.pixels.fill((0, 0, 0))

    # Turn on the required number of pixels
    for i in range(pixels_to_light):
        cp.pixels[i] = (255, 255, 0)

    # Pause briefly before updating again
    time.sleep(0.1)
```
