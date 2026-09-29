# CSPC PW2 — Lab A

## Result

The noisy position data was used to calculate velocity and acceleration by numerical differentiation.

- Mean acceleration: **-8.58 m/s²**
- Acceleration standard deviation: **28.72 m/s²**
- Largest difference after recovering the position: **0.785 m**

## Analysis

The acceleration data is very noisy because numerical differentiation amplifies measurement noise. This effect becomes even stronger when taking the derivative twice: first to obtain velocity and then to obtain acceleration.

The noisy acceleration was then integrated to recover velocity and position. The recovered position was close to the original measured position, with a maximum difference of **0.785 m**, which is within the expected approximately **1 m** range.

## Conclusion

This lab demonstrates that differentiation amplifies noise, while integration tends to reduce its effect. The results also show that the original motion can be reasonably recovered by integrating the calculated acceleration.
