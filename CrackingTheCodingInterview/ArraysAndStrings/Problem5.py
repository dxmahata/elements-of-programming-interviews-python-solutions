'''
Created on Jun 26, 2015

@author: Debanjan Mahata
'''

def compressed_string(str1):
    comp_string = ""
    count = 1
    last_char = str1[0]
    
    for iPtr in range(1, len(str1)):
        if str1[iPtr] == last_char:
            count += 1
        else:
            comp_string += last_char + str(count)
            last_char = str1[iPtr]
            count = 1
            
    comp_string += last_char + str(count)
    if len(comp_string) > len(str1):
        return "No need of compression"
    else: 
        return comp_string


if __name__ == "__main__":
    print compressed_string("aabcccccaaa")
    print compressed_string("debanjan")
    
            
