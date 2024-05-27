# Problem_9
import numpy as np
import matplotlib.pyplot as plt

def metropolis_sampling(num_samples, proposal_std, initial_x):
    samples = []
    x_t = initial_x
    
    for i in range(num_samples):
        x_prime = np.random.normal(x_t, proposal_std)
        if 3 < x_prime < 7:
            acceptance_ratio = 1  # For uniform distribution within [3, 7], p(x')/p(x_t) = 1
        else:
            acceptance_ratio = 0  # Outside the interval, the density is zero
        
        # Acceptance step
        if np.random.rand() < acceptance_ratio:
            x_t = x_prime
        
        samples.append(x_t)
    
    return np.array(samples)

# Parameters
num_samples = 10000
proposal_std = 0.5
initial_x = 5

# Generate samples using Metropolis algorithm
samples = metropolis_sampling(num_samples, proposal_std, initial_x)

# Plot the Markov Chain
plt.figure(figsize=(12, 6))
plt.plot(samples, alpha=0.6)
plt.title('Markov Chain of Metropolis Algorithm')
plt.xlabel('Iteration')
plt.ylabel('Sample Value')
plt.show()

# Plot the histogram of the samples
plt.figure(figsize=(12, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='b')#, edgecolor='black')

# Plot the true uniform distribution for comparison
x = np.linspace(3, 7, 1000)
y = np.ones_like(x) / (7 - 3)
plt.plot(x, y, 'r-', lw=2, label='True Uniform Distribution')
plt.title('Density Histogram of Samples')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()