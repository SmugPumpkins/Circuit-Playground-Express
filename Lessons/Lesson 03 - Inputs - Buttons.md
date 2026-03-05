# Lesson 03 - Inputs - Buttons

## Overview

Buttons allow users to provide input to the Circuit Playground Express. The board can detect whether a button is pressed (`True`) or not pressed (`False`) and respond accordingly.

---

## Reset Button

The reset button is used to restart the Circuit Playground Express or prepare it for bootloading new firmware. It cannot be programmed or read in code.

![Reset Buttton](https://cdn-learn.adafruit.com/assets/assets/000/076/510/medium640/educators_circuitpy_reset_button.jpg?1559761014)

---

## Button A

Button A is labeled with an `A` and is on the left side of the CircuitPlayground Express.

![Button A](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/button_a.jpg)

Button A will be in one of two states. When it is pressed, `cp.button_a` is `True`. When the button is not pressed, `cp.button_a` will be `False`.

* `cp` is the main object that gives access to the board’s hardware.
* `.button_a` checks the current state of Button A.

```python
# Check if Button A is pressed
cp.button_a
```

---

## Button B

Button B is labeled with a `B` and is on the right side of the CircuitPlayground Express.

![Button B](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/button_b.jpg)

Button B will be in one of two states. When it is pressed, `cp.button_b` is `True`. When the button is not pressed, `cp.button_b` will be `False`.

* `cp` is the main object that gives access to the board’s hardware.
* `.button_b` checks the current state of Button B.

```python
# Check if Button B is pressed
cp.button_b
```

---

## Example

This example continuously checks Button A and prints its state to the serial console.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp

# Main Loop (Runs Forever)

while True:

    # Check if Button A is pressed
    if cp.button_a:
        print("Button A is pressed!")
    else:
        print("Button A is not pressed.")
```

---

## Example - Flash Neopixels With Button

This example turns all NeoPixels green while Button A is pressed and turns them off when it is not pressed.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp

# Initial Setup

# Turn all pixels off at the start
cp.pixels.fill((0, 0, 0))

# Main Loop

while True:

    # If Button A is pressed
    if cp.button_a:

        # Turn all pixels green
        cp.pixels.fill((0, 255, 0))

    else:

        # Turn all pixels off
        cp.pixels.fill((0, 0, 0))
```

---

## Example - Button A, Button B, Neither, or Both

This example changes the NeoPixel color depending on which buttons are pressed.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp

# Initial Setup

# Turn all pixels off at the start
cp.pixels.fill((0, 0, 0))

# Main Loop

while True:

    # If both buttons are pressed
    if cp.button_a and cp.button_b:

        # Set pixels to purple
        cp.pixels.fill((255, 0, 255))

    # If only Button A is pressed
    elif cp.button_a:

        # Set pixels to red
        cp.pixels.fill((255, 0, 0))

    # If only Button B is pressed
    elif cp.button_b:

        # Set pixels to blue
        cp.pixels.fill((0, 0, 255))

    # If neither button is pressed
    else:

        # Turn all pixels off
        cp.pixels.fill((0, 0, 0))
```
