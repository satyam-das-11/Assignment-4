# Problem-6(gaussian using rejection method)
import numpy as np
import random as r
import matplotlib.pyplot as plt
#-----gaussian distribution
def f(x):
    return np.sqrt(2.0/np.pi)*np.exp(-x**2 /2.0)
X=np.linspace(0,10,1000)
#-----------------------------------
#Rejection method

x=[]
for i in range(100000):
    u=r.uniform(0,25)
    v=r.uniform(0,np.sqrt(2/np.pi))
    if(v<=f(u)):
        x.append(u)

#plotting---------------------------
plt.plot(X,f(X),label='Gaussian dist. x>=0')
plt.hist(x,40,density=1)
plt.legend()
plt.grid()
plt.show()