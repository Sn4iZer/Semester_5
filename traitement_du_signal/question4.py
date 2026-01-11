import numpy as np
import matplotlib.pyplot as plt

SR = 50

t = np.arange(0, 1.02, 1/SR)

s = 1 + np.cos(2*np.pi*5*t) + 0.3*np.cos(2*np.pi*9*t)

S = np.fft.fft(s)
freqs = np.fft.fftfreq(len(s), 1/SR)

cutoff = 6  # Hz
S_filtered = S.copy()
S_filtered[np.abs(freqs) > cutoff] = 0

s_filtered = np.fft.ifft(S_filtered).real

plt.plot(t, s, label='Original signal')
plt.plot(t, s_filtered, label='Filtered signal', linestyle='--')
plt.legend()
plt.title("Low-pass filtering effect")
plt.show()
