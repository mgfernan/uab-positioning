# Exercises: Positioning Errors

## Problems


### 1. Error budget and UERE

Consider a simplified GNSS pseudorange error budget with the following $1\sigma$ uncertainties:

| Error source | Standard deviation |
|---|---:|
| Satellite clock | $0.7\ m$ |
| Ephemeris | $0.8\ m$ |
| Ionosphere | $1.5\ m$ |
| Troposphere | $0.5\ m$ |
| Receiver noise | $0.4\ m$ |
| Multipath | $0.8\ m$ |

Assume that the errors are statistically independent.

1. Calculate the total UERE.
2. Which error source contributes most to the total variance?
3. If the ionospheric error is reduced from $1.5\ m$ to $0.5\ m$, calculate the new UERE.


### 2. From UERE to position accuracy

A receiver has an estimated UERE of

$$
\sigma_{UERE}=1.5\ m.
$$

For a particular satellite geometry, the position dilution of precision is

$$
PDOP=2.0.
$$

Assuming the simplified relationship

$$
\sigma_{pos}\approx PDOP\cdot\sigma_{UERE},
$$

1. Estimate the 3-D position standard deviation.
2. Repeat for \(PDOP=5\).
3. Explain the difference between an **error source** and **geometry amplification**.


***

## Answers

### 1.

For independent errors,

$$
\sigma_{UERE}
=
\sqrt{
\sum_i \sigma_i^2
}.
$$

1.

$$
\sigma_{UERE}
=
\sqrt{
0.7^2+
0.8^2+
1.5^2+
0.5^2+
0.4^2+
0.8^2
}
$$

$$
\boxed{
\sigma_{UERE}\approx2.10\ m
}
$$

2. The ionosphere has the largest variance contribution:

$$
\sigma_I^2=1.5^2=2.25\ m^2.
$$

3. With $\sigma_I=0.5\ m$,

$$
\sigma_{UERE,new}
=
\sqrt{
0.7^2+
0.8^2+
0.5^2+
0.5^2+
0.4^2+
0.8^2
}
$$

$$
\boxed{
\sigma_{UERE,new}\approx1.56\ m
}
$$

***

### 2.

1.

$$
\sigma_{pos}
\approx2.0(1.5)
=3.0\ m.
$$

2.

$$
\sigma_{pos}
\approx5(1.5)
=7.5\ m.
$$

3. UERE describes the uncertainty associated with the measurements and their error sources. PDOP describes how the satellite geometry maps those measurement errors into position errors. Thus, poor geometry can amplify the effect of the same underlying measurement errors.