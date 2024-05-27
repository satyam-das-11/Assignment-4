#problem-5
import numpy as np
import random as r
import matplotlib.pyplot as plt
#-----gaussian distribution
def f(x):
    return np.sqrt(0.5/np.pi)*np.exp(-x**2 /2.0)
X=np.linspace(-10,10,1000)
#--------------------------
#Box-Muller
g=[]
for i in range(10000):
    phi=r.uniform(0,2*np.pi)
    Y=-np.log(r.uniform(0,1))
    R=np.sqrt(2*Y)
    x=R*np.cos(phi)
    g.append(x)
plt.plot(X,f(X),label='Gaussian Dist.')
plt.hist(g,40,density=1)
plt.legend()
plt.grid()
plt.show()


