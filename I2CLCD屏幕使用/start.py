import machine

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
port = i2c.scan()
i2c.writeto(port[0], '\x7C')
i2c.writeto(port[0], '\x2D')
i2c.writeto(port[0], "hello world")
