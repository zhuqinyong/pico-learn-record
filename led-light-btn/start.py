from machine import Pin
import utime

out = Pin(0, Pin.OUT)
btn = Pin(28, Pin.IN)
while True:
    utime.sleep(0.5)
    print(btn.value())
    print(out.value())
    if btn.value() == 1:
        out.value(1)
    else:
        out.value(0)
