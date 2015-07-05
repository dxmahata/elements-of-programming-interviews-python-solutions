'''
Created on Jul 4, 2015

@author: Debanjan Mahata
'''


def merge_sorted_arrays(A,B):
    
    indexA = 0
    for entries in A:
        if entries > 0:
            indexA += 1
    indexA = indexA - 1
    indexB = len(B)- 1
    indexMerged = len(A) - 1

    while indexA >= 0 and indexB >= 0:
        if A[indexA] > B[indexB]:
            A[indexMerged] = A[indexA]
            indexA -= 1
            indexMerged -= 1
        else:
            A[indexMerged] = B[indexB]
            indexB -= 1
            indexMerged -= 1
            
    while indexB >= 0:
        A[indexMerged] = B[indexB]
        indexMerged -= 1
        indexB -= 1
        
    
if __name__ == "__main__":
    A = [17,20,26,31,44,0,0,0,0]
    B = [54,55,77,93]
    
    merge_sorted_arrays(A,B)
    
    print A
    
    A = [17,26,31,54,0,0,0,0]
    B = [20,44,55,77,93]
    
    merge_sorted_arrays(A,B)
    
    print A

    

    
