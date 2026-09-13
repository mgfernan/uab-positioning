# Exercises: From ECEF (XYZ) to ENU

These exercises illustrate the transformation from Earth-Centered, Earth-Fixed (ECEF) Cartesian coordinates $(X,Y,Z)$ to the local East-North-Up (ENU) frame.

The goal is not only to obtain the numerical answer, but also to develop an **intuition for what the transformation does**.


## What does the transformation do?

Consider a *displacement* (e.g. error) around a point $r_{XYZ}=(X, Y, Z)$ expressed in ECEF coordinates:

$$
\mathbf{r}_{\Delta} =
\begin{array}
\Delta X \\
\Delta Y \\
\Delta Z
\end{array}
=
\begin{array}
X - X_0\\
Y - Y_0\\
Z - Z_0
\end{array}
$$

and a local ENU frame located at a reference point $(X_0, Y_0, Z_0)$.

The ENU coordinates describe the same displacement using three **local directions**:

- **E**: East
- **N**: North
- **U**: Up

The transformation can be written as

$$
\begin{array}
E\\
N\\
U
\end{array}
=
\mathbf{R}
\begin{array}
\Delta X\\
\Delta Y\\
\Delta Z
\end{array}
$$

where

$$
\begin{array}
\Delta X\\
\Delta Y\\
\Delta Z
\end{array}
=
\begin{array}
X-X_0\\
Y-Y_0\\
Z-Z_0
\end{array}
$$

is the displacement from the reference point.

For a reference position with geodetic latitude $\phi$ and longitude $\lambda$:

$$
\mathbf{R} =
\begin{array}
-\sin\lambda & \cos\lambda & 0\\
-\sin\phi\cdot\cos\lambda &-\sin\phi\cdot\sin\lambda&\cos\phi \\
\cos\phi\cdot\cos\lambda&\cos\phi\cdot\sin\lambda&\sin\phi
\end{array}
$$

***

# Part A — Developing intuition

## Exercise 1 — A displacement purely along canonical axis

Suppose the reference location is at

$$
r_0 = (X_0,Y_0,Z_0)=(1,0,0)\ \Rightarrow\ \lambda_0 = 0^\circ, \phi_0 = 0^\circ
$$

and the displacement vector $r_{\Delta}$ relative to $r_0$ is

$$
r_\Delta = (2,0,0)
$$

### Questions

1. Build up the geometrical intuition: draw the $r_0$ and $r_\Delta$ vectors along with a unit-radius sphere?
2. Without doing any computation, what is the value of the $r_{\Delta, ENU}$ arrays for these cases:
   1. $r_{\Delta, XYZ} = (2,0,0)$
   2. $r_{\Delta, XYZ} = (0,2,0)$
   3. $r_{\Delta, XYZ} = (0,0,2)$
3. Compute the $\mathbf{R}_{\lambda_0 = 0^\circ, \phi_0 = 0^\circ}$ matrix.
4. Recompute the values mathematically. Do they match the $r_{\Delta, ENU}$ you obtained before?

***

## Exercise 2 — Impact of reference point in the transformation

This exercise will help building the intuition by changing the reference point ($r_0$)

### Questions

Compute the $r_{\Delta, ENU}$ for these cases:

1. $r_0=(0, 1, 0);\ r_{\Delta, XYZ}=(0, 2, 0)$
2. $r_0=(0, 0, 1);\ r_{\Delta, XYZ}=(0, 0, 2)$

***

# Part B — Simple rotations


Now we use, as reference position, the following location

$$
\lambda_0=45^\circ;\ \phi_0=45^\circ
$$

Recall that:

$$
\sin45^\circ=\cos45^\circ=\frac{\sqrt2}{2}\approx0.7071.
$$

## Exercise 1 — XYZ (ECEF) to ENU rotation

### Questions

1. Compute the rotation matrix $R_{\lambda_0=45^\circ;\ \phi_0=45^\circ}$
The transformation therefore becomes
2. Given a displacement vector $r_{\Delta, XYZ} = (1, 0, 0)$, build an intuition on the geometry by drawing this vector from the reference point.
3. Compute the $r_{\Delta, ENU}$. Do the values match your intuition, qualitatively?

***


# Answers

## Exercise A.1

1. (drawing)
2. $r_{ENU}$
   1. $r_{\Delta, ENU} = (0,0,2)$
   2. $r_{\Delta, ENU} = (2,0,0)$
   3. $r_{\Delta, ENU} = (0,2,0)$
3.
$$
\mathbf{R}_{\lambda_0 = 0^\circ, \phi_0 = 0^\circ} =
\begin{array}
0 & 1 & 0\\
0 & 0 & 1\\
1 & 0 & 0
\end{array}
$$
4. Matrix product. Same results of point 2.

***

## Exercise A.2

1. $r_{\Delta, ENU} = (0, 0, 2)$
2. $r_{\Delta, ENU} = (0, 0, 2)$

***

## Exercise B.1

1. Rotation matrix
$$
R_{\lambda_0=45^\circ;\ \phi_0=45^\circ} =
\begin{array}
-\frac{\sqrt 2}{2} & \frac{\sqrt 2}{2} & 0\\
-\frac{1}{2} & -\frac{1}{2} & \frac{\sqrt 2}{2}\\
\frac{1}{2} & \frac{1}{2} & \frac{\sqrt 2}{2}
\end{array}
$$

2. Reference point in XYZ (ECEF): $r_0=(0.500,0.500,0.707)$. Draw a unit-sphere, place the $r_0$ and the $r_\Delta$ arrays.
3. $$r_{\Delta, ENU} = \left( -\frac{\sqrt 2}{2}, -\frac{1}{2}, \frac{1}{2} \right)$$
