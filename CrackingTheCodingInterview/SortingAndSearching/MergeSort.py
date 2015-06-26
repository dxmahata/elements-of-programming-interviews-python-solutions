'''
Created on Jun 25, 2015

@author: Debanjan Mahata
'''


def merge_sort(A):
    if len(A) > 1:
        mid = (len(A)) // 2
        
        left = A[:mid]
        right = A[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i = i + 1
            else:
                A[k] = right[j]
                j = j + 1
                
            k = k + 1
            
        
        while i < len(left):
            A[k] = left[i]
            i = i + 1
            k = k + 1
            
        while j < len(right):
            A[k] = right[j]
            j = j + 1
            k = k + 1
            
if __name__ == "__main__":
    A = [54,26,93,17,77,31,44,55,20]
    merge_sort(A)
    print A
        
        
