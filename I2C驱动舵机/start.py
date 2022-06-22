import machine

machine.I2C(machine.Pin(28))
port = machine.I2C.scan()
