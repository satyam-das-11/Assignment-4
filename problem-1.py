# Problem-1
import numpy as np
import matplotlib.pyplot as plt

def lcg(a, c, m, seed, size):
    numbers = []
    X = seed
    for _ in range(size):
        X = (a * X + c) % m
        numbers.append(X / m)
    return numbers


a = 1664525
c = 1013904223
m = 2**32
seed = 42
size = 10000

# Generate random numbers
random_numbers = lcg(a, c, m, seed, size)

# Plot the density histogram
plt.hist(random_numbers, bins=50, density=True, alpha=0.7, color='c')

# Plot the uniform PDF for comparison
x = np.linspace(0, 1, 100)
uniform_pdf = [1] * len(x)
plt.plot(x, uniform_pdf, 'r-')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram of LCG-generated Numbers and Uniform PDF')
plt.show()
