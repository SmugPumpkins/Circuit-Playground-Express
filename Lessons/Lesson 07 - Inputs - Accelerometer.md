# Lesson 07 - Inputs - Accelerometer

## Overview

The Circuit Playground Express includes a built-in accelerometer that detects movement and orientation. Programs can read the device’s motion along three axes or detect actions like taps and shakes.

## `x`, `y`, and `z` Rotation

The accelerometer measures motion along three axes: left/right (`x`), forward/back (`y`), and up/down (`z`).

* `cp.acceleration`: Returns a tuple containing three values representing acceleration on the `x`, `y`, and `z` axes.
* `x, y, z`: Variables used to store the values for each axis.
* The values change when the board is tilted, moved, or rotated.
* These values can be printed or used in calculations to react to movement.

```python
# Read acceleration values from the accelerometer
x, y, z = cp.acceleration

# Print the values for each axis
print("X:", x)
print("Y:", y)
print("Z:", z)
```

## Tap Detection

The accelerometer can detect when the board is tapped.

* `cp.tapped`: A property that returns `True` when a tap is detected.
* `if cp.tapped`: Checks whether a tap occurred.
* This is commonly used to trigger actions when the board is tapped.

```python
# Check if the board was tapped
if cp.tapped:
    print("Tap detected!")
```

### Configuring Tap Detection

Tap detection can be configured to detect single taps or double taps.

* `cp.detect_taps`: Controls how many taps are required before detection triggers.
* `1`: Detects a single tap.
* `2`: Detects a double tap.
* After configuring this value, `cp.tapped` will trigger when the correct number of taps occurs.

```python
# Detect double taps
cp.detect_taps = 2
```

## Shake Detection

The accelerometer can also detect when the board is shaken.

* `cp.shake()`: A method that checks if a shake occurred.
* `if cp.shake()`: Runs code when a shake motion is detected.
* Shake detection is useful for triggering actions based on strong movement.

```python
# Check if the board was shaken
if cp.shake():
    print("Shake detected!")
```

### Configuring Shake Threshold

The shake detection sensitivity can be adjusted.

* `cp.shake_threshold`: Sets how strong the movement must be before a shake is detected.
* Higher values require stronger shaking.
* Lower values make shake detection more sensitive.

```python
# Increase the shake threshold so stronger movement is required
cp.shake_threshold = 30
```

## Example

This program continuously reads the accelerometer and prints the `x`, `y`, and `z` acceleration values to the serial console.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time so we can pause between readings
import time

# Continuously read the accelerometer values
while True:

    # Read acceleration values from the accelerometer
    x, y, z = cp.acceleration

    # Print the values for each axis
    print("X:", x, "Y:", y, "Z:", z)

    # Pause briefly before reading again
    time.sleep(0.5)
```

## Example - Angle Detection to Change Pitch

This program changes the pitch of the onboard speaker based on the tilt of the board.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time to slow the loop
import time

# Continuously check the tilt of the board
while True:

    # Read the acceleration values
    x, y, z = cp.acceleration

    # Convert the x tilt into a sound frequency
    frequency = int(440 + (x * 20))

    # Ensure the frequency stays within a safe range
    if frequency < 100:
        frequency = 100
    if frequency > 2000:
        frequency = 2000

    # Play the tone for a short duration
    cp.play_tone(frequency, 0.1)

    # Pause briefly before the next reading
    time.sleep(0.05)
```

## Example - Count Shakes on Neopixels

This program counts how many times the board is shaken and displays the count using NeoPixels.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for small delays
import time

# Set the NeoPixel brightness
cp.pixels.brightness = 0.2

# Start the shake counter
shake_count = 0

# Continuously check for shakes
while True:

    # Check if the board was shaken
    if cp.shake():

        # Increase the shake count
        shake_count += 1

        # Turn all pixels off first
        cp.pixels.fill((0, 0, 0))

        # Light one pixel for each shake detected
        for i in range(min(shake_count, 10)):
            cp.pixels[i] = (0, 255, 0)

    # Small delay to prevent rapid triggering
    time.sleep(0.1)
```

## Example - Count Taps on Neopixels

This program counts taps on the board and displays the total using NeoPixels.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for timing control
import time

# Configure tap detection for single taps
cp.detect_taps = 1

# Set the NeoPixel brightness
cp.pixels.brightness = 0.2

# Start the tap counter
tap_count = 0

# Continuously check for taps
while True:

    # Check if a tap was detected
    if cp.tapped:

        # Increase the tap counter
        tap_count += 1

        # Turn all pixels off first
        cp.pixels.fill((0, 0, 0))

        # Light one pixel for each tap detected
        for i in range(min(tap_count, 10)):
            cp.pixels[i] = (0, 0, 255)

    # Small delay to prevent rapid triggering
    time.sleep(0.1)
```
