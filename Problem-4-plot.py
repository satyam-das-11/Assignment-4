#Problem-4
import numpy as np
import matplotlib.pyplot as plt

with open('problem-4-output_from_C.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Convert the lines to floating-point numbers and store them in a list
numbers = [float(line.strip()) for line in lines]

# Print the list of numbers
def f(x):
    return 0.5*np.exp(-0.5*x)
xt=np.linspace(0,50,1000)
x=numbers
plt.plot(xt,f(xt),label='The actual function')
plt.hist(x,50,density=True,label='Generated random numbers')
plt.xlim(0,20)
plt.legend()
plt.grid()
plt.show()