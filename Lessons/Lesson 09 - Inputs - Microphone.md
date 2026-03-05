# Lesson 09 - Inputes - Microphone

## Overview

The Circuit Playground Express includes a built-in microphone that can detect sound levels from the environment. Programs can read microphone samples and analyze them to determine how loud the surrounding sound is.

## Library Imports

These libraries are required to access the microphone and process sound samples.

* `array`: Provides a way to store large sets of numeric data efficiently.
* `math`: Provides mathematical functions such as square root for sound calculations.
* `time`: Allows the program to pause between readings.
* `audiobusio`: Contains the `PDMIn` class used to access the microphone hardware.
* `board`: Provides access to hardware pin definitions used by the microphone.

```python
import array
import math
import time
import audiobusio
import board
```

## `PDMIn` Object

The microphone is accessed by creating a `PDMIn` object that connects to the board’s microphone hardware.

* `mic`: A variable storing the microphone object.
* `audiobusio.PDMIn()`: Creates an interface to the microphone.
* `board.MICROPHONE_CLOCK`: The pin used to send the clock signal to the microphone.
* `board.MICROPHONE_DATA`: The pin used to receive microphone data.
* `sample_rate=16000`: The number of audio samples captured per second.
* `bit_depth=16`: The number of bits used to represent each audio sample.

```python
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)
```

## Storing and Recording Samples

Microphone recordings are stored in an array that holds the captured audio samples.

* `samples`: A variable that stores the array used to hold microphone data.
* `array.array()`: Creates a fixed-type numeric array for storing sample values.
* `'H'`: Specifies that the array will store unsigned 16-bit integers.
* `[0] * 160`: Creates 160 positions in the array, each initialized to `0`.
* This array will later be filled with audio samples recorded from the microphone.

```python
samples = array.array('H', [0] * 160)
```

Microphone samples are recorded into the array using the microphone object.

* `mic`: The microphone object created earlier using `audiobusio.PDMIn`.
* `.record()`: A method that records audio data from the microphone.
* `samples`: The array that will receive the recorded sample values.
* `len(samples)`: Specifies the number of samples that should be recorded.
* After this line runs, the `samples` array will contain the recorded audio data.

```python
mic.record(samples, len(samples))
```


## Volume Detection

This function analyzes microphone samples to calculate the loudness of the recorded sound.

* `sound_level(samples)`: A function that calculates the volume level from a sample array.
* `mean`: The average value of all samples.
* `total`: A variable used to accumulate squared differences.
* `(sample - mean) ** 2`: Measures how far each sample is from the average value.
* `math.sqrt()`: Calculates the square root to produce a final volume level.

```python
def sound_level(samples):
    mean = sum(samples) / len(samples)
    total = 0
    for sample in samples:
        total += (sample - mean) ** 2
    return math.sqrt(total / len(samples))
```

## Example

This program continuously records microphone samples and prints the detected sound level to the serial console.

```python
# Import required libraries for microphone input and calculations
import array
import math
import time
import audiobusio
import board

# Create the microphone object
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# Create an array to store audio samples
samples = array.array('H', [0] * 160)

# Function to calculate sound level from samples
def sound_level(samples):
    mean = sum(samples) / len(samples)
    total = 0
    for sample in samples:
        total += (sample - mean) ** 2
    return math.sqrt(total / len(samples))

# Continuously record and measure sound levels
while True:

    # Record microphone samples into the array
    mic.record(samples, len(samples))

    # Calculate the sound level
    level = sound_level(samples)

    # Print the detected sound level
    print("Sound Level:", level)

    # Pause briefly before recording again
    time.sleep(0.1)
```

## Example - Builtin LED Volume Detection

This program turns on the built-in LED when the microphone detects a loud sound.

```python
# Import required libraries for microphone input and calculations
import array
import math
import time
import audiobusio
import board
import digitalio

# Create a digital output for the built-in LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Create the microphone object
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# Create an array to store audio samples
samples_array = array.array('H', [0] * 160)

# Function to calculate sound level
def sound_level(samples):
    mean = sum(samples) / len(samples)
    total = 0
    for sample in samples:
        total += (sample - mean) ** 2
    return math.sqrt(total / len(samples))

# Continuously monitor the microphone
while True:

    # Record microphone samples
    mic.record(samples_array, len(samples_array))

    # Calculate the sound level
    level = sound_level(samples_array)

    # Turn the LED on if the sound level is high
    if level > 200:
        led.value = True
    else:
        led.value = False

    # Small delay before repeating
    time.sleep(0.05)
```
