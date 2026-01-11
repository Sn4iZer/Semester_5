import numpy as np
import matplotlib.pyplot as plt

SR = 50

t = np.arange(0, 1.02, 1/SR)

s = 1 + np.cos(2*np.pi*5*t) + 0.3*np.cos(2*np.pi*9*t)

plt.plot(t, s)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal in time domain")
plt.grid()
plt.show()