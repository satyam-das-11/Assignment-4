import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

# Load data

x = np.array([201,244,47,287,203,58,210,202,198,158,165,201,157,131,166,160,186,125,218,146])
y = np.array([592,401,583,402,495,173,479,504,510,416,393,442,317,311,400,337,423,334,533,344])
sigma = np.array([61,25,38,15,21,15,27,14,30,16,14,25,52,16,34,31,42,26,16,22])

def model(x, a, b, c):
    return a * x**2 + b * x + c

def log_likelihood(theta, x, y, sigma):
    a, b, c = theta
    model_y = model(x, a, b, c)
    return -0.5 * np.sum(((y - model_y) / sigma) ** 2)

def log_prior(theta):
    a, b, c = theta
    # Uniform priors, change the limits if needed
    if -1000.0 < a < 1000.0 and -1000.0 < b < 1000.0 and -1000.0 < c < 1000.0:
        return 0.0
    return -np.inf

def log_posterior(theta, x, y, sigma):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, sigma)


# Initial guess
initial = np.array([0.0, 0.0, 0.0])
ndim = len(initial)
nwalkers = 50
nsteps = 4000

# Initialize walkers
pos = initial + 1e-4 * np.random.randn(nwalkers, ndim)

# Run MCMC
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(x, y, sigma))
sampler.run_mcmc(pos, nsteps, progress=True)

samples = sampler.get_chain(discard=1000, thin=10, flat=True)


# Get the median and 1-sigma uncertainties
a_median, b_median, c_median = np.median(samples, axis=0)
a_std, b_std, c_std = np.std(samples, axis=0)

print(f"a = {a_median:.3f} ± {a_std:.3f}")
print(f"b = {b_median:.3f} ± {b_std:.3f}")
print(f"c = {c_median:.3f} ± {c_std:.3f}")

# Plot the chains
f1, axes = plt.subplots(3, figsize=(10, 7), sharex=True)
labels = ["a", "b", "c"]
for i in range(ndim):
    ax = axes[i]
    ax.plot(sampler.get_chain()[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(sampler.get_chain()))
    ax.set_ylabel(labels[i])
axes[-1].set_xlabel("step number")
plt.show()

f1.savefig('Figure_10(a).pdf',bbox_inches='tight')

# Plot the corner plot
f2 = corner.corner(samples, labels=labels, truths=[a_median, b_median, c_median])
plt.show()

f2.savefig('Figure_10(b).pdf',bbox_inches='tight')

# Plot the data with the best-fit model and 200 random models from the posterior
f3=plt.figure()
plt.errorbar(x, y, yerr=sigma, fmt=".k", capsize=0)
x_fit = np.linspace(min(x), max(x), 1000)
for a, b, c in samples[np.random.randint(len(samples), size=200)]:
    plt.plot(x_fit, model(x_fit, a, b, c), color="gray", alpha=0.1)
plt.plot(x_fit, model(x_fit, a_median, b_median, c_median), color="red", label="Best-fit model")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

f3.savefig('Figure_10(c).pdf',bbox_inches='tight')


