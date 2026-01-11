
## Question 1: Signal Creation and Time-Domain Visualization

### Description
In this question, we create a signal using NumPy and display it in the time domain using Matplotlib.  
The goal is to generate the signal, define its time axis, and visualize it clearly.

---

### Code Explanation

- **Import libraries**
  - `numpy` is used to create arrays and handle numerical values.
  - `matplotlib.pyplot` is used to draw the graph.

- **Define the sampling rate**
  - A variable `SR` is created to store the sampling rate.
  - This value controls how many samples are taken per second.

- **Create the time array**
  - A time vector `t` is generated from 0 to around 1 second.
  - The step size is based on the sampling rate (`1 / SR`).
  - This array represents the time axis of the signal.

- **Build the signal**
  - A signal `s` is created by combining multiple components into one array.
  - All operations are applied directly on the time array.
  - The result is a single signal stored in `s`.

- **Plot the signal**
  - The signal is plotted using time on the x-axis and amplitude on the y-axis.
  - Axis labels and a title are added for clarity.
  - A grid is enabled to make the plot easier to read.

- **Display the plot**
  - The graph is shown on the screen using `plt.show()`.

---

### Output
- A time-domain plot showing the signal over one second.
- The signal appears as a smooth waveform with visible variations.
- The plot is clearly labeled and easy to understand.
