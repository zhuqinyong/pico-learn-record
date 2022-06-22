import machine
import utime
import tm1637

tm = tm1637.TM1637(clk=machine.Pin(14), dio=machine.Pin(15))
led = machine.Pin(25, machine.Pin.OUT)
buzzer = machine.Pin(0, machine.Pin.OUT)

n = 10

while True:
    led.toggle()
    buzzer.toggle()
    utime.sleep(3)
    tm.number(n)
    n = n - 1
    if n < 0:
        n = 10
