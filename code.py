from adafruit_circuitplayground import cp
while True:
    cp.red_led = not cp.button_b
    if cp.button_b:
        print("button b")
    if cp.button_a:
        print("button a")