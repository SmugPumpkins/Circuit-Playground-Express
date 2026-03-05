# Lesson 05 - Inputs - Capacitive Touch

## Overview

The CircuitPlayground Express has seven capacitive touch pads located around the edge of the device.

![Capacitive Touch Pads](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/capacitive_touch_pads.jpg)

## Reading Capacitive Touch Values

Each capacitive touch pad returns `True` when it is being touched and `False` when it is not.

* `cp`: The Circuit Playground object used to access hardware features.
* `cp.touch_A1`: Reads the touch state of pad A1.
* `True`: Returned when the pad is being touched.
* `False`: Returned when the pad is not being touched.

```python
# Check if pad A1 is being touched
cp.touch_A1
```

* `cp.touch_A2`: Reads the touch state of pad A2.

```python
# Check if pad A2 is being touched
cp.touch_A2
```

* `cp.touch_A3`: Reads the touch state of pad A3.

```python
# Check if pad A3 is being touched
cp.touch_A3
```

* `cp.touch_A4`: Reads the touch state of pad A4.

```python
# Check if pad A4 is being touched
cp.touch_A4
```

* `cp.touch_A5`: Reads the touch state of pad A5.

```python
# Check if pad A5 is being touched
cp.touch_A5
```

* `cp.touch_A6`: Reads the touch state of pad A6.

```python
# Check if pad A6 is being touched
cp.touch_A6
```

* `cp.touch_TX`: Reads the touch state of the TX pad (this pad is not labeled A7).
* `True`: Returned when the TX pad is being touched.
* `False`: Returned when the TX pad is not being touched.

```python
# Check if the TX pad is being touched
cp.touch_TX
```

## Example

This example continuously checks all touch pads and prints which ones are currently being touched.

```python
from adafruit_circuitplayground import cp

# Continuously monitor all touch pads
while True:
    # Check each touch pad individually
    if cp.touch_A1:
        print("Touching A1")
    if cp.touch_A2:
        print("Touching A2")
    if cp.touch_A3:
        print("Touching A3")
    if cp.touch_A4:
        print("Touching A4")
    if cp.touch_A5:
        print("Touching A5")
    if cp.touch_A6:
        print("Touching A6")
    if cp.touch_TX:
        print("Touching TX")
```

## Example - If At Least One of Multiple is Pressed

This example turns the onboard red LED on if either A1 or A2 is being touched.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp

# Continuously check the touch pads
while True:
    # If A1 OR A2 is being touched
    if cp.touch_A1 or cp.touch_A2:
        # Turn the onboard red LED on
        cp.red_led = True
    else:
        # Turn the onboard red LED off
        cp.red_led = False
```

## Example - If Multiple Need to Be Pressed

This example turns the onboard red LED on only if both A1 and A2 are being touched at the same time.

```python
# Import the Circuit Playground library
from adafruit_circuitplayground import cp

# Continuously check the touch pads
while True:
    # If A1 AND A2 are being touched at the same time
    if cp.touch_A1 and cp.touch_A2:
        # Turn the onboard red LED on
        cp.red_led = True
    else:
        # Turn the onboard red LED off
        cp.red_led = False
```
