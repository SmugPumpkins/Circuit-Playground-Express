# Challenge 02 - Light Pitch
This challenge explores using the built-in photoresistor (light detection) and built in passive buzzer.
## Mild 🌶️
The photoresistor returns an `int` relative to the amount of light it detects. You will need to create a variable to set a `threshold` value.

If the amount of light is greater than the `threshold`:

* Start a tone

If the amount of light is less than the `threshold`:

* Stop the tone
## Medium 🌶️🌶️
The photoresistor returns an `int` relative to the amount of light it detects. You will need to create 3 variables to set some `threshold` values.

If the amount of light is greater than the first `threshold` value:

* Stop the current tone
* Start a tone at a certain pitch

If the amount of light is greater than the second `threshold` value:

* Stop the current tone
* Start a tone at a higher pitch than the first value

If the amount of light is greater than the third `threshold` value:

* Stop the current tone
* Start a tone at a higher pitch than the second value

If the amount of light is less than eny of the `threshold` values:

* Stop the tone


## Spicy 🌶️🌶️🌶️
The photoresistor returns an `int` relative to the amount of light it detects.

Process the brightness `int` value:

* Set a pitch relative to the brightness value. 
* Continuously change the pitch relative to the detected brightness.