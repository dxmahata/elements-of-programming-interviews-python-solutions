'''
Created on Jun 26, 2015

@author: Debanjan Mahata
'''

def is_rotation(s1,s2):
    if s1 == "" and s2 == "":
        return True
    elif len(s1) != len(s2):
        return False
    else:
        if s2 in s1+s2:
            return True
        else:
            return False
        
        
if __name__ == "__main__":
    print is_rotation("waterbottle","erbottlewat")
    print is_rotation("Jyoti Sharma", "Sharma")
