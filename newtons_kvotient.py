import matplotlib.pyplot as plt
import sys

# Test function and analytic derivative
def f(x):
    return x**2+x

def fder(x):
    return 2*x + 1

# symmetric derivative
def asyder(x):
    h = 0.0001
    return (f(x + h) - f(x - h)) / (2 * h)

# arrays for printing
fs = []
an = []
sy = []
ys = []

n = 700
h = 0.01

# Populate print data
for i in range(0, n):
    fs.append(f(i * h))
    an.append(fder(i * h))
    sy.append(asyder(i * h) - 1)
    ys.append(i * h)

# Print data
plt.plot(ys, fs)
plt.plot(ys, an)
plt.plot(ys, sy)
plt.show()
