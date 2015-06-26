'''
Created on Jun 25, 2015

@author: Debanjan Mahata
'''


def partition(A, start, end):
    pivot_point = start
    pivot_value = A[pivot_point]
    left = start+1
    right = end
    
    done = False
    
    while not done:
        
        while left <= right and A[left] <= pivot_value:
            left = left + 1
            
        while left <=right and A[right] > pivot_value:
            right = right - 1
            
        if right < left:
            done = True
        else:
            A[left], A[right] = A[right], A[left]
            
    A[pivot_point], A[right] = A[right], A[pivot_point] 
    return right
    
    
def quick_sort(A, start, end):
    
    if start < end:
        split_point = partition(A, start, end)
        quick_sort(A, start, split_point-1)
        quick_sort(A, split_point + 1, end)
        
        
if __name__ == "__main__":
    A = [54,26,93,17,77,31,44,55,20]
    quick_sort(A,0, len(A)-1)
    print A
