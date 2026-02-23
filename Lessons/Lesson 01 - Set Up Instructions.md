# Circuit Playground Express + CircuitPython + PyCharm Setup (Windows)

Follow **every step in order**. Do not skip steps. If something does not work, stop and fix it before moving on.

---

## Part 1: Board Setup (Installing CircuitPython)

### Step 1: Download the CircuitPython Firmware

1. Go to:
   [https://circuitpython.org/board/circuitplayground_express/](https://circuitpython.org/board/circuitplayground_express/)
2. Click **Download .UF2 Now**
3. Leave the file in your **Downloads** folder

---

### Step 2: Put the Board Into Bootloader Mode

1. Plug the **Circuit Playground Express** into your computer using a USB cable
2. Press the **RESET** button on the board **two times quickly**
3. A new removable drive will appear named **CPLAYBOOT**

If the drive does not appear:

* Try a different USB cable
* Try a different USB port
* Press reset twice again

---

### Step 3: Install CircuitPython on the Board

1. Open the **CPLAYBOOT** drive
2. Drag the downloaded **UF2** file into the drive
3. Wait for the board to restart automatically

When successful:

* The **CPLAYBOOT** drive disappears
* A new drive appears named **CIRCUITPY**

This means CircuitPython is installed correctly.

---

## Part 2: Install msys2 and tio (Required for Serial Output)

### Step 1: Download and Install msys2

1. Go to:
   [https://www.msys2.org/](https://www.msys2.org/)
2. Download the installer
3. Run the installer
4. **DO NOT CHANGE THE INSTALL LOCATION**
   Leave it as the default (usually `C:\msys64`)
5. Finish the installation

---

### Step 2: Install tio

1. Open **MSYS2** (use the default MSYS2 terminal)
2. Paste the following command and press **Enter**:

```
pacman -S tio
```

3. When asked if you want to proceed, type:

```
y
```

and press **Enter**

---

### Step 3: Verify tio Installation (in MSYS2)

In the MSYS2 terminal, type:

```
tio --version
```

A version number means tio installed correctly.

---

## Part 3: Add msys2 to the PATH

### Step 1: Open Environment Variables

1. Click the **Start Menu**
2. Type:
   **Edit environment variables for your account**
3. Press **Enter**

---

### Step 2: Add msys2 to the User PATH

1. In the window that opens:

   * Look under **User variables** (not System variables)
   * Select **Path**
   * Click **Edit…**
2. Click **New**
3. Paste:

```
C:\msys64\usr\bin
```

4. Click **OK**
5. Click **OK** again to close all windows

If you did **not** install msys2 in the default location, click **Browse** instead and locate the correct `usr\bin` folder.

---

### Step 3: Verify tio Works in Command Prompt

1. Open **Command Prompt**
2. Type:

```
tio --version
```

If a version number appears, PATH is set correctly.

---

## Part 4: PyCharm Configuration

### Step 1: Open PyCharm Settings

1. Open **PyCharm**
2. Go to:
   **File → Settings**

---

### Step 2: Turn Off Auto-Save

1. Navigate to:
   **Appearance & Behavior → System Settings → Autosave**
2. Turn **OFF**:

   * “Save files if the IDE is idle for … seconds”
   * “Save files when switching to a different application or a built-in terminal”

---

### Step 3: Turn On Unsaved File Indicator

1. Go to:
   **Editor → General → Editor Tabs → Appearance**
2. Turn **ON**:

   * “Mark modified”

---

### Step 4: Set the Project Root to the Board

1. Make sure the **Circuit Playground Express is plugged in**
2. Make sure the **CIRCUITPY** drive is visible
3. In PyCharm:

   * **Settings → Project Structure**
   * Click **+ Add Content Root**
   * Select the **CIRCUITPY** drive
4. Apply and save

Your Python files will now save **directly to the board**.

---

### Step 5: Install CircuitPython Stubs and Other Required Libraries

1. In PyCharm:

   * **Settings → Project → Python Interpreter**
2. Click **Install**
3. Search for:

```
circuitpython-stubs
```

4. Install it
5. Do the same for the following libraries:
```
adafruit-circuitpython-circuitplayground
```
```
adafruit-circuitpython-hid
```
```
adafruit-circuitpython-lis3dh
```
```
adafruit-circuitpython-thermistor
```
```
adafruit-circuitpython-neopixel
```
This enables code completion and error checking.

---

## Part 5: Connect the Board to the PyCharm Terminal

### Step 1: Find the COM Port

Run this command in **PyCharm’s Terminal** or **Command Prompt**:

```
Get-CimInstance Win32_PnPEntity -Filter "ClassGuid = '{4d36e978-e325-11ce-bfc1-08002be10318}'" | Select-Object Name
```

Look for an entry that mentions a **USB** connection and note the **COM number**
(example: `COM20`)

---

### Step 2: Connect Using tio

In the **PyCharm Terminal**, type:

```
tio COM20
```

Replace `COM20` with **your** actual COM port.

If successful:

* The terminal connects to the board
* `print()` output from `code.py` appears here

---

## Part 6: Check To Make Sure Everything Works
Copy and paste the following code into the `code.py` file in your PyCharm project.
```python
from adafruit_circuitplayground import cp
while True:
    cp.red_led = not cp.button_b
    if cp.button_b:
        print("button b")
    if cp.button_a:
        print("button a")
```

This code will do the following:
* A red LED will turn on. If you press the B button it should turn off.
* When the B button is pressed, the terminal prints "button b"
* When the A button is pressed, the terminal prints "button a"

Save the file.

Try pressing the A and B buttons to see if everything is properly configured.

One last program to upload to ensure everything works is this program that allows you to get all of the pins and sensors that are built into the Circuit Playground Express. When you paste and save this code, it should output a list of pins that the board has access to:
```python
import microcontroller
import board 
try:
    import cyw43  # raspberrypi
except ImportError:
    cyw43 = None

board_pins = []
for pin in dir(microcontroller.pin):
    if (isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin) or
        (cyw43 and isinstance(getattr(microcontroller.pin, pin), cyw43.CywPin))):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append(f"board.{alias}")
        # Add the original GPIO name, in parentheses.
        if pins:
            # Only include pins that are in board.
            pins.append(f"({str(pin)})")
            board_pins.append(" ".join(pins))

for pins in sorted(board_pins):
    print(pins)
```