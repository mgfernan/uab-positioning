# Exercises: Observables


## Problems


### 1. Carrier phase: why is it so precise?

Consider a GPS L1 signal:

$$
f_{L1}=1575.42\ \mathrm{MHz}
$$

The tracking loop of a receiver measures a (raw) carrier-phase observable of

$$
\phi = 432\,123.4\ \text{cycles}
$$

But once the positioning engine processes all measurements, estimates the integer ambiguity to

$$
N=105\,000\,000.
$$

For this simplified exercise, neglect atmospheric effects, satellite/receiver clocks and hardware biases.

Answer the following questions:

1. Compute the wavelength of the signal?
2. What is the value in meters for the carrier phase measurement and the integer ambiguity?
3. What is the value in meters for the full carrier-phase distance?
4. Suppose the receiver can measure the carrier phase to $1/100$ of a cycle. What is this equivalent to in metres?
5. Compare this with a pseudorange measurement whose noise is approximately $1\ \mathrm{m}$. Why is carrier phase potentially much more precise?


### Problem 2 — Three observables: different *views* of the same geometry

A receiver observes the same satellite at two consecutive epochs.

| Observable | Epoch $t$ | Epoch $t+1$ |
|---|---:|---:|
| Pseudorange | $25\,071\,907.453$ m | $25\,071\,989.461$ m |
| Carrier phase | $131\,753\,761.87$ cycles | $131\,754\,192.86$ cycles |
| Doppler  | $-430.948$ Hz| $-431.823$ Hz |

The interval between epochs is

$$
\Delta t=1\ \mathrm{s}
$$

and use

$$
\lambda_{L1}=0.1903\ \mathrm{m}.
$$

Answer the following questions:

1. Is the satellite approaching?
2. Is the satellite going towards the horizon or towards the zenith?
3. Using the pseudorange, estimate the change in range between the two epochs.
4. Using the carrier phase, estimate the change in carrier-phase distance.
5. Estimate the range rate ($\dot \rho$) from the pseudorange.
6. Estimate the range rate ($\dot \rho$) from the carrier phase.
7. Use the Doppler measurement to estimate the range rate.


### Problem 3 — Detecting cycle slip(s)

A receiver is tracking a GPS L1 satellite. Between two consecutive epochs,

$$
\Delta t=1\ \mathrm{s}.
$$

The observations are the same than the previous example, except for the carrier phase,
which measures the following:


| Observable | Epoch $t$ | Epoch $t+1$ |
|---|---:|---:|
| Carrier phase | $131\,753\,761.87$ cycles | $131\,754\,197.86$ cycles |

Use

$$
\lambda_{L1}=0.1903\ \mathrm{m}.
$$

Answer the following questions:

1. What change in distance is suggested by the carrier phase now?
2. Is the new distance consistent with the range rate from previous exercise?
3. Approximately how many carrier cycles would correspond to the pseudorange change?
4. Use the Doppler to identify and compute the number of carrier cycles.


***

## Answers

### Problem 1

1. Wavelength

$$
\lambda_{L1}= \frac{c}{f_{L1}}
		   = \frac{299\,792\,458\ \mathrm{m/s}}{1.57542\times10^9\ \mathrm{Hz}}
		   \approx 0.1903\ \mathrm{m}.
$$

2. Carrier-phase distance

The fractional phase is

$$
\begin{aligned}
\phi_{fractional} &=& 432\,123.4\ \text{cycles} \\
&=& 0.1903\ \text{m/cycle} \times 432\,123.4\ \text{cycles} \\
&\approx& 82\,233.08\ \mathrm{m} \\
\end{aligned}
$$

The integer ambiguity part:

$$
\begin{aligned}
\phi_{ambiguity} &=& 105\,000\,000\ \text{cycles} \\
&=& 0.1903\ \text{m/cycle} \times 105\,000\,000\ \text{cycles} \\
&\approx& 19\,981\,500\ \mathrm{m} \\
\end{aligned}
$$

3. Full Carrier-phase distance

The full phase, including the integer ambiguity, is

$$
\begin{aligned}
\Phi &= N+\phi \\
			&= 105\,000\,000+432\,123.4 \\
			&= 105\,432\,123.4\ \text{cycles}.
\end{aligned}
$$

The full carrier-phase distance is therefore

