# Basic example of one-dimensional parameter estimation using
# a grid of possibilities.

import matplotlib.pyplot as plt
import numpy as np

# Grid of possible lambdas
lambdas = np.linspace(1.0, 20.0, 10001)

# A log-uniform prior, perhaps?
prior = 1.0 / lambdas
prior /= np.trapz(prior, x=lambdas)

# Data
xs = np.array([5, 3, 5, 6, 2, 6, 0, 4])
N = len(xs)

# Log likelihood (up to an additive constant)
log_lik = np.sum(xs)*np.log(lambdas) - N*lambdas

# Likelihood (up to a multiplicative constant)
lik = np.exp(log_lik - log_lik.max())

# Posterior - unnormalised then normalised
h = prior*lik
Z = np.trapz(h, x=lambdas)
post = h/Z

# Calculate and print some summaries
post_mean = np.trapz(lambdas*post, x=lambdas)
post_var = np.trapz((lambdas - post_mean)**2 * post, x=lambdas)
post_sd = np.sqrt(post_var)
print("lambda = {m} +- {s}".format(m=post_mean, s=post_sd))

# Calculate and print the posterior probability of a statement
p = np.trapz(post*(lambdas > 5.0), x=lambdas)
print("P(lambda > 5 | data) = {p}".format(p=p))

# Plot the prior, likelihood, and posterior
plt.plot(lambdas, prior, label="Prior")
plt.plot(lambdas, lik, label="Likelihood", alpha=0.2, linestyle="--")
plt.plot(lambdas, post, label="Posterior")
plt.xlabel("$\\lambda$")
plt.ylabel("Probability Density")
plt.legend()
plt.show()

