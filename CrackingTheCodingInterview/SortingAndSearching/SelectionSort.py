'''
Created on Jun 25, 2015

@author: Debanjan Mahata
'''

def selection_sort_iterative(A):
    
    for passes in range(len(A)-1, 0, -1):
        maxPosition = passes
        for iPtr in range(passes):
            if A[iPtr] > A[maxPosition]:
                maxPosition = iPtr
                
        A[maxPosition], A[passes] = A[passes], A[maxPosition]
        
    return A


def selection_sort_recursive(A, n):
    
    if n == 0:
        return
    else:
        maxPosition = n
        for iPtr in range(n):
            if A[iPtr] > A[maxPosition]:
                maxPosition = iPtr
        A[maxPosition], A[n] = A[n], A[maxPosition]
        selection_sort_recursive(A, n-1)
    
    

if __name__ == "__main__":
    A = [54,26,93,17,77,31,44,55,20]
    print selection_sort_iterative(A)
    B = [54,26,93,17,77,31,44,55,20]
    selection_sort_recursive(B, len(B)-1)
    print B
    
        