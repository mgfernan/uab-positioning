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
2. Compute the ionospheric TEC (assuming code biases are almost 0)
3. What is the ionospheric delay for L1 and L2


### 4. Troposphere: zenith and slant delay

A GNSS receiver observes a satellite at an elevation angle of $30^\circ$. The zenith hydrostatic and wet tropospheric delays are

$$
T_{z,dry} = 2.30\ m,
\qquad
T_{z,wet} = 0.25\ m.
$$

Assume a simple mapping function

$$
m(e) = \frac{1}{\sin e}.
$$

1. Compute the total zenith tropospheric delay $T$.
2. Compute the slant tropospheric delay at an elevation of $30^\circ$.
3. Repeat the calculation for an elevation of $10^\circ$.
4. Explain why the tropospheric error becomes particularly important for low-elevation satellites.

### 5. Satellite orbit error

The position of a GNSS satellite is known with an error vector of:

$$
\Delta\mathbf{r}_{s,ECEF}=
\begin{bmatrix}
1.2\\
0.6\\
1.484
\end{bmatrix}\ m.
$$


Assume that the line-of-sight unit vector from the receiver to the satellite is

$$
\mathbf{u}_{ECEF}
=
\begin{bmatrix}
0.6\\
0.3\\
0.742
\end{bmatrix}.
$$

1. Calculate the contribution of the satellite error into the pseudorange measurement.


### 6. Common-mode errors and differential positioning

Two GNSS receivers, a base $B$ and a rover $R$, observe the same satellite $s$.

The pseudorange model is simplified to

$$
PR_i^s
=
\rho_i^s
+c\delta t_i
-c\delta t^s
+I_i^s
+T_i^s
+\epsilon_i^s,
$$

where $i\in\{B,R\}$.

Assume that the satellite clock error is $+2.0\ m$, the ionospheric delays are

$$
I_B^s=4.0\ m,
\qquad
I_R^s=4.3\ m,
$$

and the tropospheric delays are

$$
T_B^s=2.1\ m,
\qquad
T_R^s=2.2\ m.
$$

The receiver clock biases are

$$
c\delta t_B=1.0\ m,
\qquad
c\delta t_R=4.0\ m.
$$

1. Which error terms cancel when forming the single difference

$$
\Delta PR_{RB}^s=PR_R^s-PR_B^s?
$$

2. Compute the contribution of the clock and atmospheric terms to the single difference.
3. Explain why differential GNSS can mitigate some errors without explicitly estimating them.
4. Why are atmospheric errors not completely cancelled when the rover and base are separated?


### 7. Multipath versus clock error

A receiver observes four satellites. A simplified residual analysis gives:

| Satellite | Residual |
|---|---:|
| $G01$ | $+3.1\ m$ |
| $G08$ | $+2.9\ m$ |
| $G15$ | $+3.2\ m$ |
| $G22$ | $+0.4\ m$ |

Assume the residuals are computed after applying the broadcast satellite clock correction.

1. What observation error could explain a similar offset for three satellites?
2. Why does the $G22$ observation suggest that the problem may not be purely a receiver clock error?
3. Give two possible explanations for the different behaviour of $G22$.


### 8. Elevation-dependent weighting

A receiver assigns an observation standard deviation according to

$$
\sigma(e)=\frac{\sigma_0}{\sin e},
$$

where

$$
\sigma_0=0.5\ m.
$$

1. Calculate the standard deviation assigned to a satellite at $90^\circ$, $30^\circ$, and $10^\circ$.
2. Which observation receives the largest weight in a weighted least-squares solution?
3. Explain physically why low-elevation observations are often down-weighted.
4. Does down-weighting eliminate the atmospheric error?


### 9. Correlated errors and the covariance matrix

Two pseudorange measurements have standard deviations

$$
\sigma_1=1\ m,
\qquad
\sigma_2=1\ m,
$$

and correlation coefficient

$$
\rho=0.8.
$$

1. Write the covariance matrix of the two observations.
2. If the errors were independent, what would the covariance matrix look like?
3. Consider the average

