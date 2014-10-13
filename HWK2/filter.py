'''
Homework 2
Problem 3
High-pass filter
V.Ruiz, October 2014
'''
import numpy as np

def remove_trend(series,N=1):
    """Filter function that removes a trend from a series of points (Nx2 array)
using a polynomial fit of order N (default: N=1)"""
    
    x, y = series[:,0], series[:,1]
    fit = np.polynomial.Polynomial.fit(x, y, N)
    ysol=fit(x)
    new= np.array(zip(x,y-ysol)) 
    return new
    