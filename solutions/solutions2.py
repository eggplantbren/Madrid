import matplotlib.pyplot as plt
import numpy as np
import scipy.misc

# QUESTION 1
# (a)

# The expected number of photons
lamb = 10.0

# Grid of possibilities for x
xs = np.arange(0, 101)

# Probability distribution
ps = lamb**xs * np.exp(-lamb) / scipy.misc.factorial(xs)

# Expected value and standard deviation
ex = np.sum(ps*xs)
var = np.sum(ps*(xs - ex)**2)
sd = np.sqrt(var)

# Print result
print("1(a): E(x) = {e}, sd(x) = {s}".format(e=ex, s=sd))


# (b)
# The probability of 10 photons in a second
p10 = ps[xs == 10][0]

# The probability of 10 photons in two non-overlapping seconds
print("1(b):", p10**2)


# QUESTION 2
# (a)

# A grid
xs = np.linspace(-10.0, 10.0, 10001)

# Probability density
ps = np.exp(-0.5*xs**2) / np.sqrt(2*np.pi)

# Plot
plt.plot(xs, ps)
plt.xlabel("$x$")
plt.ylabel("Probability Density")
plt.title("2(a)")
plt.show()

# (b)
# Probability in the interval
prob = np.trapz(ps*(np.abs(xs) <= 1.0), x=xs)
print("2(b):", prob)

# (c)
# Probability in the interval
prob = np.trapz(ps*(np.abs(xs) <= 2.0), x=xs)
print("2(c):", prob)

# (d)
# Expected value and standard deviation
ex = np.trapz(ps*xs, x=xs)
var = np.trapz(ps*(xs - ex)**2, x=xs)
sd = np.sqrt(var)

# Print result
print("2(e): E(x) = {e}, sd(x) = {s}".format(e=ex, s=sd))

# (e)
# For this question, the range from x=-10 to x=10 might
# slightly affect the results, but no worries
# Create the t density
nu = 3.0
ps = (1.0 + xs**2/nu) ** (-0.5*(nu + 1.0))

# Normalise it
ps = ps/np.trapz(ps, x=xs)

# Probability in the interval
prob = np.trapz(ps*(np.abs(xs) <= 2.0), x=xs)
print("2(e):", prob)

# It's lower than 2(c) because of the heavy tails.

