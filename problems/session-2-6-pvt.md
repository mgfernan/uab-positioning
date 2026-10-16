# Exercises: PVT

## 1. PVT: single point positioning

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

### 1. Answer

see [this notebook for the solution of the problem](notebooks/pvt_solution_2D.ipynb)

***

## 2. DOP computation

A receiver is located at $(1, 1)$ and receives signals from three transmitters located at:

`Scenario A`

$$
T_{A,1} = (5, 2)\\
T_{A,2} = (-2, 4)\\
T_{A,3} = (0, -4)
$$


`Scenario B`

$$
T_{B,1} = (5, 2)\\
T_{B,2} = (-4, -7)\\
T_{B,3} = (0, -4)
$$

1. Compute the DOP for both scenarios. Which one is better?

### 2. Answer

see [this notebook for the solution of the problem](notebooks/pvt_dop_computation.ipynb)

***

## 3. DOP computation and transmitter selection

Four transmitters are located at:

$$
T_1 = (5, 2)
T_2 = (−2, 4)
T_3 = (0, −4)
T_4 = (7, 3)
$$

and the receiver is located approximately at position:

$$
R = (0, 0)
$$

Answer these questions:

1. Which is the minimum number of pseudorange measurements that the receiver needs to calculate its position?
2. This receiver has very limited computing power and can only use three pseudorange measurements to calculate its position. At first glance, which of the four pseudorange measurements would you discard for the calculation? Why?
3. Calculate the PDOP (Position Dilution of Precision).
4. Calculate the PDOP for the transmitter combinations
[1, 2, 3]
[2, 3, 4]
5. Why do they have such similar values?
6. Intuitively, if we use the transmitter combination
[1, 3, 4]
will the PDOP be better or worse?

### 3. Answers

The problem is solved in [this notebook](notebooks/pvt_dop_computation_tx_selection.ipynb).

1. The minimum number of pseudorange measurements that the receiver needs to calculate its position in 2D is three. In 3D, it would be four.
2. Looking at the positions of the transmitters, it is clear that Transmiiter 1 (T1, located at (5, 2)) should be discarded as it is aligned with Transmitter 4 (T4, located at (7, 3)).
3. Check notebook for the solution of the problem.
4. Check notebook for the solution of the problem.
5. Because T1 and T4 are aligned and thus they offer a very similar geometry
