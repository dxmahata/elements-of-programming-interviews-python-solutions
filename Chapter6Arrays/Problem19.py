'''
Created on Jun 14, 2015

@author: Debanjan Mahata
'''

"""
Implement a function for reversing the words in a string. Your function 
should use O(1) space.
"""

class Solution:
    
    def __init__(self):
        self.s = None
        
    def set_s(self,s):
        self.s = s
        
    def reverse_words_of_string(self):
        
        if not self.s:
            return self.s
        else:
            return " ".join(self.s.split()[::-1])

        
            
    
    
if __name__ == "__main__":
    
    soln = Solution()
    
    soln.set_s("I love You")
    print soln.reverse_words_of_string()