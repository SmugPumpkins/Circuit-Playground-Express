# Lesson 11 - Outputs - Builtin LED

## Overview

The Circuit Playground Express includes a built-in red LED that can be turned on or off through code. Programs can control this LED to provide simple visual feedback or indicators.

## Syntax

The built-in red LED can be controlled using the `cp.red_led` property.

* `cp`: The Circuit Playground Express object used to access onboard hardware.
* `.red_led`: A property that controls the state of the built-in red LED.
* `True`: Turns the LED on.
* `False`: Turns the LED off.

```python
cp.red_led = True
```

## Example - Blink

This program repeatedly turns the built-in LED on and off to create a blinking effect.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time so we can pause between LED changes
import time

# Continuously blink the LED
while True:

    # Turn the LED on
    cp.red_led = True

    # Wait half a second
    time.sleep(0.5)

    # Turn the LED off
    cp.red_led = False

    # Wait half a second
    time.sleep(0.5)
```

## Example - Toggled with Buttons

This program turns the LED on when button A is pressed and turns it off when button B is pressed.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Continuously check button inputs
while True:

    # Turn the LED on if button A is pressed
    if cp.button_a:
        cp.red_led = True

    # Turn the LED off if button B is pressed
    if cp.button_b:
        cp.red_led = False
```

## Example - Record Pattern with Button A, Make Pattern With Button B

This program records a sequence of button presses while recording mode is active and plays the pattern back later. The red LED indicates recording mode, while NeoPixels display the pattern in red during recording and green during playback.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for delays
import time

# Set NeoPixel brightness
cp.pixels.brightness = 0.2

# List to store the recorded pattern
pattern = []

# Track recording mode
recording = False

# Main program loop
while True:

    # Start or stop recording with Button A
    if cp.button_a:

        # Toggle recording mode
        recording = not recording

        # Turn the red LED on when recording, off otherwise
        cp.red_led = recording

        # If starting a new recording, clear previous pattern
        if recording:
            pattern = []

        # Delay to prevent multiple triggers
        time.sleep(0.4)

    # If recording mode is active
    if recording:

        # Record whether Button B is pressed
        press = cp.button_b
        pattern.append(press)

        # Clear pixels before displaying state
        cp.pixels.fill((0, 0, 0))

        # Show recorded presses in red
        for i in range(min(len(pattern), 10)):
            if pattern[i]:
                cp.pixels[i] = (255, 0, 0)

        # Delay between recorded steps
        time.sleep(0.2)

    # If not recording and Button B is pressed, play the pattern
    elif cp.button_b and pattern:

        # Turn off the recording indicator
        cp.red_led = False

        # Play the pattern using green pixels
        for state in pattern:

            # Clear all pixels
            cp.pixels.fill((0, 0, 0))

            # Display the current step
            if state:
                cp.pixels[0] = (0, 255, 0)

            # Delay between playback steps
            time.sleep(0.2)

        # Small delay after playback
        time.sleep(0.3)
```

