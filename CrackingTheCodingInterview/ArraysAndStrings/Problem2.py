'''
Created on Jun 26, 2015

@author: Debanjan Mahata
'''

def reverse_string(str1):
    str_list = list(str1)
    iPtr = 0
    jPtr = len(str_list)-1
    while iPtr <= jPtr:
        str_list[iPtr], str_list[jPtr] = str_list[jPtr], str_list[iPtr]
        iPtr += 1
        jPtr -= 1
    return "".join(str_list)


if __name__ == "__main__":
    print reverse_string("my name is debanjan")
    print reverse_string("madam I am your only adam")
