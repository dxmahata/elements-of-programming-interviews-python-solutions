'''
Created on Jun 13, 2015

@author: Debanjan Mahata
'''

"""
Write a program to test whether the letters forming a string s
can be permuted to form a palindrome, For example, 'edified' can
be permuted to form 'deified'. Explore solution that trade time 
for space.
"""

class Solution:
    
    def __init__(self,s):
        self.s = s
        self.strDict = {}
        

    def hash_impl_palindrome_formation(self):
        """O(N) space complexity, O(N) Time complexity"""
        
        if not self.s:
            return True
        else: 
            is_odd_len = False
            
            for entries in self.s:
                if entries in self.strDict:
                    self.strDict[entries] += 1
                else:
                    self.strDict[entries] = 1
                    
            if len(self.s) % 2 != 0:
                is_odd_len = True
                
            no_of_odd_entries = 0
            
            for entries in self.strDict.itervalues():
                if entries % 2 != 0:
                    no_of_odd_entries += 1
                    
            if is_odd_len == True and no_of_odd_entries == 1:
                return True
            elif is_odd_len == False and no_of_odd_entries == 0:
                return True
            else:
                return False
        
    
    def sort_impl_palindrom_formation(self):
        """O(NlgN) time complexity, O(1) space complexity"""
        
        if not self.s:
            return True
        else:
            is_odd_len = False
            no_of_odd_entries = 0
            
            sortedString = sorted(self.s)
            
            counter = 0
            
            while counter < len(sortedString)-1:
                if sortedString[counter] == sortedString[counter + 1]:
                    counter += 2
                else:
                    counter += 1
                    no_of_odd_entries += 1
                    
            if counter % 2 != 0:
                is_odd_len = True
    
            if is_odd_len == True and no_of_odd_entries == 1:
                return True
            elif is_odd_len == False and no_of_odd_entries == 0:
                return True
            else:
                return False
            
            

            
if __name__ == "__main__":
    
    soln1 = Solution("madam")
    print soln1.hash_impl_palindrome_formation()
    print soln1.sort_impl_palindrom_formation()
    
    
    soln2 = Solution("edified")
    print soln2.hash_impl_palindrome_formation()
    print soln2.sort_impl_palindrom_formation()

    
    
    
    
    
            
            
