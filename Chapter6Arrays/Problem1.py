'''
Created on Jun 4, 2015

@author: Debanjan Mahata
'''

"""
Q. Write a function that takes an array A of length n and an index i into
A, and rearranges the elements such that all elements less than A[i] appear first,
followed by elements equal to A[i], followed by elements greater than A[i]. Your
algorithm should have O(1) space complexity and O(n) time complexity
"""



def dutchNationalFlag(A, piv):
    assert 0 <= piv <= len(A)-1
    if len(A) == 0:
        return A
    else:
        low = 0
        mid = 0
        high = len(A)-1
        pivot = piv
        
        while mid <= high:
            if A[mid] < A[pivot]:
                A[mid], A[low] = A[low], A[mid]
                low += 1
                mid += 1
            elif A[mid] == A[pivot]:
                mid += 1
            elif A[mid] > A[pivot]:
                A[mid], A[high] = A[high], A[mid]
                high -= 1
                
                
        return A


    
    
########################################################################
#Different variations of the problem#
########################################################################

"""
Q. Given an array A of 0s 1s and 2s, give an algorithm for sorting A. The algorithm
should put all 0s first then all 1s and finally all 2s.
Input = [0,1,1,0,1,2,1,2,0,0,0,1]
Output = [0,0,0,0,0,1,1,1,1,1,2,2]
"""

def dutchNationalFlag2(A):
    
    if len(A) == 0:
        return A
    else:
        
        for elements in A:
            assert elements in [0,1,2]
        
        low = 0
        mid = 0
        high = len(A)-1
        
        while mid <= high:
            if A[mid] == 1:
                mid += 1
            elif A[mid] == 0:
                A[mid], A[low] = A[low], A[mid]
                low += 1
                mid += 1
            elif A[mid] == 2:
                A[mid], A[high] = A[high], A[mid]
                high -= 1
        return A
    
"""
Separate 0s and 1s in an array: We are given an array of 0s and 1s in random order. Separate 0s on
left side and 1s on right side of the array. Traverse array only once.
Input = [0,1,0,1,0,0,1,1,1,0]
Output = [0,0,0,0,0,1,1,1,1,1]
"""

def dutchNationalFlag3(A):
    if len(A) == 0:
        return A
    else:
        for elements in A:
            assert elements in [0,1]
        low = 0
        high = len(A)-1
        while low < high:
            if A[low] == 0 and low < high:
                low += 1
                
            if A[high] == 1 and low < high:
                high -= 1
                
            if low < high:
                A[low], A[high] = A[high], A[low]
                
        return A
        



"""
Separate Even and Odd numbers: Given an array A, write a function that segregates even and odd
numbers. The functions should put all even numbers first and then odd numbers.
Example
Input = [12,34,45,9,8,90,3]
Output = [12,34,90,8,9,45,3]
"""
def dutchNationalFlag4(A):
    if len(A) == 0:
        return A
    else:
        low = 0
        high = len(A)-1
        
        for elements in A:
            assert type(elements) == type(1) or type(elements) == type(1.0)
        
        while (low < high):
            if A[low]%2 == 0 and low < high:
                low += 1
            if A[high]%2 == 1 and low < high:
                high -= 1
                
            if low < high:
                A[low], A[high] = A[high], A[low]
                
        return A
                

    
if __name__ == "__main__":
    A = [4,1,6,2,29,36,100,-34]
    arrangedA = dutchNationalFlag(A,4)
    print arrangedA
    
    A = [0,1,1,0,1,2,1,2,0,0,0,1]
    arrangedA = dutchNationalFlag2(A)
    print arrangedA
    
    A = [0,1,0,1,0,0,1,1,1,0]
    arrangedA = dutchNationalFlag3(A)
    print arrangedA
    
    A = [12,34,45,9,8,90,3]
    arrangedA = dutchNationalFlag4(A)
    print arrangedA
