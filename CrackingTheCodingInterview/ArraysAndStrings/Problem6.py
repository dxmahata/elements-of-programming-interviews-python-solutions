'''
Created on Jul 1, 2015

@author: Debanjan Mahata
'''

"""
for i = 0 to n:
    temp = top[i]
    top[i] = left[i]
    left[i] = bottom[i]
    bottom[i] = right[i]
    right[i] = temp
"""

def rotate_matrix_90(matrix,n):
    
    for layer in range(0,n/2):
        first = layer
        last = n-1-layer
        
        for i in range(first,last):
            
            offset = i - first
            
            temp = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = temp
            
            
            
def transpose(m,n):
    return [list(x) for x in zip(*m)]
            
            
if __name__ == "__main__":
    
    matrix = [[1,0,3,2],[0,23,12,3],[0,0,0,34],[1,2,3,4]]
    
    for i in range(len(matrix)):
        print matrix[i]
            

    rotate_matrix_90(matrix,4)
    
    print "\n"
    for i in range(len(matrix)):
        print matrix[i]
        
    matrix = [[1,0,3,2],[0,23,12,3],[0,0,0,34],[1,2,3,4]]
    m = transpose(matrix,4)
    print "\n"
    for i in range(len(m)):
        print m[i]

    
    

            
