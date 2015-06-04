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
    
    
if __name__ == "__main__":
    A = [4,1,6,2,29,36,100,-34]
    arrangedA = dutchNationalFlag(A,4)
    print arrangedA
    
    A = [0,1,1,0,1,2,1,2,0,0,0,1]
    arrangedA = dutchNationalFlag2(A)
    print arrangedA
