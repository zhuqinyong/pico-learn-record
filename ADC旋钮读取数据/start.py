import machine
import utime

potentiometer = machine.ADC(26)
while True:
    utime.sleep(0.5)
    print(potentiometer.read_u16())
