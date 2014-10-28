'''
Homework 2
Problem 3
High-pass filter
V.Ruiz, October 2014
'''
import numpy as np
from matplotlib import pyplot as plt
def remove_trend(series,N=1):
    """Filter function that removes a trend from a series of points (Nx2 array)
using a polynomial fit of order N (default: N=1)"""
    
    x, y = series[:,0], series[:,1]
    fit = np.polynomial.Polynomial.fit(x, y, N)
    ysol=fit(x)
    return np.array(zip(x,y-ysol))

if __name__=='__main__':
    print "test for N=(1,2,3)"
    t=np.arange(100)
    f=1000*np.random.rand(100)+t**2
    x=np.asarray(zip(t,f))
    xn1=remove_trend(x)
    xn2=remove_trend(x,N=2)
    xn3=remove_trend(x,N=3)
    p0, =plt.plot(x[:,0],x[:,1], label="series")
    p1, =plt.plot(xn1[:,0],xn1[:,1], label="N1")
    p2, =plt.plot(xn2[:,0],xn2[:,1], label="N2")
    p3, =plt.plot(xn3[:,0],xn3[:,1], label="N3")
    plt.legend(handles=[p0,p1,p2,p3])
    plt.show()
    