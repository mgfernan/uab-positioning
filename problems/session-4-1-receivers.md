# Exercises: Receivers

## RF Front-End

### Noise power and noise figure


In the following system:

```{mermaid}
flowchart LR
    ANT["📡 <b>Antenna</b><br/>Pin = −160 dBW<br/>TA = 100 K"]
    G1["<b>LNA</b><br/>G1 = 15 dB<br/>F1 = 2 dB<br/>T1 = ?"]
    G2["<b>LNA</b><br/>G2 = 35 dB<br/>F2 = 3 dB<br/>T2 = ?"]
    FILT["<b>Bandpass Filter</b><br/>B = 20 MHz<br/>G3 = −4 dB<br/>F3 = ?<br/>T3 = ?"]
    G4["<b>LNA</b><br/>G4 = 30 dB<br/>F4 = 3.5 dB<br/>T4 = ?"]
    MIX(("<b>Mixer</b><br/>G5 = −15 dB<br/>F5 = 15 dB<br/>T5 = ?"))
    G6["<b>LNA</b><br/>G6 = 40 dB<br/>F6 = 6 dB<br/>T6 = ?"]

    ANT --> G1 --> G2 --> FILT --> G4 --> MIX --> G6

    classDef antenna fill:#fff,stroke:#333,stroke-width:1.5px
    classDef amp fill:#fff,stroke:#333,stroke-width:1.5px
    classDef filter fill:#fff,stroke:#333,stroke-width:1.5px
    classDef mixer fill:#fff,stroke:#333,stroke-width:1.5px

    class ANT antenna
    class G1,G2,G4,G6 amp
    class FILT filter
    class MIX mixer
```


Compute the following parameters:

1. Receiver noise temperature: $T_R$
2. Systemnoise temperature: $T_{sys}$
3. Receiver gain: $G$
4. Equivalent spectral noise density at the input of the receiver: $N_{0,in}$
5. Equivalent spectral noise density at the output of the receiver: $N_{0,out}$
6. Signal power at the output of the receiver: $P_{out}$
7. Noise power at the output of the receiver: $N_{out}$
8. SNR at the output of the receiver: $SNR_{out}$
9. Carrier to spectral noise density at the output of the reciever: $(C/N_0)_{out}$

### Answers:


1. Noise temperature $T_R$

First we need to compute the noise figure for the whole system (Friss formula).

$$
\begin{aligned}
F_1 &= 2 \ dB = 10^{\frac{2}{10}} = 1.58 & \qquad G_1 &= 15 \ dB = 10^{\frac{15}{10}} = 31.623 \\
F_2 &= 3 \ dB = 10^{\frac{3}{10}} = 1.995 & \qquad G_2 &= 35 \ dB = 10^{\frac{35}{10}} = 3162.28 \\
F_3 &= 4 \ dB = 10^{\frac{4}{10}} = 2.512 & \qquad G_3 &= -4 \ dB = 10^{\frac{-4}{10}} = 0.398 \\
F_4 &= 3.5 \ dB = 10^{\frac{3.5}{10}} = 2.239 & \qquad G_4 &= 30 \ dB = 10^{\frac{30}{10}} = 1000 \\
F_5 &= 15 \ dB = 10^{\frac{15}{10}} = 31.623 & \qquad G_5 &= -15 \ dB = 10^{\frac{-15}{10}} = 0.0316 \\
F_6 &= 6 \ dB = 10^{\frac{6}{10}} = 3.98 & \qquad G_6 &= 40 \ dB = 10^{\frac{40}{10}} = 10000 \\
\end{aligned}
$$

$$
\begin{aligned}
F &= 1.58 + \frac{1.995-1}{31.623} + \frac{2.512-1}{31.623 \cdot 3162.28} \\
&+ \frac{2.239-1}{31.623 \cdot 3162.28 \cdot 0.398} + \frac{31.623-1}{31.623 \cdot 3162.28 \cdot 0.398 \cdot 1000} \\
&+ \frac{3.98-1}{31.623 \cdot 3162.28 \cdot 0.398 \cdot 1000 \cdot 0.0316} \\
&= 1.58 + 0.0315 + 0.000015 + 0.000031 + 0.00000076 + 0.0000024 = 1.612 \\
\end{aligned}
$$

Assumint a $T_0 = 290 K$, the receiver noise temperature is:

$$
\boxed{
T_R = 290 \cdot (1.612 - 1) = 177.5 \ K
}
$$

2. $T_{sys} = T_A + T_R = 100 + 177.5 = 277.5\ K$

3. Receiver gain: $G = G_1 + G_2 + G_3 + G_4 + G_5 + G_6 = 15 + 35 -4 +30 -15 +40 = 101 dB$

4. At the input (before the overall gain): $N_{0,in} = k \cdot T_{sys} =1.38 \cdot 10^{-23} \cdot 277.5 = 3.83 \cdot 10^{-21} W/Hz = -204.17\ dB\ Hz$

5. At the output (after the overall gain): $N_{0,out} = N_{0,in} + G = -204.17 + 101 = -103.17\ dB\ Hz$

6. Signal power at the output of the receiver: $P_{out} = P_{in} + G = -160 + 101 = -59\ dBW$

7. Noise power at the output of the receiver: $N_{out} = N_{0,out} + 10 \cdot \log_{10}(B) = -103.17 + 10 \cdot \log_{10}(20 \cdot 10^6) = -103.17 + 73.01 = -30.16\ dBW$

8. SNR at the output of the receiver: $SNR_{out} = P_{out} - N_{out} = -59 - (-30.16) = -28.84\ dB$

9. Carrier to spectral noise density at the output of the reciever: $(C/N_0)_{out} = P_{out} - N_{0,out} = -59 - (-103.17) = 44.17\ dB\ Hz$

