'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''

"""
calculate the number of trailing zeros in a factorial of n
"""

def countFactorsOf5(num):
    count = 0
    while num%5 == 0:
        count += 1
        num /= 5
    return count 

def countZerosInFactorial(num):
    count = 0
    for i in range(2,num+1):
        count += countFactorsOf5(i)
    return count
    
if __name__ == "__main__":
    
    print countFactorsOf5(15)
    print countZerosInFactorial(10)
        


