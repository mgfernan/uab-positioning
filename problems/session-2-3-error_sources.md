# Exercises: error sources

## Problems

### 1. Ionosphere: mapping function

At a given moment, the ionosphere has a vertical electron content of

$$
VTEC = 12.5\ TECU
$$

Note that:

$$
1\ \mathrm{TECU}=10^{16}\ \mathrm{el/m^2}.
$$

1.  What is the ionospheric group delay (code delay) for a carrier at $f_{L1} = 1575.42\ MHz$, for a signal arriving vertically at a receiver located on the Earth's surface?

2. Write the expression of the ionospheric mapping function. If $R_E = 6370 km$ is the Earth's radius and $h_m = 400 km$ is the ionosphere's altitude, calculate, for a signal arriving at an elevation angle of $20^\circ$: (a) the obliquity factor and (b) the slant ionospheric group delay.
3. If the carrier is $f_{L2} = 1227.6\ MHz$, will the ionospheric delay be greater or smaller? Why?
4. What is the ionospheric phase delay under the same conditions as in parts
(1) and (2)?

### 2. Ionosphere: slant to vertical

A scientist has measured the ionospheric delay at an elevation of 30° above the horizon $I = 14.7 m$ at the carrier frequency $f_{L1} = 1575.42\ MHz$. Based on this measurement, estimate the total electron content in the vertical direction. Assume that the ionosphere can be modelled as a thin layer at an altitude of 400 km.


### 3. Ionosphere: observable combinations

A dual-frequency GPS receiver measures the pseudoranges at $f_{L1} = 1575.42 MHz$ and $f_L2 = 1227.6 MHz$ to a GPS satellite as follows:
$$
PR_{L1} = 24\,130\,795.37\ m \\
PR_{L2} = 24\,130\,802.72\ m
$$

1. Compute the ionosphere-free pseudorange.
2. What is the ionospheric delay for L1 and L2 (assuming code biases are almost 0)?
3. What TEC corresponds to the previous ionospheric delay?


***

## Answers

### 1.

1.
$$
I = \frac{40.3}{f^2} \cdot VTEC = \frac{40.3}{(1575.42 \times 10^6)^2} \cdot 12.5 \times 10^{16} = 0.203\ m
$$
2.

$$
m(e) = \frac{1}{\sqrt{1 - \left(\frac{R_E}{R_E + h_m} \cdot \cos e\right)^2}} = \frac{1}{\sqrt{1 - \left(\frac{6370}{6370 + 400} \cdot \cos 20^\circ\right)^2}} \approx 2.14
$$

$$
STEC = m(e) \cdot VTEC = 2.14 \cdot 12.5\ TECU = 26.75\ TECU
$$

3. The ionospheric delay is inversely proportional to the square of the frequency. Therefore, the delay at $f_{L2}$ will be greater than at $f_{L1}$.

4. The ionospheric phase delay is the negative of the group delay, so it will be -0.203 m for the vertical signal and -0.203 * 2.14 = -0.434 m for the signal at 20° elevation.

### 2.

$$
m(e) = \frac{1}{\sqrt{1 - \left(\frac{R_E}{R_E + h_m} \cdot \cos e\right)^2}} = \frac{1}{\sqrt{1 - \left(\frac{6370}{6370 + 400} \cdot \cos 30^\circ\right)^2}} \approx 1.72
$$

$$
I_v = \frac{I}{m(e)} = \frac{14.7\ m}{1.72} \approx 8.52\ m
$$

$$
STEC = \frac{I_v \cdot f^2}{40.3} = \frac{8.52\ m \cdot (1575.42 \times 10^6)^2}{40.3} \approx 52.48\ TECU
$$

### 3.

1. The ionosphere-free pseudorange can be calculated using the formula:

$$
PR_{IF} = \frac{f_{L1}^2 \cdot PR_{L1} - f_{L2}^2 \cdot PR_{L2}}{f_{L1}^2 - f_{L2}^2}
$$

$$
PR_{IF} = \frac{(1575.42 \times 10^6)^2 \cdot 24\,130\,795.37 - (1227.6 \times 10^6)^2 \cdot 24\,130\,802.72}{(1575.42 \times 10^6)^2 - (1227.6 \times 10^6)^2} \approx 24\,130\,784.01\ m
$$

2. The ionospheric delay for L1 and L2 can be calculated with the geometry combination (assuming code biases are negligible):

$$
I \approx PR_{LI} = 24\,130\,802.72 - 24\,130\,795.37 \approx 7.35\ m
$$

3. The TEC corresponding to the ionospheric delay can be calculated using the formula:

$$
TEC = \frac{I \cdot f^2}{40.3} = \frac{7.35\ m \cdot (1575.42 \times 10^6)^2}{40.3} \approx 45.26\ TECU
$$
