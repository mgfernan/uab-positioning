# Exercises: PVT

## Problems

### 1. PVT: single point positioning

A receiver receives the signal from three transmitters located at

$$
T_1 = (5, 2)\\
T_2 = (-2, 4)\\
T_3 = (0, -4)
$$

The receiver measures the pseudoranges

$$
\rho_1 = 4.32\ \text{m} \\
\rho_2 = 4.54\ \text{m} \\
\rho_3 = 5.40\ \text{m}
$$

1. Draw the transmitters and the circles corresponding to the different pseudoranges.

2. Do all the circles intersect at a single point? Why?

3. Another receiver, located at the same position as the first receiver, measures the pseudoranges below. Is it possible to draw all the pseudorange circles for this receiver?

$$
\rho_1' = -0.38\ \text{m} \\
\rho_2' = -0.26\ \text{m} \\
\rho_3' = 0.90\ \text{m}
$$

4. What does it mean for the pseudoranges to be negative?

5. Set up the system of equations (Least Squares) that you would use to compute the position solution for cases above around the initial *a-priori* point $(1, 1)$.

6. If the position solution are $(1, 2, 1\times 10^{-9})$ and $(1, 2, -15\times 10^{-9})$ for the two cases above, what is the difference between them?

7. What is the clock offset of the receivers?

***

## Answers

### 1.


see [this notebook for the solution of the problem](notebooks/session_2_5_pvt_1.ipynb)