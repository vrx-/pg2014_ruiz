'''
Homework 2
Problem 2
Point Class, rotation method
V.Ruiz, October 2014
'''

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
        '''Rotates point clockwise by a specified numbers of radians around another optional point (def=origin)'''
        if p is None:
            p = Point(0.0,0.0)
        self.x-=p.x
        self.y-=p.y
        xn=self.x*cos(Ang)-self.y*sin(Ang)
        yn=self.x*sin(Ang)+self.y*cos(Ang)
        self.x=xn+p.x
        self.y=yn+p.y
        return Point(self.x, self.y)