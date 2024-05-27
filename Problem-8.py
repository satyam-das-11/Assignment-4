# Problem-8
import numpy as np
import random as r
import matplotlib.pyplot as plt

#defining the given function-------------
def f(x,y):
    if(x**2+y**2<=1):
        return 1
    else:
        return 0

n=0.0
N=0.0
for i in range(10000):
    u=r.uniform(-1,1)
    v=r.uniform(-1,1)
    if(f(u,v)==1):
        n=n+1
    N+=1
Area= (n/N)*4      
print("Area of the circle :",Area) 
#============================================
#Volume of a 10 dimensional sphere
d=10 # d dimensional sphere
def f(X):
    R=np.dot(X,X)
    if(R<=1):
        return 1
    else:
        return 0
n_10=0.0 
N_10=0.0 
for i in range(100000):
    X=[r.uniform(-1,1) for i in range(d)]
    Ra=np.dot(X,X)
    if(Ra<=1):
        n_10+=1
    N_10+=1

Volume_10=(n_10/N_10)*(2**d)
print("Volume of the 10 dimensional sphere : ",Volume_10)