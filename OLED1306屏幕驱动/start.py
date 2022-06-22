# 1 # Display Image & text on I2C driven ssd1306 OLED display
#  2 from machine import Pin, I2C
#  3 from ssd1306 import SSD1306_I2C
#  4 import framebuf
#  5
#  6 WIDTH = 128 # oled display width
#  7 HEIGHT = 32 # oled display height
#
# i2c = I2C(0) # Init I2C using I2C0 defaults,
#   SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
# print("I2C Address : "+hex(i2c.scan()[0]).upper()) # Display device address
# print("I2C Configuration: "+str(i2c))