# Generate fake data for the power law fit question.
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rng

rng.seed(0)

# Sample size
N = 100

# True parameter values
m_min = 1.0
alpha = 2.0

# True masses
m = m_min*(1.0 - rng.rand(N))**(-1.0/alpha)

# SD of measurement errors
sig = 0.5

# Measured masses
x = m + sig*rng.randn(N)

np.savetxt("power_law_data.txt", x)

# Plot
plt.hist(x, 100)
plt.show()

