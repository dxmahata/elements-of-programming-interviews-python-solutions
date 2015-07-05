'''
Created on Jul 5, 2015

@author: Debanjan Mahata
'''

def remove_empty_strings(A):
    return [s for s in A if s!= ""]

def search_removing_empty_strings(A,val):
    left = 0
    right = len(A)-1
    
    while left <= right:
        mid = left + (right-left)//2
        if A[mid] == val:
            return mid
        elif A[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
            
    return None

def search_with_empty_strings(A,val):
    
    left = 0
    right = len(A)-1
    
    while left <= right:
        
        mid = left + (right-left)//2
        
        if A[mid] == "":
            left = mid - 1
            right = mid + 1
            
            while True:
                if left < 0 and right > len(A)-1:
                    return None
                elif right <= len(A)-1 and A[right] != "":
                    mid = right
                    break
                elif left >= 0 and A[left] != "":
                    mid = left
                    break
                left -= 1
                right -= 1
                
        if A[mid] == val:
            return mid
        elif A[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
            
    return None
            
        
        

if __name__ == "__main__":
    
    A = ["at","","","","ball","","","car","","","dad","",""]
    A = remove_empty_strings(A)
    
    print search_removing_empty_strings(A,"ball")
    
    A = ["at","","","","ball","","","car","","","dad","",""]
    print search_with_empty_strings(A,"ball")
