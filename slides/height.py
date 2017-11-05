import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

# Use Dan FM's favourite fonts
plt.rc("font", size=20, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

# Possible values for x
x = np.linspace(1.3, 2.2, 10001)

# p(x)
mu, sig = 1.778, 0.102
p = 1.0/sig/np.sqrt(2*np.pi)*np.exp(-0.5*(x - mu)**2/sig**2)

# Plot the density
plt.plot(x, p, "k-", linewidth=2)
plt.gca().fill_between(x[(x >= 1.5) & (x <= 2.0)],\
                y1=p[(x >= 1.5) & (x <= 2.0)], color="grey", alpha=0.2)
plt.gca().fill_between(x[(x >= 1.8) & (x <= 2.0)],\
                y1=p[(x >= 1.8) & (x <= 2.0)], color="blue", alpha=0.2)
plt.xlabel("Height (m)")
plt.ylabel("Frequency density, $f(x)$")
plt.xlim([x.min(), x.max()])
plt.ylim([0.0, 1.2*p.max()])
plt.title("Frequency distribution of mens' heights")
plt.savefig("height1.pdf", bbox_inches="tight")


# Plot the density
plt.clf()
plt.plot(x, p, "k-", linewidth=2)
plt.gca().fill_between(x[(x >= 1.5) & (x <= 2.0)],\
                y1=p[(x >= 1.5) & (x <= 2.0)], color="grey", alpha=0.2)
plt.gca().fill_between(x[(x >= 1.8) & (x <= 2.0)],\
                y1=p[(x >= 1.8) & (x <= 2.0)], color="blue", alpha=0.2)
plt.xlabel("Height (m)")
plt.ylabel("Probability Density, $f(x)$")
plt.xlim([x.min(), x.max()])
plt.ylim([0.0, 1.2*p.max()])
plt.title("Probability distribution for a single height")
plt.savefig("height2.pdf", bbox_inches="tight")

