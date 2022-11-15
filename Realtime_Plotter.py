import numpy as np
import time
import matplotlib.pyplot as plt
import psutil
import matplotlib.pyplot as plt
import sys
import datetime
from datetime import timedelta


x = []#np.linspace(0, 100, 100)
y = []#np.linspace(0, 100, 100)
y2 = []
plt.ion()
figure, ax = plt.subplots(figsize=(6, 4))
ax.ticklabel_format(useOffset=False)
line1, = ax.plot(x, y, color='b')
line2, = ax.plot(x, y2, color='g')

plt.title("Dynamic Plot of Graph", fontsize=25)
plt.grid(visible=True, which='both', color='y', ls='--', animated=False)

plt.xlabel("X", fontsize=18)
plt.ylabel("Graph", fontsize=18)
plt.xticks(rotation=5)

p = 0

# Plots data with 1001 points in cache at any given point in time.
# x shows max 30 seconds of data 
# TODO: need to make these configurable

while True:
    if (len(x) > 1000) and True:
        x.pop(0)
        y.pop(0)
        y2.pop(0)


    p += 1
    #for p in range(200):
    #ax.set_xlim(left=0, right=p + 5)

    t = datetime.datetime.now()
    print (t)
    x.append(t)
    cpu_usage = psutil.cpu_percent()
    y.append(cpu_usage)
    y2.append(cpu_usage + 5)

    #ax.set_xlim([datetime.date(2022,7,28,11,14), datetime.date(2022,7,28,11,18)])
    #ax.set_xlim(datetime.datetime(2022, 7, 28, 11, 27), datetime.datetime(2022, 7, 28, 11, 28))
    #ax.set_xlim(left=max(0, p - 50), right=p + 5)
    #ax.set_xlim(t-timedelta(seconds=10), t+timedelta(seconds=10))
    #ax.set_xlim(t - timedelta(seconds=10), t + timedelta(seconds=1))

    ax.set_xlim(t - timedelta(seconds=30), t + timedelta(seconds=1))
    #ax.set_xlim(max(t,t - timedelta(seconds=5)), t + timedelta(seconds=1))
    ax.set_ylim(0, top=max(max(y), max(y2)))

    #updated_y = np.cos(x - 0.05 * p)

    line1.set_xdata(x)
    line1.set_ydata(y)

    line2.set_xdata(x)
    line2.set_ydata(y2)

    figure.canvas.draw()

    figure.canvas.flush_events()
    time.sleep(0)