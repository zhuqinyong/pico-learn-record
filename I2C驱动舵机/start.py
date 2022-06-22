from machine import Pin, PWM
import utime

servo = PWM(Pin(25))
n = 0
while True:
    servo.duty_u16(abs(32000 - n * 1000))
    n = n + 1
    n = n % 64
    print(n)
    utime.sleep(0.2)
