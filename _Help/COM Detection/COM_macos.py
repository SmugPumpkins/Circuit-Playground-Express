# Lists USB serial ports on macOS
# No external packages required

import os


def list_usb_ports():
    print("USB Connections:")

    for device in os.listdir("/dev"):
        # USB serial devices typically match these patterns
        if device.startswith("tty.usb") or device.startswith("cu.usb"):
            print(f"/dev/{device}")


if __name__ == "__main__":
    list_usb_ports()