'''
Homework 3
Re-do Problem 2.1
V.Ruiz
'''
import numpy as np

def integrate(f,dx=1.0):
    '''
    Function to compute the integral of a list of numbers [f_n(x_n)], 
    using the trapezoidal rule with a default value of dx=1.0
    '''
    intg = 0
    for i in range(1,len(f)):
        intg=intg+(dx*(f[i]+f[i-1])/2)
    return intg

if __name__=='__main__':
    
    #test with a flat function, of value 1
    print "Test for a list of 1, length 11"
    f=np.ones(11)
    print "for dx=1."
    print integrate(f) #should be 10
    print "for dx=.5"
    print integrate(f,dx=0.5) #should be 5
    print "for dx=2."
    print integrate(f,dx=2) #should be 20
    


