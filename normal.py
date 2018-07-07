#!/usr/bin/python

'''
Plot a normally distributed random variable - and samples of this process - using scipy's univariate probability distributions.
'''

from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pd

# Define parameters for normal distribution.
mu = 0
sigma = 5
rng = range(-30,30)

# Generate normal distribution with given mean and standard deviation.
dist = norm(mu, sigma)

# Plot probability density function and of this distribution.
# the pdf() method takes takes in a list x values and returns a list of y's.
plt.subplot(311) # Creates a 3 row, 1 column grid of plots, and renders the following chart in slot 1.
plt.plot(rng, dist.pdf(rng), 'r', linewidth=2)
plt.title('Probability density function of normal distribution')


# Plot probability density function and of this distribution.
plt.subplot(312)
plt.plot(rng, dist.cdf(rng))
plt.title('Cumulutative distribution function of normal distribution')

# Draw 1000 samples from the random variable.
sample = dist.rvs(size=10000)

print "Sample descriptive statistics:"
print pd.DataFrame(sample).describe()

# Plot a histogram of the samples.
plt.subplot(313)
plt.hist(sample, bins=100, normed=True)
plt.plot(rng, dist.pdf(rng), 'r--', linewidth=2)
plt.title('10,000 random samples from normal distribution')

# Show all plots.
plt.show()
