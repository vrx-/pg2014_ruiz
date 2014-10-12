'''
Homework 2
Problem 1
Distance between arays of points
V.Ruiz, October 2014
'''
import numpy as np

def dist_array(a,b):
    """Returns distance between all intems in two arrays of points (with shapes (N, 2) and (M, 2))"""
    xa,ya=zip(*a)
    xb,yb=zip(*b)
    MXa=np.asarray([xa]*np.size(xb)).T
    MYa=np.asarray([ya]*np.size(yb)).T
    MXb=np.asarray([xb]*np.size(xa))
    MYb=np.asarray([yb]*np.size(ya))
    Dist=np.sqrt((MXa-MXb)**2+(MYa-MYb)**2)
    return Dist