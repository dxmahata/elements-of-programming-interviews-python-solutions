'''
Created on Jun 25, 2015

@author: Debanjan Mahata
'''


def shell_sort(A):
    sublistcount = len(A)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            shell_sort_helper(A,startposition,sublistcount)
        
            print("After increments of size",sublistcount,"The list is",A)
        
        sublistcount = sublistcount // 2



def shell_sort_helper(A, start, gap):
    for iPtr in range(start, len(A), gap):
        jPtr = iPtr
        currentElement = A[jPtr]
        while jPtr > 0 and A[jPtr - gap] > A[jPtr]:
            A[jPtr] = A[jPtr - gap]
            jPtr -= gap
            
        A[jPtr] = currentElement
        
if __name__ == "__main__":
    A = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    shell_sort(A)
    