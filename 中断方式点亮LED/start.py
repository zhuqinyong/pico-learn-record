import machine
from machine import Timer, Pin
import utime
led = Pin(0, Pin.OUT)
btn = Pin(28, Pin.IN, Pin.PULL_DOWN)


def btn_irq_handler(pin):
    btn.irq(handler=None)
    print(pin)


led.value(1)
utime.sleep(1)
led.value(0)
btn.irq(trigger=machine.Pin.IRQ_RISING,handler=btn_irq_handler)
