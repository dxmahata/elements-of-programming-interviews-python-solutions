'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''

"""
swap two elements without using temporary variable
"""

def swap1(a,b):
    a = a - b 
    b = a + b 
    a = b - a
    
    return a,b 
    
def swap2(a,b):
    a = a ^ b
    b = a ^ b 
    a = a ^ b
    return a, b
    
    
if __name__ == "__main__":
    
    a = 20
    b = 10000
    
    print swap1(a,b)
    
    
    print swap2(a,b)
    
