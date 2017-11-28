import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.misc

# Lambda
lamb = 10.0

# Set of possible xs
xs = np.arange(0, 100)

# Poisson distribution
ps = np.exp(-lamb)*lamb**xs / scipy.misc.factorial(xs)

# Plot it
plt.bar(xs, ps)
plt.show()

# Expected value and standard deviation
ex = np.sum(xs*ps)
var = np.sum((xs - ex)**2*ps)
sd = np.sqrt(var)
print(ex, sd)


# Probability of 10 photons in a 1second time interval
p10 = ps[xs == 10]
print(p10)

# Non-overlapping intervals are independent, so probability
# 10 photons in two consecutive intervals is
print(p10**2)
