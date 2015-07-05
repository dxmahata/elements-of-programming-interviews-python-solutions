'''
Created on Jul 5, 2015

@author: Debanjan Mahata
'''

def search(A, left, right, val):
    mid = left + (right-left) // 2
    
    if A[mid] == val:
        return mid
    
    if right < left:
        return None
    
    if A[left] < A[mid]:
        if val >= A[left] and val <= A[mid]:
            return search(A,left, mid-1, val)
        else:
            return search(A, mid+1, right, val)
    elif A[mid] < A[left]:
        if val >= A[mid] and val <= A[right]:
            return search(A, mid+1, right, val)
        else:
            return search(A,left, mid-1, val)
    elif A[mid] == A[left]:
        if A[mid] != A[right]:
            return search(A, mid+1, right, val)
        else:
            result = search(A,left, mid-1, val)
            if result == None:
                return search(A,mid+1,right,val)
            else:
                return result
    return None
                
        
        
if __name__ == "__main__":
    
    A = [15,16,19,20,25,1,3,4,5,7,10,14]
    
    index = search(A,0,len(A)-1,5)
    print index
    
    index = search(A,0,len(A)-1,16)
    print index