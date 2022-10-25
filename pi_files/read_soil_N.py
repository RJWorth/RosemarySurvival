import datetime as dt
import numpy as np
import time
import board
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

N = 20

now = dt.datetime.now()
touch = []
temp = []
for i in range(N):
	touch.append(ss.moisture_read())
	temp.append(ss.get_temp())

md_touch = np.median(touch)
md_temp = np.median(temp)
print(f"{now},{md_temp},{md_touch}")

