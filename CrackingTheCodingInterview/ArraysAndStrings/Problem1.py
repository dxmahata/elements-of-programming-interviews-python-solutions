'''
Created on Jun 26, 2015

@author: Debanjan  Mahata
'''

def has_unique_characters_space_inefficient(str1):
    """method using additional data structure"""
    if len(str1) == "":
        return True
    elif len(str1) == len(set(str1)):
        return True
    else:
        return False
    
def has_unique_characters_space_efficient(str1):
    """method without using additional space
    Space Efficiency O(1)
    Time Efficiency O(N^2)"""
    for char in str1:
        if str1.count(char) > 1:
            return False
    return True

def has_unique_characters_space_efficient_time_efficient(str1):
    """method without using additional space
    Space Efficiency O(1)
    Time Efficiency O(NlgN)"""
    
    str1 = str1.replace(" ","")
    sorted_string = sorted(str1)
    
    for i in range(len(sorted_string)-1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True
    
    
    
if __name__ == "__main__":
    string1 = "madam"
    string2 = "amit"
    
    print has_unique_characters_space_inefficient(string1)
    print has_unique_characters_space_inefficient(string2)
    
    print has_unique_characters_space_efficient(string1)
    print has_unique_characters_space_efficient(string2)
    
    print has_unique_characters_space_efficient_time_efficient(string1)
    print has_unique_characters_space_efficient_time_efficient(string2)
    
    
    