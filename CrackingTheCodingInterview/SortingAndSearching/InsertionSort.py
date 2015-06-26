'''
Created on Jun 25, 2015

@author: Debanjan Mahata
'''

def insertion_sort_recursive(A, n):
    if n == 0:
        return 
    else:
        insertion_sort_recursive(A, n-1)
        iPtr = n
        while iPtr > 0 and A[iPtr-1] > A[iPtr]:
            A[iPtr], A[iPtr-1] = A[iPtr-1], A[iPtr]
            iPtr -= 1
            
            
def insertion_sort_iterative(A):
    for iPtr in range(1, len(A)):
        jPtr = iPtr
        currentElement = A[jPtr]
        while jPtr > 0 and A[jPtr-1] > A[jPtr]:
#            A[jPtr-1], A[jPtr] = A[jPtr], A[jPtr-1]
            A[jPtr] = A[jPtr-1]
            jPtr -= 1
            
        A[jPtr] = currentElement
    return A
            
            
if __name__ == "__main__":
    A = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    insertion_sort_recursive(A, len(A)-1)
    print A
    B = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print insertion_sort_iterative(B)