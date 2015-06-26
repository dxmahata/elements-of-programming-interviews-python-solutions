'''
Created on Jun 25, 2015

@author: Debanjan Mahata
'''


def count_sort(A):
    counter = [0]* (max(A)+1)
    for entries in A:
        counter[entries] += 1
    index = 0
    for i in range(len(counter)):
        while counter[i] > 0:
            A[index] = i
            index += 1
            counter[i] -= 1
            
    return A


if __name__ == "__main__":
    A = [0,0,0,2,3,1,2,1,3,4,5,2,4,21,2]
    print count_sort(A)
     