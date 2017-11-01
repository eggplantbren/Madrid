import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import factorial

# Hypothesis space
x = np.arange(0, 30)

# Three poisson distributions
p1 = 3.0**x * np.exp(-3.0) / factorial(x)
#p1 = p1/p1.sum()

p2 = 6.0**x * np.exp(-6.0) / factorial(x)
#p2 = p2/p2.sum()

p3 = 15.0**x * np.exp(-15.0) / factorial(x)
#p3 = p3/p3.sum()


# Set fonts
plt.rc("font", size=16, family="Serif", serif="Computer Sans")
plt.rc("text", usetex=True)

# Make the plot
plt.bar(x, p1, alpha=0.4, label=r"$\lambda = 3$")
plt.bar(x, p2, alpha=0.4, label=r"$\lambda = 6$")
plt.bar(x, p3, alpha=0.4, label=r"$\lambda = 15$")
plt.xlabel(r"$x$")
plt.ylabel("Probability")
plt.legend(loc="upper right")
plt.savefig("poisson.pdf")

