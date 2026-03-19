# Lesson 12 - Outputs - Speaker

## Overview

The Circuit Playground Express includes a small onboard speaker that can generate tones and play simple sound files. Programs can use this speaker to play musical notes, sound effects, or respond to sensor input with audio feedback.

## Notes and Frequencies

The speaker generates sound by producing tones at specific frequencies. Musical notes correspond to specific frequency values measured in Hertz (Hz).

<details><summary>List of Piano Notes and Frequencies</summary>

| Note | Frequency (Hz) |
|------|----------------|
| B0   | 31             |
| C1   | 33             |
| CS1  | 35             |
| D1   | 37             |
| DS1  | 39             |
| E1   | 41             |
| F1   | 44             |
| FS1  | 46             |
| G1   | 49             |
| GS1  | 52             |
| A1   | 55             |
| AS1  | 58             |
| B1   | 62             |
| C2   | 65             |
| CS2  | 69             |
| D2   | 73             |
| DS2  | 78             |
| E2   | 82             |
| F2   | 87             |
| FS2  | 93             |
| G2   | 98             |
| GS2  | 104            |
| A2   | 110            |
| AS2  | 117            |
| B2   | 123            |
| C3   | 131            |
| CS3  | 139            |
| D3   | 147            |
| DS3  | 156            |
| E3   | 165            |
| F3   | 175            |
| FS3  | 185            |
| G3   | 196            |
| GS3  | 208            |
| A3   | 220            |
| AS3  | 233            |
| B3   | 247            |
| C4   | 262            |
| CS4  | 277            |
| D4   | 294            |
| DS4  | 311            |
| E4   | 330            |
| F4   | 349            |
| FS4  | 370            |
| G4   | 392            |
| GS4  | 415            |
| A4   | 440            |
| AS4  | 466            |
| B4   | 494            |
| C5   | 523            |
| CS5  | 554            |
| D5   | 587            |
| DS5  | 622            |
| E5   | 659            |
| F5   | 698            |
| FS5  | 740            |
| G5   | 784            |
| GS5  | 831            |
| A5   | 880            |
| AS5  | 932            |
| B5   | 988            |
| C6   | 1047           |
| CS6  | 1109           |
| D6   | 1175           |
| DS6  | 1245           |
| E6   | 1319           |
| F6   | 1397           |
| FS6  | 1480           |
| G6   | 1568           |
| GS6  | 1661           |
| A6   | 1760           |
| AS6  | 1865           |
| B6   | 1976           |
| C7   | 2093           |
| CS7  | 2217           |
| D7   | 2349           |
| DS7  | 2489           |
| E7   | 2637           |
| F7   | 2794           |
| FS7  | 2960           |
| G7   | 3136           |
| GS7  | 3322           |
| A7   | 3520           |
| AS7  | 3729           |
| B7   | 3951           |
| C8   | 4186           |
| CS8  | 4435           |
| D8   | 4699           |
| DS8  | 4978           |

</details>

## `play_tone()`

The `play_tone()` function plays a single tone for a specified duration.

* `cp.play_tone()`: A function that generates a tone using the speaker.
* `440`: The frequency of the tone in Hertz (Hz).
* `0.5`: The duration of the tone in seconds.
* The tone automatically stops when the duration is finished.

```python
cp.play_tone(440, 0.5)
```

## `start_tone()` and `stop_tone()`

These functions allow a tone to start and continue playing until it is manually stopped.

* `cp.start_tone()`: Begins playing a continuous tone.
* `440`: The frequency of the tone in Hertz.
* `cp.stop_tone()`: Stops the tone that is currently playing.
* This is useful when a tone should play while a condition remains true.

```python
cp.start_tone(440)
cp.stop_tone()
```

## `play_file()`

The speaker can also play `.wav` sound files stored on the board.

* `cp.play_file()`: Plays an audio file from the CIRCUITPY drive.
* `"sound.wav"`: The filename of the sound file to play.
* The file must be stored on the board’s filesystem.

```python
cp.play_file("sound.wav")
```

CircuitPlayground Express **cannot** play `.mp3` files. Many free online sound effects download as `.mp3` files. You may need to use an online `.mp3` to `.wav` converter.

The CircuitPlayground Express has very limited storage space. You also may need to use an online `.wav` compressor.

## Example

This program plays a simple scale using several musical notes.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for delays
import time

# List of note frequencies for a simple scale
notes = [262, 294, 330, 349, 392, 440, 494, 523]

# Play each note in the list
for note in notes:

    # Play the current note
    cp.play_tone(note, 0.3)

    # Small pause between notes
    time.sleep(0.05)
```

## Example - Accelerometer Trumpet

This program changes the pitch of the tone depending on how the board is tilted.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for loop control
import time

# Continuously read the accelerometer
while True:

    # Get the accelerometer values
    x, y, z = cp.acceleration

    # Convert tilt into a frequency
    frequency = int(440 + (x * 40))

    # Limit the frequency to a safe range
    if frequency < 200:
        frequency = 200
    if frequency > 2000:
        frequency = 2000

    # Play a short tone based on tilt
    cp.play_tone(frequency, 0.1)

    # Small delay between updates
    time.sleep(0.05)
```

## Example - Animated Neopixels and Speaker Sounds

This program plays tones while animating the NeoPixels with different colors.

```python
# Import the Circuit Playground Express library
from adafruit_circuitplayground import cp

# Import time for delays
import time

# Set NeoPixel brightness
cp.pixels.brightness = 0.2

# Define some notes
notes = [262, 330, 392, 523]

# Define some colors
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0)
]

# Play notes with matching colors
for i in range(len(notes)):

    # Set pixel color
    cp.pixels.fill(colors[i])

    # Play the corresponding note
    cp.play_tone(notes[i], 0.3)

    # Short delay before the next note
    time.sleep(0.05)

# Turn pixels off at the end
cp.pixels.fill((0, 0, 0))
```
