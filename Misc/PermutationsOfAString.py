'''
Created on Jun 14, 2015

@author: Debanjan Mahata
'''


def perm(A,k,n):
    if k == n:
        print "".join(A[0:n])
    else:
        for i in range(k,n):
            A[i],A[k] = A[k],A[i]
            perm(A,k+1,n)
            A[i],A[k] = A[k],A[i]
            

if __name__ == "__main__":
    strS = "123"
    perm(list(strS),0,len(strS))
            
