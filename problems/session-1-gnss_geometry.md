# GNSS Introduction

## GNSS geometry

These are simple exercises aimed at getting a feeling on what are the numbers
associated to the GNSS geometry.

Consider this diagram showing a basic (2D) GNSS geometry

![](../assets/figures/gnss_geometry.svg)

Assume the following kown data:


- $h_{GNSS} = h_{GPS} = 20.200\ km$
- $R_{Earth} = 6.371\ km$

1. Compute the following amounts related to $distance$ ($range$):

    1. The distance between the receiver and the satellite at high elevation (i.e. overhead), $R_h$?
    2. The travel time for the signal received overhead ($\tau_h$)?
    3. The distance between the receiver when the satellite is at low elevation (i.e. horizon), $R_l$?
    4. The travel time for the signal received at low elevation ($\tau_l$)

2. Regarding $\color{blue}{velocity}$ ($\color{blue}{Doppler}$)...

    1. What is the meaning of *along-range* and *across-range*?
    2. Considering that the Doppler is relative to the range direction, which of these components should be taken to compute velocity or Doppler?
    3. What is the Doppler shift for overhead (high elevation) observations?
    4. Compute the $\alpha$ angle.
    5. What is the orbital speed of GPS satellites? (you may need to look the slides)
    6. At the low elevation position, is the satellite approaching or going away? Will the Doppler shift be positive (higher frequency?) or negative (lower frequency)? What is the Doppler shift value for low elevation observations? Remember that:
    $$|\Delta f| = \frac{v_{LOS}}{c}\cdot f_0\quad with \quad f_0=1.575,42\ MHz$$

3. Regarding the clock offset in the range:
   1. What is the range error if we have a $1\ \mu s$ clock offset?