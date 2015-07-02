'''
Created on Jul 1, 2015

@author: Debanjan Mahata
'''

def set_zeros(matrix):
    
    zero_rows = [False]*len(matrix)
    zero_columns = [False]*len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_columns[j] = True
                
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if zero_rows[i] or zero_columns[j]:
                matrix[i][j] = 0
                
                
if __name__ == "__main__":
    
    matrix = [[1,0,3,2,4],[0,23,12,3,9],[0,0,0,34,21],[1,2,3,4,5]]
    
    for i in range(len(matrix)):
        print matrix[i]
            

    set_zeros(matrix)
    
    print "\n"
    for i in range(len(matrix)):
        print matrix[i]

    

                
                
                
    
    
