# Challenge 03 - Shake Light
This challenge explores using the built in accelerometer and built in Neopixels.
## Mild 🌶️
When shaken, the shake detection is set to `True`, and otherwise is set to `False`.

When shaken is `True`:
* Turn on the Neopixel lights.
## Medium 🌶️🌶️
When shaken, the shake detection is set to `True`, and otherwise is set to `False`. You will also need a variable to track the Neopixel state.

When shaken is `True` and the lights are off:
* Turn on the lights.

When shaken is `True` and the lights are on:
* Turn off the lights.
## Spicy 🌶️🌶️🌶️
When shaken, the shake detection is set to `True`, and otherwise is set to `False`. You will also need some variables to track the Neopixel state.

When shaken is `True` and the lights are off:
* Turn on the lights as a different color than the color they were previously. 
    * *For example, the first time the lights turn on they could be blue. The second time they turn on, they could be red. The third time they turn on, they could be blue again OR they could be a third new color.*

When shaken is `True` and the lights are on:
* Turn off the lights.