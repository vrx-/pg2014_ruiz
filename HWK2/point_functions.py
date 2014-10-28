'''
Homework 2
Problem 2
Point Class, rotation method
V.Ruiz, October 2014
'''
import numpy as np
from math import sqrt, cos, sin

class Point(object):
    """Point object (x,y)"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)
        return sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Point(%f, %f)' % (self.x, self.y)
    
    def rotate(self, Ang, p=None):
        '''
        Method: Rotates point clockwise by a specified numbers of radians 
        around another point (default=origin)
        '''
        if p is None:
            p = Point(0.0,0.0)
        self.x-=p.x
        self.y-=p.y
        xn=self.x*cos(-Ang)-self.y*sin(-Ang)
        yn=self.x*sin(-Ang)+self.y*cos(-Ang)
        self.x=xn+p.x
        self.y=yn+p.y
        return Point(self.x, self.y)
    
if __name__=='__main__':
    p=Point(0,1)
    print "rotation test: rotate (0,1) around (0,0) in 0.5*pi"
    print p.rotate(np.pi/2)
    print "rotation test: rotate (0,0) around (0,1) in 0.5*pi"
    p1=Point(0,0)
    po=Point(0,1)
    print p1.rotate(np.pi/2,po)

    