$$
\bar e=\frac{e_1+e_2}{2}.
$$

Compute its standard deviation for the correlated case.
4. Compare it with the independent case.
5. Explain why assuming independent errors can lead to an overly optimistic estimate of positioning precision.



***

## Answers

### 1.

1.
$$
I = \frac{40.3}{f^2} \cdot VTEC = \frac{40.3}{(1575.42 \times 10^6)^2} \cdot 12.5 \times 10^{16} = 2.03\ m
$$
2.

$$
m(e) = \frac{1}{\sqrt{1 - \left(\frac{R_E}{R_E + h_m} \cdot \cos e\right)^2}} = \frac{1}{\sqrt{1 - \left(\frac{6370}{6370 + 400} \cdot \cos 20^\circ\right)^2}} \approx 2.14
$$

$$
STEC = m(e) \cdot VTEC = 2.14 \cdot 12.5\ TECU = 26.75\ TECU
$$

3. The ionospheric delay is inversely proportional to the square of the frequency. Therefore, the delay at $f_{L2}$ will be greater than at $f_{L1}$.

4. The ionospheric phase delay is the negative of the group delay, so it will be $-2.03\ m$ for the vertical signal and $-2.03 \cdot 2.14 = -4.34\ m$ for the signal at $20^\circ$ elevation.

### 2.

$$
m(e) = \frac{1}{\sqrt{1 - \left(\frac{R_E}{R_E + h_m} \cdot \cos e\right)^2}} = \frac{1}{\sqrt{1 - \left(\frac{6370}{6370 + 400} \cdot \cos 30^\circ\right)^2}} \approx 1.72
$$

$$
I_v = \frac{I}{m(e)} = \frac{14.7\ m}{1.72} \approx 8.52\ m
$$

$$
STEC = \frac{I_v \cdot f^2}{40.3} = \frac{8.52\ m \cdot (1575.42 \times 10^6)^2}{40.3} \approx 52.47\ TECU
$$

### 3.

1. The ionosphere-free pseudorange can be calculated using the formula:

$$
PR_{IF} = \frac{f_{L1}^2 \cdot PR_{L1} - f_{L2}^2 \cdot PR_{L2}}{f_{L1}^2 - f_{L2}^2}
$$

$$
PR_{IF} = \frac{(1575.42 \times 10^6)^2 \cdot 24\,130\,795.37 - (1227.6 \times 10^6)^2 \cdot 24\,130\,802.72}{(1575.42 \times 10^6)^2 - (1227.6 \times 10^6)^2} \approx 24\,130\,784.01\ m
$$

2. The $TEC$ can be calculated from the geometry free combination

$$
PR_{LI} \approx 40.3\cdot (\frac{1}{f_2^2}-\frac{1}{f_1^2}) \cdot TEC
$$

$$
TEC \approx \frac{24\,130\,802.72 - 24\,130\,795.37}{40.3\cdot (\frac{1}{(1227.6e6)^2}-\frac{1}{(1575.42e6)^2})} \approx 69.97\ TECU
$$

3. The ionospheric delay for L1 and L2 are then:

$$
I_1 = \frac{40.3}{(1575.42e6)^2} \cdot 69.97e16 \approx 11.36\ m \\
I_2 = \frac{40.3}{(1227.6e6)^2} \cdot 69.97e16 \approx 18.71\ m \\
$$


### 4.


1. The zenith total delay is

$$
T = T_{z,dry} + T_{z,wet} = 2.30 + 0.25 = 2.55\ m.
$$

2. At $e=30^\circ$,

$$
m(30^\circ) = \frac{1}{\sin 30^\circ}=2.
$$

Therefore,

$$
T(30^\circ) = m(e) \cdot T
=2(2.55)=5.10\ m.
$$

3. At $e=10^\circ$,

$$
m(10^\circ)=\frac{1}{\sin 10^\circ}\approx5.76,
$$

and therefore

$$
T(10^\circ)\approx5.76(2.55)
\approx14.7\ m.
$$

