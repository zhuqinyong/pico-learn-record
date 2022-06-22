from machine import Pin
import utime
led = Pin(25, Pin.OUT)
led.value(1)
while True:
    print(led.value())
    utime.sleep(1)
    led.value(0)
    utime.sleep(0)
    led.value(1)