#problem-2
import numpy as np
import matplotlib.pyplot as plt

#generating random numbers---
x=[]
for i in range(10000):
    x.append(np.random.rand())
    
    
#Uniforn PDF  ------------  
def pdf(x):
    N=len(x)
    y=[1.0 for i in range(N)]
    return [x,y]

X=np.linspace(0,1,20)
#-------------------------
#plotting
plt.plot(pdf(X)[0],pdf(X)[1],label='uniform distribution')
plt.hist(x,50,density=1)
plt.legend()
plt.show()