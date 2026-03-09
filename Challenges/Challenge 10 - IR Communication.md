# Challenge 10 - IR Communication
This challenge requires a partner and explores using the IR communication module for the device!

## Mild 🌶️
Have one partner upload the Transmitter sample code, and the second partner upload the Receiver sample code. 

* Demonstrate that the IR communication is working to Mr. Forsyth.
* Switch roles and reupload the code.
* Demonstrate that the IR communication is working to Mr. Forsyth again.


## Medium 🌶️🌶️
Modify the sample code so that you have 10 custom messages that can be sent between the 2 IR devices.

* When the A button is pressed, the next custom message in the list should be sent.
* When the B button is pressed, the previous custom message in the list should be sent.
* The messages being sent should wrap around. For example, if I pressed the B button when it was on the first message, it should wrap around to the 10th message. If I pressed the A button on the 10th message, it should wrap around to the first message.
* The important thing here is that there should be 10 unique patterns set up to be communicated over IR.

## Spicy 🌶️🌶️🌶️
Modify the code so that both Circuit Playground Devices and Transmit and Receive Messages. 

* Each device should send a specific message when Button A is pressed.
* Each device should send a specific message if it receives the Button A massage from the other device.

For example, you would need to have the following 2 scenarios.

**Scenario 1:**

* Button A is pressed on Device 1. *Device 1 prints a message to the terminal to signify this.*
* Device 1 sends an initial message. *Device 1 prints a message to the terminal to signify this.*
* Device 2 receives the message. *Device 2 prints a message to the terminal to signify this.*
* Device 2 sends a response message to Device 1. *Device 2 prints a message to the terminal to signify this.*
* Device 1 receives the response message from Device 2. *Device 1 prints a message to the terminal to signify this.*

**Scenario 2:**

* Button A is pressed on Device 2. *Device 2 prints a message to the terminal to signify this.*
* Device 2 sends an initial message. *Device 2 prints a message to the terminal to signify this.*
* Device 1 receives the message. *Device 1 prints a message to the terminal to signify this.*
* Device 1 sends a response message to Device 2. *Device 1 prints a message to the terminal to signify this.*
* Device 2 receives the response message from Device 1. *Device 2 prints a message to the terminal to signify this.*