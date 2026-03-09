# Challenge 08 - Capacitive Touch Instrument
This challenge explores using the capacitive touch sensors and speaker.

## Mild 🌶️
Each sensor has 2 states, `True` or `False`.

For 3 of the sensors:

* Start a tone when a sensor is `True`.
* Stop the tone when the sensors are `False`.
* Each of the 3 sensors should play a different tone.

## Medium 🌶️🌶️
Each sensor has 2 states, `True` or `False`.

For all 7 of the sensors:

* Start a tone when a sensor is `True`.
* Stop the tone when the sensors are `False`.
* Each of the 7 sensors should have a different note that are part of a 7 note scale (see the frequency to note conversion in the `Lesson 12 - Outputs - Speaker`)

## Spicy 🌶️🌶️🌶️
Each sensor has 2 states, `True` or `False`.

For all 7 of the sensors:

* Start a tone when a sensor is `True`.
* Stop the tone when the sensors are `False`.
* Each of the 7 sensors should have a different note that are part of a 7 note scale (see the frequency to note conversion in the `Lesson 12 - Outputs - Speaker`)

When `Button A` is pressed, the notes all shift up 1 octave (for example, if it was B1 to start, it would shift to the B2 frequency).

When `Button B` is pressed, the notes all shift down 1 octave (for example, if it was B3, it would shift to the B2 frequency).

Pressing either `Button A` or `Button B` does not cause the frequencies to exceed the minimum or maximum threshold as noted in the frequency to note conversion in `Lesson 12 - Outputs - Speaker`.