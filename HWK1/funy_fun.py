'''
Homework 1
Problem 1 and 2
V.Ruiz
'''

#Function to return a list of n fibonacci numbers
#Input : n  Output: Fib(n)

def fib(n):
    if n<2:
        fib_s=[n]
    else:
        fib_s=[1,1]
        for i in range(2,n):
            fib_s.append(fib_s[i-1]+fib_s[i-2])
    return fib_s


#Function to compute the integral of a list of numbers [f_n(x_n)], using the trapezoidal rule with a default value of dx=1.0

def integrate(f,dx=1.0):
    intg = 0
    for i in range(1,len(f)):
        intg=intg+(dx*(f[i]+f[i-1])/2)
    return intg


