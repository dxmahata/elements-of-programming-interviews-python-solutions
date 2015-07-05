'''
Created on Jul 5, 2015

@author: Debanjan Mahata
'''

def find_element(matrix, element):
    row = 0
    col = len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == element:
            return True
        elif matrix[row][col] > element:
            col -= 1
        else:
            row += 1
    return False


if __name__ == "__main__":
    
    matrix = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
    print find_element(matrix, 55)
    print find_element(matrix, 20)
    print find_element(matrix, 110)