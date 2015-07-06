'''
Created on Jul 5, 2015

@author: Debanjan Mahata
'''


import sys

def max1(x,y):
    return x ^ ((x^y) & -(x < y))

def max2(x,y):
    return x - ((x - y) & ((x - y) >> sys.getsizeof(1)-1))

def min1(x,y):
    return y ^ ((x^y) & -(x < y))

def min2(x,y):
    return y + ((x - y) & ((x - y) >> sys.getsizeof(1)-1))


if __name__ == "__main__":
    
    print max1(5,6)
    print min1(5,6)
    print max1(5,-6)
    print min1(-5,6)
    
    print max2(5,6)
    print min2(5,6)
    print max2(5,-6)
    print min2(-5,6)