4. The atmospheric path becomes much longer at low elevation angles. Consequently, both the tropospheric delay and the sensitivity to modelling errors increase.


### 5.

Only the component of the satellite position error along the receiver–satellite line of sight directly affects the measured range.

For a small satellite position error, approximate the resulting range error as

$$
\Delta\rho
\approx
\mathbf{u}^{T} \cdot \Delta\mathbf{r}_s.
$$

Therefore

$$
\Delta\rho
\approx
0.6(1.2)+0.3(0.6)+0.742(1.484) \approx2.00\ m
$$


### 6.

1. The satellite clock error cancels because the same satellite is observed by both receivers:

$$
(-c\delta t^s)-(-c\delta t^s)=0.
$$


2. The receiver clock terms do not cancel and its contribution is

$$
c\delta t_R-c\delta t_B=4.0-1.0=3.0\ m.
$$

The ionospheric contribution is

$$
I_R^s-I_B^s=4.3-4.0=0.3\ m,
$$

and the tropospheric contribution is

$$
T_R^s-T_B^s=2.2-2.1=0.1\ m.
$$

Thus the combined clock and atmospheric contribution is

$$
3.0+0.3+0.1=3.4\ m.
$$

3. Differential positioning exploits the spatial and temporal correlation of errors. Common errors appear similarly in both observations and are therefore removed or strongly reduced by differencing.

4. Atmospheric delays depend on the signal propagation path. Two receivers separated by a certain baseline do not experience exactly the same ionospheric and tropospheric conditions, so only the common component is cancelled.


### 7.

1. A common receiver-related error, such as a receiver clock bias, could produce a similar offset in several observations. The receiver clock bias affects all simultaneously observed satellites approximately equally:

$$
\Delta PR^s\approx c\delta t_r.
$$

Therefore, a common offset of about $3\ m$ is consistent with a receiver clock error.

1. If the error were purely a receiver clock bias, all four observations should show approximately the same offset. The $G22$ residual is substantially different.

2. Possible explanations include:

- satellite-specific ephemeris or clock residual error;
- multipath affecting the $G22$ signal path;
- larger measurement noise;
- an incorrect or corrupted observation.

The key point is that common-mode and satellite-specific errors have different signatures.

### 8.

1.

For $e=90^\circ$

$$
\sigma(90^\circ)=0.5\ m.
$$

For $e=30^\circ$

$$
\sigma(30^\circ)
=
\frac{0.5}{\sin30^\circ}
=
1.0\ m.
$$

For $e=10^\circ$

$$
\sigma(10^\circ)
=
\frac{0.5}{\sin10^\circ}
\approx2.88\ m.
$$

1. The $90^\circ$ observation receives the largest weight ($w= 1/\sigma^2$) because it has the smallest assigned variance.

2. Low-elevation signals travel through a longer atmospheric path and are generally more affected by multipath and modelling errors.

3. No. Weighting only changes the influence of the observation in the navigation solution. It does not correct the underlying measurement error.



### 9.

1. The covariance is

$$
\operatorname{cov}(e_1,e_2)
=
\rho\sigma_1\sigma_2
=
0.8.
$$

Therefore,

$$
\mathbf R=
\begin{bmatrix}
1 & 0.8\\
0.8 & 1
\end{bmatrix}
m^2.
$$

2. For independent observations,

$$
\mathbf R=
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}
m^2.
$$

3. The variance of the average is

$$
\sigma_{\bar e}^2
=
\frac{1}{4}
\left(
\sigma_1^2+\sigma_2^2
+2\rho\sigma_1\sigma_2
\right).
$$

Thus,

$$
\sigma_{\bar e}^2
=
\frac{1}{4}(1+1+1.6)
=
0.9,
$$

so

$$
\sigma_{\bar e}\approx0.95\ m.
$$

4. For independent observations,

$$
\sigma_{\bar e}
=
\frac{1}{\sqrt2}
\approx0.71\ m.
$$

The correlated observations provide much less noise reduction.

5. If correlations are ignored, the covariance model assumes that observations contain more independent information than they actually do. The resulting formal precision can therefore be too optimistic.
