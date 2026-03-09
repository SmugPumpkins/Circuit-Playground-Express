# Challenge 09 - Microphone Neopixels
This challenge explores using the microphone input and the Neopixels.

## Mild 🌶️
Using the example volume detector, make it so that when the microphone detects a loud volume, the Neopixels turn red.

When the microphone detects a quiet volume, the Neopixels turn green.


## Medium 🌶️🌶️
Using the example volume detector, make it so that when the microphone can change color depending on volume levels that you determine:

| Volume Level  | Neopixel Color  |
|:-------------:|:---------------:|
|  Very Quiet   |      Green      |
|     Quiet     |     Yellow      |
|    Medium     |     Orange      |
|     Loud      |       Red       |

## Spicy 🌶️🌶️🌶️
Using the example volume detector, create a volume detector that lights up more Neopixels as the volume decreases.

* Determine a minimum volume threshold.
* Determine a maximum volume threshold.
* When the volume is at or below the minimum threshold, have 1 neopixel lit up.
* When the volume is at or above the maximum threshold, have all 10 neopixels lit up.
* For any volume between the minimum and maximum threshold, the number of pixels lit up should change based on the current volume level.

*(It's a volume detector, don't overthink it too much!)*