import machine
import utime

led = machine.Pin(0, machine.Pin.OUT)
btn = machine.Pin(28, machine.Pin.IRQ_RISING)


def btn_irq_handler(pin):
    btn.irq(handler=None)
    print(pin)


while True:
    print(btn.value())
    led.value(1)
    utime.sleep(1)
    led.value(0)
    btn.irq(trigger=machine.Pin.IRQ_RISING, handler=btn_irq_handler)
