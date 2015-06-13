'''
Created on Jun 13, 2015

@author: Debanjan Mahata
'''
"""
Let S be an array of strings. Write a function that finds the 
closest pair of equal entries. For example if s = ["All", "work",
"and", "no", "play", "makes", "for", "no", "work", "no", "fun",
"no","results"], then the second and third occurrences of "no"
is the closest pair.
"""

import sys

class Solution:
    
    def __init__(self):
        self.strDict = {}
        self.strList = []
        
    def set_StrList(self,strList):
        self.strList = strList
        
    def get_StrList(self):
        return self.strList
    
    def find_closest_pair_of_equal_entries(self):
        
        if not self.strList:
            return (None,-1,-1)
        else:
            tempStr = None
            tempIndex1 = -1
            tempIndex2 = -1
            minDist = sys.maxint
            index = 0
            for entries in self.strList:
                if entries in self.strDict:
                    if index - self.strDict[entries] < minDist:
                        minDist = index - self.strDict[entries]
                        tempIndex1 = self.strDict[entries]
                        tempIndex2 = index
                        tempStr = entries 
                        self.strDict[entries] = index
                else:
                    self.strDict[entries] = index
                    
                index += 1
                
            return (tempStr, tempIndex1, tempIndex2)
                    
                


if __name__ == "__main__":
    
    #list of strings
    strList1 = ["foo", "bar", "widget", "foo", "widget", "widget", "adnan"]
    strList2 = ["All", "work", "and", "no", "play", "makes", "for", "no",
                 "work", "no", "fun", "no","results"]
    
    soln = Solution()
    
    soln.set_StrList(strList1)
    print soln.find_closest_pair_of_equal_entries()
    
    soln.set_StrList(strList2)
    print soln.find_closest_pair_of_equal_entries()
    
    soln.set_StrList([])
    print soln.find_closest_pair_of_equal_entries()
    
    soln.set_StrList(["test", "test"])
    print soln.find_closest_pair_of_equal_entries()