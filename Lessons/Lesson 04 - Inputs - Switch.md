# Lesson 04 - Inputs - Switch

## Overview

Like the buttons, the switch will be in one of two states. The switch is located in the center of the CircuitPlayground Express, between the music note and the ear.

![Switch](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/slide_switch.jpg)

## Switch Value

The switch will be `True` when it is in the left position (next to the music note), and will be `False` when it is in the right position (next to the ear).

* `cp`: The Circuit Playground object used to access hardware features.
* `cp.switch`: A property that reads the current position of the slide switch.
* `True`: Returned when the switch is in the left position (music note side).
* `False`: Returned when the switch is in the right position (ear side).

```python
# Read the current position of the slide switch
cp.switch
```

## Example

This example continuously checks the slide switch and turns the onboard red LED on when the switch is left, and off when the switch is right.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp

# Continuously check the switch position
while True:
    # If the switch is in the left position (music note side)
    if cp.switch:
        # Turn the onboard red LED on
        cp.red_led = True
    else:
        # Turn the onboard red LED off
        cp.red_led = False
```
