# LEO positioning: Derivation of the Doppler Jacobian

## Problem statement

For satellite $i$ at epoch $k$ and a stationary user $u$, the Doppler shift is

$$
f_{D,i,k} = -\frac{f_0}{c} \left(\mathbf{v}_{i,k} \cdot \mathbf{e}_{i,k} + \dot{\delta t}_u - \dot{\delta t}_{i,k}\right) + \varepsilon_{D,i,k}
$$

where the geometric range and line-of-sight unit vector are

$$
\rho_{i,k} = \|\mathbf{r}_{i,k} - \mathbf{r}_u\| = \sqrt{(x_{i,k} - x_u)^2 + (y_{i,k} - y_u)^2 + (z_{i,k} - z_u)^2}
$$

$$
\mathbf{e}_{i,k} = \frac{\mathbf{r}_{i,k} - \mathbf{r}_u}{\rho_{i,k}}
$$

The estimated state is $\mathbf{x}_u = [\mathbf{r}_u^{T}, \dot{\delta t}_u]^{T}$; receiver velocity is fixed to zero, and receiver clock drift is assumed constant over the observation arc.

## Linearization about an a priori state

The model is nonlinear in $\mathbf{r}_u$, so it is linearized about an a priori state $\mathbf{x}_0 = [\mathbf{r}_0^{T}, \dot{\delta t}_0]^{T}$ (e.g., a coarse position and zero clock drift). The true state is written as the a priori plus a correction:

$$
\mathbf{r}_u = \mathbf{r}_0 + \Delta\mathbf{r},
\qquad
\dot{\delta t}_u = \dot{\delta t}_0 + \delta\dot{t},
\qquad
\Delta\mathbf{x} = \begin{bmatrix} \Delta\mathbf{r}^{T}, & \Delta\dot{t} \end{bmatrix}^{T}.
$$

Denote the modelled Doppler by $f_{D,i,k}(\mathbf{x}_u)$. A first-order Taylor expansion around $\mathbf{x}_0$ gives

$$
f_{D,i,k}(\mathbf{x}_u) \approx f_{D,i,k}(\mathbf{x}_0) + \left.\frac{\partial f_{D,i,k}}{\partial \mathbf{x}_u}\right|_{\mathbf{x}_0} \delta\mathbf{x}
= f_{D,i,k}(\mathbf{x}_0) + \mathbf{H}_{i,k}\,\Delta\mathbf{x}.
$$

Moving the a priori prediction to the left-hand side yields the observed-minus-computed residual, which is the measurement of the linearized problem:

$$
z_{i,k} = f_{D,i,k}^{\text{obs}} - f_{D,i,k}(\mathbf{x}_0) = \mathbf{H}_{i,k}\,\Delta\mathbf{x} + \varepsilon_{D,i,k}.
$$

All geometric quantities below ($\rho_{i,k}$, $\mathbf{e}_{i,k}$, ...) are therefore evaluated at the a priori position, using the known satellite-to-a-priori offset

$$
\mathbf{d}_{i,k} = \mathbf{r}_{i,k} - \mathbf{r}_0 = [d_{x,i,k}, d_{y,i,k}, d_{z,i,k}]^{T},
\qquad
\rho_{i,k} = \|\mathbf{d}_{i,k}\|,
\qquad
\mathbf{e}_{i,k} = \frac{\mathbf{d}_{i,k}}{\rho_{i,k}}.
$$

The offset $\mathbf{d}_{i,k}$ is known and is not the unknown correction $\Delta\mathbf{r}$. They are related through the true line of sight, $\mathbf{r}_{i,k} - \mathbf{r}_u = \mathbf{d}_{i,k} - \Delta\mathbf{r}$, so $\mathbf{d}_{i,k}$ is the true line of sight when $\Delta\mathbf{r} = \mathbf{0}$.

## Derivative with respect to user position

For a stationary user ($\mathbf{v}_u = \mathbf{0}$), and holding the velocities and clock drifts fixed, the position derivative is

$$
\frac{\partial f_{D,i,k}}{\partial \mathbf{r}_u} = -\frac{f_0}{c} \mathbf{v}_{i,k}^{T} \frac{\partial \mathbf{e}_{i,k}}{\partial \mathbf{r}_u}.
$$

Here, the derivative of the unit vector is a matrix. The derivatives are evaluated at $\mathbf{r}_u = \mathbf{r}_0$, where $\mathbf{r}_{i,k} - \mathbf{r}_u = \mathbf{d}_{i,k}$. Let $e_x = d_{x,i,k}/\rho_{i,k}$, with analogous definitions for $e_y$ and $e_z$. Since

