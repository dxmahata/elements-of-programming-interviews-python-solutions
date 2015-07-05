'''
Created on Jul 5, 2015

@author: Debanjan Mahata
'''

def find(A,K):
    
    if not A:
        return None
    elif len(A) == 1:
        return None
    else:
        start = 0
        end  = len(A)-1
        integerPairs = []
        while start <= end:
            tempSum = A[start] + A[end]
            if tempSum == K:
                integerPairs.append((A[start],A[end]))
            elif tempSum < K:
                start += 1
            else:
                end -= 1
            
            start += 1
            end -= 1
                
        return integerPairs

if __name__ == "__main__":
    
    A = [3,1,-2,6,32,-28]
    A.sort()
    print A
    print find(A,4)
    
