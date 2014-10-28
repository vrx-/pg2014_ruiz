'''
Homework 3
Re-do Problem 1.1
V.Ruiz
'''

def fib(n):
    '''
    Function to return a list of n fibonacci numbers
    Input : n  Output: Fib(n)
    '''
    if n<2:
        fib_s=[n]
    else:
        fib_s=[1,1]
        for i in range(2,n):
            fib_s.append(fib_s[i-1]+fib_s[i-2])
    return fib_s
    
if __name__=='__main__':
    
    #test for n=1-10
    for n in range(10):
        print "fib series for", n+1, fib(n) 

