# Exercises: Navigation Equations

## Problems


### 1. Navigation equations

Suppose a receiver moving along the $x$-axis and its position is denoted by
only one coordinate ($x_u$).

We got two satellites in view with coordinates:

$$
\begin{matrix}
(x_1,y_1) &= (-3,6)\ \textrm{m} \\
(x_2,y_2) &= (2,2)\ \textrm{m}
\end{matrix}
$$

The measured pseudoranges from each satellites are

$$
\begin{matrix}
PR_1 &= 7\ \textrm{m} \\
PR_2 &= 3\ \textrm{m}
\end{matrix}
$$

Take into account a clock offset in the receiver equal to $c \cdot \delta t_u$

Answer the following questions:

1. Draw an approximate geometry of the problem and the distances involved, to get an intuitive idea of the solution.
2. Write the navigation equations for this problem using an unknown position $x_u$ and the clock offset $c \cdot \delta t_u$.
3. Linearize the previous equations around $x_{u,0} = 1\ \textrm{m}$ and solve them
4. Importance of having a good apriori: Linearize again the navigation equations but around the solution previously found in `2`.

***

## Answers

### 1. Navigation equations

1. Draw the axis and the satellites at the given coordinates, then draw circles around each satellite with radii equal to the measured pseudoranges. The intersection of the circles will give an approximate location of the receiver.

2. The navigation equations are

$$
\begin{matrix}
7 &=& \sqrt{(-3 - x_u)^2 + 6^2} + c \cdot \delta t_u \\
3 &=& \sqrt{(2 - x_u)^2 + 2^2} + c \cdot \delta t_u
\end{matrix}
$$

3. Linearizing the equations around $x_{u,0} = 1\ \textrm{m}$ we get

$$
\begin{matrix}
7 &\approx \underbrace{\sqrt{(-3 - 1)^2 + 6^2}}_{\rho_{0,1}} - \frac{-3 - 1}{\sqrt{(-3 - 1)^2 + 6^2}} \cdot \Delta x + c \cdot \delta t_u \\
3 &\approx \underbrace{\sqrt{(2 - 1)^2 + 2^2}}_{\rho_{0,2}} - \frac{2 - 1}{\sqrt{(2 - 1)^2 + 2^2}} \cdot \Delta x + c \cdot \delta t_u
\end{matrix}
$$

$$
\begin{bmatrix}
7 - \sqrt{(-3 - 1)^2 + 6^2} \\
3 - \sqrt{(2 - 1)^2 + 2^2}
\end{bmatrix}
=
\begin{bmatrix}
-\frac{-3 - 1}{\sqrt{(-3 - 1)^2 + 6^2}} & 1 \\
-\frac{2 - 1}{\sqrt{(2 - 1)^2 + 2^2}} & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
$$

$$
\begin{bmatrix}
-0.2111 \\
0.7639
\end{bmatrix}
=
\begin{bmatrix}
0.5547 & 1 \\
-0.4472 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
$$

This system can be used with Python's `numpy`: `np.dot (np.linalg.inv(A), b)`

$$
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
=
\begin{bmatrix}
-0.97317212 \\
0.32871622
\end{bmatrix}
$$

Therefore, the position is

$$
x_u = x_{u,0} + \Delta x = 1 - 0.97317212 \approx 0.02682788\ \textrm{m}
$$

4. Linearizing again the navigation equations around the solution found in `3` we get:

$$
\begin{bmatrix}
0.2798 \\
0.1905
\end{bmatrix}
=
\begin{bmatrix}
0.4504 & 1 \\
-0.7023 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
=
\begin{bmatrix}
-0.0774 \\
0.2449
\end{bmatrix}
\Rightarrow
x_u = 0.0268 + 0.0774 \approx 0.1043\ \textrm{m}
$$

another iteration:
$$
\begin{bmatrix}
0.2445 \\
0.2443
\end{bmatrix}
=
\begin{bmatrix}
0.4595 & 1 \\
-0.6879 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
\Rightarrow
\begin{bmatrix}
\Delta x \\
c \cdot \delta t_u
\end{bmatrix}
=
\begin{bmatrix}
0.0002 \\
0.2444
\end{bmatrix}
\Rightarrow
x_u = 0.1043 + 0.0002 \approx 0.1045\ \textrm{m}
$$

$$
\boxed{
    \textrm{Having a good apriori is critical!}
}
$$

