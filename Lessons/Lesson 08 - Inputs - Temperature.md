# Lesson 08 - Inputs - Temperature

## Overview

The Circuit Playground Express includes a built-in temperature sensor that measures the board’s temperature. Programs can read this value to respond to changes in environmental or device temperature.

## Syntax

This syntax reads the current temperature from the Circuit Playground Express sensor.

* `cp`: The Circuit Playground Express object that provides access to sensors and hardware features.
* `.temperature`: A property that reads the temperature from the built-in temperature sensor.
* `temperature_value`: A variable used to store the measured temperature for use in the program.
* The returned value is measured in degrees Celsius.

```python
# Read the current temperature from the sensor
temperature_value = cp.temperature
```

## Example

This program continuously reads the temperature sensor and prints the temperature value to the serial console.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time so we can pause between readings
import time

# Continuously read the temperature sensor
while True:

    # Read the temperature value
    temperature = cp.temperature

    # Print the temperature to the serial console
    print("Temperature:", temperature, "C")

    # Pause briefly before the next reading
    time.sleep(0.5)
```

## Example - Temperature Detecting Neopixels

This program changes the NeoPixel color depending on the temperature detected by the sensor.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for timing control
import time

# Set the NeoPixel brightness
cp.pixels.brightness = 0.2

# Continuously monitor the temperature
while True:

    # Read the temperature value
    temperature = cp.temperature

    # Turn pixels blue if the temperature is cold
    if temperature < 20:
        cp.pixels.fill((0, 0, 255))

    # Turn pixels green if the temperature is moderate
    elif temperature < 28:
        cp.pixels.fill((0, 255, 0))

    # Turn pixels red if the temperature is warm
    else:
        cp.pixels.fill((255, 0, 0))

    # Pause briefly before checking again
    time.sleep(0.5)
```
