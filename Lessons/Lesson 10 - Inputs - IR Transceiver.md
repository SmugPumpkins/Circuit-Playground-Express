# Lesson 10 - Inputs - IR Transceiver

## Overview

The Circuit Playground Express includes an infrared (IR) transmitter and receiver that allow boards to communicate wirelessly using infrared light. Programs can transmit encoded messages and receive them on another board to trigger actions or exchange data.

## Library Installation Instructions

The `adafruit_irremote` library must be available on the board.

1. Download the CircuitPython library bundle [(which can be found here)](https://circuitpython.org/libraries).
2. Unzip the bundle.
3. In the folder, open the `lib` folder.
4. Find the file called `adafruit_irremote.mpy`.
5. Copy `adafruit_irremote.mpy` into the `lib` folder of the CIRCUITPY drive.

For PyCharm to provide autocompletion for the `adafruit_irremote` library, you will need to install the following package for PyCharm.

```
adafruit-circuitpython-irremote
```

## TX and RX

Infrared communication uses two roles: transmitting (TX) and receiving (RX).

* **TX (Transmitter)**: Sends encoded infrared messages using the board’s IR LED.
* **RX (Receiver)**: Detects incoming infrared pulses and converts them into digital data.
* Both features can exist on the same board, allowing two-way communication.
* IR communication requires the transmitting LED to face the receiving sensor.

## Importing Libraries

These libraries provide access to the hardware and IR communication tools.

* `board`: Provides access to hardware pin definitions used by the IR transmitter and receiver.
* `pulseio`: Provides classes used to generate and measure timed pulses.
* `adafruit_irremote`: Provides encoding and decoding tools for IR messages.

```python
import board
import pulseio
import adafruit_irremote
```

## IR Communication Principles

### Pulses and Timing

Infrared communication works by sending pulses of infrared light with precise timing patterns. The transmitter rapidly turns the IR LED on and off to create pulses, while the receiver measures how long each pulse lasts. Different pulse lengths represent different pieces of information, and the timing between pulses is used to separate bits and messages.

### Encoding and Decoding

Messages are not sent as normal numbers or characters. Instead, they are converted into patterns of timed pulses through an encoding process. The receiver measures the incoming pulse timings and decodes them back into digital values. Encoders define how data is converted into pulse patterns, while decoders interpret those patterns and reconstruct the original message.

## Transmitting

### `PulseOut` Object

A `PulseOut` object generates the timed pulses that drive the infrared transmitter.

* `pulseout`: A variable storing the pulse output object.
* `pulseio.PulseOut()`: Creates an object capable of generating timed pulses.
* `board.IR_TX`: The pin connected to the infrared transmitter LED.
* `frequency=38000`: The carrier frequency used by most IR communication protocols.
* `duty_cycle=2 ** 15`: Controls how much of each cycle the signal stays on.

```python
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
```

### Encoder

An encoder converts digital data into a sequence of pulses that represent binary values.

* `encoder`: A variable storing the encoder object.
* `adafruit_irremote.GenericTransmit()`: Creates an encoder using configurable pulse timings.
* `header=[9000, 4500]`: The starting pulse pattern that signals the beginning of a message.
* `one=[560, 1700]`: Pulse timing used to represent a binary `1`.
* `zero=[560, 560]`: Pulse timing used to represent a binary `0`.
* `trail=0`: The trailing pulse at the end of the transmission.

```python
encoder = adafruit_irremote.GenericTransmit(
    header=[9000, 4500],
    one=[560, 1700],
    zero=[560, 560],
    trail=0
)
```

### Sending Messages

Once an encoder and transmitter exist, messages can be transmitted.

* `encoder.transmit()`: Sends encoded data using the IR transmitter.
* `pulseout`: The `PulseOut` object responsible for generating pulses.
* `[255, 2, 255, 0]`: A list of byte values representing the message being sent.
* Each number in the list represents a single byte of transmitted data.

```python
encoder.transmit(pulseout, [255, 2, 255, 0])
```

### Limitations

Infrared communication becomes less reliable as messages grow longer because the transmission takes more time and increases the chance of interference or missed pulses.

| # of bytes  | Approximate Time | Likely to Succeed             |
| ----------- | ---------------- | ----------------------------- |
| 1-4 bytes   | ~60 ms           | Extremely likely to succeed   |
| 5-16 bytes  | ~240 ms          | Very likely to succeed        |
| 17-32 bytes | ~0.5 seconds     | Unlikely to succeed           |
| 33-64 bytes | ~1 second        | Very unlikely to succeed      |
| 65+ bytes   | 1+ seconds       | Extremely unlikely to succeed |

## Receiving

### `PulseIn` Object

A `PulseIn` object records incoming pulse timings from the infrared receiver.

* `pulsein`: A variable storing the pulse input object.
* `pulseio.PulseIn()`: Creates an object that measures pulse timings.
* `board.IR_RX`: The pin connected to the infrared receiver.
* `maxlen=120`: The maximum number of pulses that can be stored.
* `idle_state=True`: Indicates the signal’s resting state.

```python
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
```

### Decoder

A decoder converts incoming pulse timings into digital message values.

* `decoder`: A variable storing the decoder object.
* `adafruit_irremote.GenericDecode()`: Creates a decoder capable of interpreting generic IR messages.

```python
decoder = adafruit_irremote.GenericDecode()
```

### Receiving Messages

The decoder reads pulses from the receiver and stores them for decoding.

* `decoder.read_pulses()`: Waits for an incoming IR message.
* `pulsein`: The pulse input object receiving the signal.
* `pulses`: A variable storing the captured pulse timings.

```python
pulses = decoder.read_pulses(pulsein)
```

### Error Prevention

Sometimes pulse data cannot be decoded properly. A `try/except` block prevents the program from crashing when this happens.

* `try`: Attempts to decode the captured pulses.
* `decoder.decode_bits()`: Converts the pulse data into a message.
* `pulses`: The captured pulse timings.
* `except adafruit_irremote.IRDecodeException`: Catches decoding errors.
* `continue`: Skips the current loop iteration and waits for another message.

```python
try:
    message = decoder.decode_bits(pulses)
except adafruit_irremote.IRDecodeException:
    continue
```

## Example - Transmission

This program sends different IR messages depending on which button is pressed on the Circuit Playground Express.

```python
# Import libraries
import board
import pulseio
import adafruit_irremote
from adafruit_circuitplayground import cp
import time

# Create PulseOut object
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)

# Create an encoder
encoder = adafruit_irremote.GenericTransmit(
    header=[9000, 4500],
    one=[560, 1700],
    zero=[560, 560],
    trail=0
)

# Define some messages
message_a = [255, 1, 255, 1]
message_b = [1, 255, 1, 255]
message_both = [127, 1, 127, 255]
message_neither = [1, 127, 255, 127]

# Main loop
while True:

    # Button logic
    if cp.button_a and not cp.button_b:
        encoder.transmit(pulseout, message_a)  # Send message
    elif cp.button_b and not cp.button_a:
        encoder.transmit(pulseout, message_b)  # Send message
    elif cp.button_a and cp.button_b:
        encoder.transmit(pulseout, message_both)  # Send message
    else:
        encoder.transmit(pulseout, message_neither)  # Send message
    
    # Delay at end of loop so message doesn't get cut off
    time.sleep(0.2)
```

## Example - Receiver

This program listens for incoming IR messages and prints which message was received.

```python
# Import libraries
import board
import pulseio
import adafruit_irremote

# Create PulseIn object
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)

# Create decoder object
decoder = adafruit_irremote.GenericDecode()

# Define some messages
message_a = [255, 1, 255, 1]
message_b = [1, 255, 1, 255]
message_both = [127, 1, 127, 255]
message_neither = [1, 127, 255, 127]

while True:
    # Read the pulses
    pulses = decoder.read_pulses(pulsein)

    # In case there would be an error we use a try / except block
    try:
        message = decoder.decode_bits(pulses)
    except adafruit_irremote.IRDecodeException:
        continue

    # Print logic
    if message == message_a:
        print("A button pressed!")
    elif message == message_b:
        print("B button pressed!")
    elif message == message_both:
        print("Both buttons pressed!")
    elif message == message_neither:
        print("Neither button pressed!")
```

## Example - Transceiving

This example shows how a board can both receive and transmit IR messages by temporarily pausing the receiver during transmission.

```python
# Import libraries
import board
import pulseio
import adafruit_irremote

# Create transmitter and receiver objects
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)

# Create decoder and encoder
decoder = adafruit_irremote.GenericDecode()
encoder = adafruit_irremote.GenericTransmit(
    header=[9000, 4500],
    one=[560, 1700],
    zero=[560, 560],
    trail=0
)

while True:

    # Listen for incoming pulses
    pulses = decoder.read_pulses(pulsein)

    # Attempt to decode the message
    try:
        message = decoder.decode_bits(pulses)
    except adafruit_irremote.IRDecodeException:
        continue

    # If a specific message is received, send a response
    if message == [1, 2, 3, 4]:

        # Pause the receiver before transmitting
        pulsein.pause()

        # Transmit the response message
        encoder.transmit(pulseout, [9, 9, 9, 9])

        # Resume the receiver
        pulsein.resume()
```
