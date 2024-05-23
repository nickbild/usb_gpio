import time
from usbgpio import USBgpio

gpio = USBgpio('/dev/ttyACM0', 115200)

gpio.set_output(2)
gpio.set_input(3)

while True:
    gpio.digital_write(2, "HIGH")
    time.sleep(1)
    gpio.digital_write(2, "LOW")
    time.sleep(1)

    print(gpio.digital_read(3))
