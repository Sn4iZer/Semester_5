
## Question 1: Signal Creation and Time-Domain Visualization

### Code Explanation


- **Import libraries**
```bash
import numpy as np
import matplotlib.pyplot as plt
```
  - `numpy` is used to create arrays and handle numerical values.
  - `matplotlib.pyplot` is used to draw the graph.

- **Define the sampling rate**
```bash
SR = 50
```
  - A variable `SR` is created to store the sampling rate.
  - This value controls how many samples are taken per second.

- **Create the time array**
```bash
t = np.arange(0, 1.02, 1/SR)
```
  - A time vector `t` is generated from 0 to around 1 second.
  - The step size is based on the sampling rate (`1 / SR`).
  - This array represents the time axis of the signal.

- **Build the signal**
```bash
s = 1 + np.cos(2*np.pi*5*t) + 0.3*np.cos(2*np.pi*9*t)
```
  - A signal `s` is created by combining multiple components into one array.
  - All operations are applied directly on the time array.
  - The result is a single signal stored in `s`.

- **Plot the signal**
```bash
plt.plot(t, s)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal in time domain")
plt.grid()
```
  - The signal is plotted using time on the x-axis and amplitude on the y-axis.
  - Axis labels and a title are added for clarity.
  - A grid is enabled to make the plot easier to read.

- **Display the plot**
```bash
plt.show()
```
  - The graph is shown on the screen using `plt.show()`.

---

### Output
- A time-domain plot showing the signal over one second.
- The signal appears as a smooth waveform with visible variations.
- The plot is clearly labeled and easy to understand.


## Question 2: 1D Fourier Transform and Frequency Visualization

### Code Explanation

- **Import libraries and function**
  
```bash
from ressources1 import fourier1D
```

- fourier1D is imported from an external file and used to compute and display the Fourier transform.

```bash
s = 1 + np.cos(2*np.pi*5*t) + 0.3*np.cos(2*np.pi*9*t)
```
- The signal is built and stored in the variable s.

- This is the same signal used in Question 1.

- **Apply the Fourier transform**

```bash
fourier1D(s, SR)
```

- The signal and the sampling rate are passed to the fourier1D function.

- The function computes the Fourier transform internally.

- The frequency spectrum is automatically displayed.

**Inside the fourier1D Function**
 - **Get signal size**

```bash
N = len(s)
```

- The number of samples in the signal is stored.

- **Compute the Fourier transform**

```bash
a = np.abs(np.fft.fftshift(np.fft.fft(s))) / N
```
- The Fourier transform is computed.

- The result is centered and converted to amplitudes.

- The output is normalized using the signal length.

- **Create the frequency axis**

```bash
x = fe * (np.arange(-np.floor(n), np.ceil(n))) / N
```
- A frequency axis is generated.

- This axis matches the transformed signal.

- **Display the spectrum**

```bash
plt.bar(x, a)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectre de Fourier')
plt.grid(True)
plt.show()
```

- The frequency spectrum is displayed using a bar plot.

- Labels, title, and grid are added for clarity.

### Output :

- A frequency-domain plot is displayed.

- The plot shows the main frequency components of the signal.

- Peaks appear at specific frequencies, representing the signal content.


## Question 3: Zero-Padding and Fourier Transform Resolution

### Code Explanation

- **Create a zero-padded signal**
```bash
s_pad = np.concatenate((s, np.zeros(5 * len(s))))
```

- A new signal s_pad is created from the original signal s.

- Zeros are added at the end of the signal.

- The number of zeros added is five times the original signal length.

- This increases the total number of samples without changing the original data.

- **Apply the Fourier transform to the padded signal**

```bash
fourier1D(s_pad, SR)
```

- The zero-padded signal is passed to the same Fourier function.

- The function processes the longer signal and displays its spectrum.

- No change is made to the sampling rate.

### Output

- A new frequency-domain plot is displayed.

- The spectrum appears smoother and more detailed.

- No new frequency components are created.

- The frequency resolution is visually improved due to the increased signal length.


## Question 4: Low-Pass Filtering and Signal Reconstruction

### Code Explanation

- **Compute the Fourier transform**
```bash
S = np.fft.fft(s)
freqs = np.fft.fftfreq(len(s), 1/SR)
```
- The Fourier transform of the original signal s is stored in S.

- freqs is the array of corresponding frequencies.

- **Apply a low-pass filter**

```bash
cutoff = 6  # Hz
S_filtered = S.copy()
S_filtered[np.abs(freqs) > cutoff] = 0
```

- A copy of the spectrum S_filtered is created.

- Frequencies higher than the cutoff value (6 Hz) are set to zero.

- This keeps only the low-frequency components.

- **Reconstruct the filtered signal**

```bash
s_filtered = np.fft.ifft(S_filtered).real
```

- The inverse Fourier transform is applied to S_filtered.

- The result is the time-domain filtered signal.

- .real is used to remove any small imaginary parts caused by computation.

- **Plot original and filtered signals**

```bash
plt.plot(t, s, label='Original signal')
plt.plot(t, s_filtered, label='Filtered signal', linestyle='--')
plt.legend()
plt.title("Low-pass filtering effect")
plt.show()
```
- Both signals are plotted together for comparison.

- The original signal is solid, the filtered signal is dashed.

- A legend and title are added for clarity.

### Output

- The plot shows the original and filtered signals.

- High-frequency components are removed in the filtered signal.

- The filtered signal is smoother and slower, keeping only the low frequencies.
