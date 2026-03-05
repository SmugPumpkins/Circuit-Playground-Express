import subprocess

def list_usb_ports():
    print("USB Connections:")

    # Query Windows for USB serial devices
    result = subprocess.run(
        ["wmic", "path", "Win32_PnPEntity", "where", "PNPClass='Ports'", "get", "Name"],
        capture_output=True,
        text=True,
    )

    for line in result.stdout.splitlines():
        # Only include devices that expose a COM port and are USB
        if "(COM" in line and "USB" in line:
            port = line.split("(COM")[-1].replace(")", "").strip()
            print(f"COM{port}")


if __name__ == "__main__":
    list_usb_ports()