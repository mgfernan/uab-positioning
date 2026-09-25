# Exercises: Observable combinations

## Problems

### 1. Narrow-lane and wide-lane combinations

1. Write the expression for the narrow- and wide-lane carrier phase combinations.
2. Derive the expression for the effective wavelength of each combination.
3. If $f_{L1} = 1\,575.42\ MHz$ and $f_{L2} = 1\,227.6\ MHz$, what are the corresponding wide and narrowlane combination?

***

## Answers

### 1.

1. The narrow-lane and wide-lane carrier phase combinations are given by:

   - Wide-lane combination:
$$
L_{WL} = \frac{f_a \cdot L_a - f_b \cdot L_b}{f_a - f_b}
$$

   - Narrow-lane combination:
$$
L_{NL} = \frac{f_a \cdot L_a + f_b \cdot L_b}{f_a + f_b}
$$

2. The effective wavelength of each combination can be derived from the carrier phase combinations. :

   - For the wide-lane combination:

$$
\begin{aligned}
L_a &= \dots + \lambda_a \cdot N_a + \dots \\
L_b &= \dots + \lambda_b \cdot N_b + \dots \\
L_{WL} &= \dots + \lambda_{WL} \cdot N_{WL} + \dots \\
&= \frac{f_a \cdot (\dots + \lambda_a \cdot N_a + \dots) - f_b \cdot (\dots + \lambda_b \cdot N_b + \dots)}{f_a - f_b} \\
&= \dots + \frac{f_a \cdot \lambda_a \cdot N_a - f_b \cdot \lambda_b \cdot N_b}{f_a - f_b} + \dots \\
&= \dots + \frac{f_a \cdot \frac{c}{f_a} \cdot N_a - f_b \cdot \frac{c}{f_b} \cdot N_b}{f_a - f_b} \\
&= \dots + \frac{c \cdot N_a - c \cdot N_b}{f_a - f_b} + \dots \\
&= \dots + \frac{c}{f_a - f_b} \cdot (N_a - N_b) + \dots \\
\end{aligned}
$$

$$
\begin{aligned}
\lambda_{WL} &= \frac{c}{f_a - f_b} \\
&= \frac{c}{\frac{c}{\lambda_a} - \frac{c}{\lambda_b}} \\
&= \frac{\lambda_a \cdot \lambda_b}{\lambda_b - \lambda_a} \\
\end{aligned}
$$

   - For the narrow-lane combination:

$$
\begin{aligned}
\lambda_{NL} &= \frac{c}{f_a + f_b} \\
&= \frac{c}{\frac{c}{\lambda_a} + \frac{c}{\lambda_b}} \\
&= \frac{\lambda_a \cdot \lambda_b}{\lambda_b + \lambda_a} \\
\end{aligned}
$$