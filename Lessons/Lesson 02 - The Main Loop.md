# Lesson 02 - The Main Loop

## Overview

The main loop is the part of a Circuit Playground Express program that runs continuously. It allows the board to constantly check inputs and respond with outputs.

---

## Setting Up Imported Libraries

This section imports the libraries needed to control the Circuit Playground Express hardware.

* `from adafruit_circuitplayground import cp` imports the `cp` object.
* `cp` gives access to built-in hardware like buttons, LEDs, the speaker, and sensors.
* `import` tells Python to load external code so we can use it in our program.

```python
from adafruit_circuitplayground import cp
```

---

## Setting Up Initial Values Before the Loop

Initial values are created before the loop so they can be reused and updated while the program runs.

* `led_index = 0` creates a variable named `led_index`.
* `0` is the starting value that represents the first onboard LED.
* Variables defined before the loop can change inside the loop.

```python
# Create a variable to track which LED is on
led_index = 0
```

---

## Creating a Loop for I/O

A `while True` loop runs forever, allowing the board to constantly read inputs and control outputs.

* `while True:` creates an infinite loop.
* `True` always evaluates as true, so the loop never stops.
* `pass` is a placeholder that does nothing.
* The indented block is the code that repeats continuously.

```python
while True:
    # Replace 'pass' with input and output code from the CircuitPlayground Express that will go here
    pass
```

---

## Example - Putting it All Together

This example continuously checks if Button A is pressed and turns the first LED on while the button is held down.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp


# Initial Setup (Before the Loop)

# Turn all LEDs off at the start
cp.pixels.fill((0, 0, 0))


# Main Loop (Runs Forever)

while True:

    # Check if Button A is pressed
    if cp.button_a:

        # Turn LED 0 red when pressed
        cp.pixels[0] = (255, 0, 0)

    else:

        # Turn LED 0 off when not pressed
        cp.pixels[0] = (0, 0, 0)
```
