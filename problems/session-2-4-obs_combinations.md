# Exercises: Observable combinations

## Problems

### 1. Narrow-lane and wide-lane combinations

1. Write the expression for the narrow- and wide-lane carrier phase combinations.
2. Derive the expression for the effective wavelength of each combination.
3. If $f_{L1} = 1\,575.42\ MHz$ and $f_{L2} = 1\,227.6\ MHz$, what are the corresponding wide and narrowlane combination?

### 2. GRAPHIC combination

1. Write the expression for the GRAPHIC combination.
2. What is the effective wavelength of the GRAPHIC combination?
3. How large is the ionospheric delay for this combination?
4. What is the effective noise for this combination?
5. What would be the maximum noise of the code measurement (at $f_{L1} = 1\ 575.42\ MHz$) for which it would be possible to solve for the integer ambiguity of the GRAPHIC combination?

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

3. If $f_{L1} = 1\,575.42\ MHz$ and $f_{L2} = 1\,227.6\ MHz$, the corresponding wide and narrow-lane combinations are:

   - Wide-lane combination:
$$
\lambda_1 = \frac{c}{f_{L1}} \approx 0.190293672\ m
\lambda_2 = \frac{c}{f_{L2}} \approx 0.244210213\ m
\lambda_{WL} \approx 0.862\ m
$$

    - Narrow-lane combination:
$$
\lambda_{NL} \approx 0.107\ m
$$

### 2.

1. The GRAPHIC combination is given by:
$$
\begin{aligned}
PR_{GRAPHIC,a} &= \frac{PR_a + L_a}{2} \\
&= \rho + c \cdot dt + T + \frac{\lambda_a}{2}\cdot N_a + \frac{\varepsilon_{PR}}{2} + \frac{\varepsilon_L}{2}
\end{aligned}
$$

2. The effective wavelength of the GRAPHIC combination is:
$$
\lambda_{GRAPHIC} = \frac{\lambda_a}{2}
$$

3. The ionospheric delay for this combination is $0$ (cancels out)
4.
$$
\varepsilon_{GRAPHIC} = \frac{\varepsilon_{PR}}{2} + \frac{\varepsilon_L}{2} \approx \frac{\varepsilon_{PR}}{2}
$$

$$
\sigma_{\varepsilon,{GRAPHIC}} = \frac{\sigma_{\varepsilon,PR}}{\sqrt{2}}
$$

5. The maximum noise of the code measurement for which it would be possible to solve for the integer ambiguity of the GRAPHIC combination is:

$$
\begin{aligned}
\lambda_1 &= 0.190293672\ m \\
\lambda_{GRAPHIC} &= \frac{\lambda_1}{2} \approx 0.095146836\ m \\
\sigma_{\varepsilon,PR} &< \frac{\lambda_{GRAPHIC}}{2} \\
\sigma_{\varepsilon,PR} &< 0.047573418\ m
\end{aligned}
$$

