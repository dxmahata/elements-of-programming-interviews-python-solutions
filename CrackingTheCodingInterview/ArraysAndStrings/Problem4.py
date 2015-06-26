'''
Created on Jun 26, 2015

@author: Debanjan Mahata
'''

def replace_spaces(str1):
    
    space_count = 0
    
    for char in str1:
        if char == " ":
            space_count += 1
            
    new_length = len(str1) + 2*space_count
    str_list = [""]*new_length
    
    for i in range(len(str1)-1,-1,-1):
        if str1[i] == " ":
            str_list[new_length-1] = "0"
            str_list[new_length-2] = "2"
            str_list[new_length-3] = "%"
            new_length -= 3
        else:
            str_list[new_length-1] = str1[i]
            new_length -= 1
            
    return "".join(str_list)

if __name__ == "__main__":
    print replace_spaces("my name is debanjan mahata")
    assert replace_spaces("my name is debanjan mahata") == "my name is debanjan mahata".replace(" ","%20")