$$
\frac{\partial \rho_{i,k}}{\partial x_u} = -\frac{d_{x,i,k}}{\rho_{i,k}},
$$

the quotient rule gives

$$
\frac{\partial e_x}{\partial x_u}
= -\frac{1}{\rho_{i,k}} + \frac{d_{x,i,k}^2}{\rho_{i,k}^3}
= -\frac{1-e_x^2}{\rho_{i,k}}.
$$

Because $d_{x,i,k}$ does not depend on $y_u$ or $z_u$, the cross-partials are

$$
\frac{\partial e_x}{\partial y_u}
= \frac{d_{x,i,k}\,d_{y,i,k}}{\rho_{i,k}^3}
= \frac{e_x e_y}{\rho_{i,k}},
\qquad
\frac{\partial e_x}{\partial z_u}
= \frac{d_{x,i,k}\,d_{z,i,k}}{\rho_{i,k}^3}
= \frac{e_x e_z}{\rho_{i,k}}.
$$

The other components follow by symmetry, giving

$$
\frac{\partial \mathbf{e}_{i,k}}{\partial \mathbf{r}_u}
= \frac{1}{\rho_{i,k}}
\begin{bmatrix}
-(1-e_x^2) & e_x e_y & e_x e_z \\
e_y e_x & -(1-e_y^2) & e_y e_z \\
e_z e_x & e_z e_y & -(1-e_z^2)
\end{bmatrix}
= -\frac{1}{\rho_{i,k}}\left(\mathbf{I}_3 - \mathbf{e}_{i,k}\mathbf{e}_{i,k}^{T}\right).
$$

## Derivative with respect to user clock drift

The Doppler model is linear in the user clock drift $\dot{\delta t}_u$. Its partial derivative is therefore

$$
\frac{\partial f_{D,i,k}}{\partial \dot{\delta t}_u} = -\frac{f_0}{c}.
$$

## Jacobian terms

For a stationary user, $\dot{\rho}_{i,k} = \mathbf{v}_{i,k} \cdot \mathbf{e}_{i,k}$, evaluated at the a priori position. The Jacobian row $\mathbf{H}_{i,k} = [H^{(x)}, H^{(y)}, H^{(z)}, H^{(\dot{\delta t}_u)}]$ multiplies the corrections $\delta\mathbf{x}$ (not the absolute coordinates). Its position components are

$$
\begin{aligned}
H_{i,k}^{(x)} &= \frac{f_0}{c\rho_{i,k}} \left(v_{i,k}^{(x)} - \dot{\rho}_{i,k} e_{i,k}^{(x)}\right) \\
&= \frac{f_0}{c\rho_{i,k}^3} \left(v_{i,k}^{(x)} (d_{y,i,k}^2 + d_{z,i,k}^2) - v_{i,k}^{(y)} d_{x,i,k}d_{y,i,k} - v_{i,k}^{(z)} d_{x,i,k}d_{z,i,k}\right), \\
H_{i,k}^{(y)} &= \frac{f_0}{c\rho_{i,k}^3} \left(-v_{i,k}^{(x)} d_{x,i,k}d_{y,i,k} + v_{i,k}^{(y)} (d_{x,i,k}^2 + d_{z,i,k}^2) - v_{i,k}^{(z)} d_{y,i,k}d_{z,i,k}\right), \\
H_{i,k}^{(z)} &= \frac{f_0}{c\rho_{i,k}^3} \left(-v_{i,k}^{(x)} d_{x,i,k}d_{z,i,k} - v_{i,k}^{(y)} d_{y,i,k}d_{z,i,k} + v_{i,k}^{(z)} (d_{x,i,k}^2 + d_{y,i,k}^2)\right), \\
H_{i,k}^{(\dot{\delta t}_u)} &= -\frac{f_0}{c}.
\end{aligned}
$$

## Stacked linear system

Stacking all satellites and epochs gives

$$
\mathbf{z} = \mathbf{H}\,\Delta\mathbf{x} + \boldsymbol{\varepsilon},
\qquad
\Delta\hat{\mathbf{x}} = (\mathbf{H}^{T}\mathbf{W}\mathbf{H})^{-1}\mathbf{H}^{T}\mathbf{W}\,\mathbf{z},
$$

with $\mathbf{W}$ the measurement weight matrix. The state is then updated as $\mathbf{x}_0 \leftarrow \mathbf{x}_0 + \Delta\hat{\mathbf{x}}$, and the process is iterated (recomputing $\mathbf{z}$ and $\mathbf{H}$ at the new $\mathbf{x}_0$) until $\|\Delta\hat{\mathbf{r}}\|$ is below a threshold.


