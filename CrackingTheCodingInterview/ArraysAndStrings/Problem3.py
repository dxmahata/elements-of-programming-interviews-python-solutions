'''
Created on Jun 26, 2015

@author: Debanjan Mahata
'''

def string_permutation_memory_efficient(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False


def string_permutation_time_efficient(str1, str2):
    if len(str1) != len(str2):
        return False
    
    letters = {}
    
    for entries in str1:
        if entries in letters:
            letters[entries] += 1
        else:
            letters[entries] = 1
        
    for entries in str2:
        if entries in letters:
            letters[entries] -= 1
            if letters[entries] < 0:
                return False
        else:
            return False
        
    return True
            
 
    


if __name__ == "__main__":
    print string_permutation_memory_efficient("god","dog")
    print string_permutation_memory_efficient("debanjan","vinay")
    
    print string_permutation_time_efficient("god", "dog")
    print string_permutation_time_efficient("debanjan", "vinay")
    
    