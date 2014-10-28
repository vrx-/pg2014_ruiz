'''
Homework 2
Problem 1
Distance between points in two arrays
V.Ruiz, October 2014
'''
import numpy as np

def dist_array(a,b):
    """
    Returns distance between all intems in two arrays of points 
    array shapes should be (N, 2) and (M, 2)
    """
    xa,ya=zip(*a)
    xb,yb=zip(*b)
    MXa=np.asarray([xa]*np.size(xb)).T
    MYa=np.asarray([ya]*np.size(yb)).T
    MXb=np.asarray([xb]*np.size(xa))
    MYb=np.asarray([yb]*np.size(ya))
    Dist=np.sqrt((MXa-MXb)**2+(MYa-MYb)**2)
    return Dist
    
if __name__=='__main__':
    print "test for points in horizontal line"
    a=([([0,i]) for i in range(10)])
    b=([([0,-i]) for i in range(10)])
    print "a=", a
    print "b=", b
    print "distance between a & a"
    dist_aa=dist_array(a,a)
    print dist_aa
    print "distance between a=(x,y) & b=(x,-y)"
    dist_ab=dist_array(a,b)
    print dist_ab