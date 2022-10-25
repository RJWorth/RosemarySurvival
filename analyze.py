import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
sb.set_style("whitegrid")

df = pd.read_csv("data/soil_sensor_readings.csv")
df["time"] = pd.to_datetime(df["time"])
df = df.set_index("time")
df.index = df.index.tz_localize('UTC').tz_convert("US/Central")

### Time at which stabilization began
t1 = pd.Timestamp("2022-10-08 23:00:00.0", tz="US/Central")
### For original section, smooth more aggressively
### After measurement stabilization added, use smaller window to reduce lag
N1 = 20
N2 = 10
df[f"moisture_smoothed_{N1}"] = df["moisture"].rolling(N1).median()
df[f"moisture_smoothed_{N2}"] = df["moisture"].rolling(N2).median()
df["moisture_smoothed"] = df[f"moisture_smoothed_{N1}"]
df.loc[df.index > t1, "moisture_smoothed"] = df.loc[df.index > t1, f"moisture_smoothed_{N2}"]

### Remove the initial noisey section
df.loc[df.index <= t1, "moisture"] = np.nan

df["temp"] = df["temp"]*9/5 + 32

df = df.reset_index()

f1, ax1 = plt.subplots(2, sharex=True, figsize=[12, 6])

ax1[0].plot(df["time"], df["temp"], lw=1, color="red", label="Temperature")
ax1[0].set_ylabel("Temperature (F?)")

ax1[1].scatter(df["time"], df["moisture"], s=5, color="blue", alpha=0.5, label="Moisture")
ax1[1].plot(df["time"], df["moisture_smoothed"], lw=2, color="blue", label="Moisture (smoothed)")
ax1[1].set_ylabel("Moisture")

for label in ax1[-1].get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

ax1[0].set_title("Wifi-Rosemary Status Report")

plt.tight_layout()
f1.savefig("plots/sensor_readings.png")
plt.close(f1)
