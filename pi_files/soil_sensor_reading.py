import datetime as dt
import time
import board
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

now = dt.datetime.now()
touch = ss.moisture_read()
temp = ss.get_temp()
print(f"{now},{temp},{touch}")