$$
\begin{aligned}
L &= \lambda\Phi \\
	&= 0.1903\times105\,432\,123.4 \\
	&\approx 20\,063\,733.08\ \mathrm{m}.
\end{aligned}
$$

4. $1/100$ cycle

One cycle corresponds to

$$
\lambda=0.1903\ \mathrm{m}.
$$

Therefore,

$$
\frac{\lambda}{100}
=
\frac{0.1903}{100}
$$

$$
\boxed{1.903\ \mathrm{mm}}.
$$

5. Why is carrier phase more precise?

A pseudorange measurement may have errors at the metre level, while carrier phase can be measured to a small fraction of a wavelength.

For L1:

$$
\lambda\approx19\ \mathrm{cm}.
$$

A measurement precision of $1/100$ cycle corresponds to only about

$$
\boxed{1.9\ \mathrm{mm}}.
$$

The carrier phase is therefore potentially **orders of magnitude more precise**, although it contains the unknown integer ambiguity.


### Problem 2

1. Range is increasing $\Rightarrow$ satellite going away. This is also confirmed by the carrier phase (number of cycles increasing) and a negative Doppler shift value
2. Satellite moving away $\Rightarrow$ to horizon
3. The rate change in meters is:

$$
\Delta\rho
=
25\,071\,989.461-25\,071\,907.453
$$

$$
\boxed{\Delta\rho=82.008\ \mathrm{m}}.
$$

4. The change in cycles is

$$
\Delta\phi
=
131\,754\,192.861
-
131\,753\,761.870
$$

$$
=430.991\ \mathrm{cycles}.
$$

In metres:

$$
\Delta L
=
430.991\times0.1903
$$

$$
\boxed{\Delta L\approx82.017\ \mathrm{m}}.
$$

The two measurements therefore give almost the same range change.

5. Since $\Delta t=1$ s,

$$
\dot\rho
\approx
\frac{\Delta\rho}{\Delta t}
$$

so

$$
\boxed{\dot\rho\approx82.008\ \mathrm{m/s}}.
$$

6. Range rate from carrier phase

$$
\dot\rho
\approx
\frac{82.017}{1}
$$

giving

$$
\boxed{\dot\rho\approx82.017\ \mathrm{m/s}}.
$$

7. Range rate from Doppler

Using

$$
v_{LOS}
=
-\frac{c f_D}{f_0}
$$

for $f_D=-430.948$ Hz:

$$
v_{LOS}
\approx
-\frac{3\times10^8(-430.948)}
{1.57542\times10^9}
$$

$$
\boxed{v_{LOS}\approx82.063\ \mathrm{m/s}}.
$$


### Problem 3

1. Carrier-phase change

$$
\Delta\phi
=
131\,754\,197.86 - 131\,753\,761.87
$$

$$
=435.90\ \mathrm{cycles}.
$$

Therefore,

$$
\Delta L
=
435.90\times0.1903
$$

$$
\boxed{\Delta L\approx82.969\ \mathrm{m}}.
$$

2. Are they consistent?

They are reasonably close, but not identical. The difference is

$$
82.969-82.017
\approx0.952\ \mathrm{m}.
$$

3. Number of carrier cycles corresponding to the pseudorange change

$$
N_\mathrm{cycles}
\approx
\frac{0.952}{0.1903}
$$

$$
\boxed{N_\mathrm{cycles}\approx5.003\ \mathrm{cycles}}.
$$

The carrier phase changed by approximately $5$ cycles, so there is a noticeable discrepancy.

4. Use Doppler to identify cycle slips

Doppler can be used to compute the range rate (from previous exercise $82.063$ m/s)

$$
\dot \phi = \frac{82.063}{0.1903} = 431.230 \textrm{cycles/s}
$$

Project the number of cycles at epoch $t$ ($\hat \phi_{t+1}$)

$$
\hat \phi_{t+1} = 131\,753\,761.87 - 431.230 \cdot \underbrace{\Delta t}_{1\,s}
$$

$$
\hat \phi_{t+1} = 131\,754,193.100
$$

$$
\Delta \phi = \phi_{t+1} - \hat \phi_{t+1} = 131\,754\,197.86 - 131\,754\,192.86
$$


$$
\boxed{
\Delta \phi = 5\ \textrm{cycles}
}
$$
