'''
Created on Jun 13, 2015

@author: Debanjan Mahata
'''

"""
Write a function that takes as input a dictionary of English words,
and returns a partition of the dictionary into subsets of words that are all anagrams
of each other.
"""


class Solution:
    
    def __init__(self):
        self.englishDictList = []
        self.anagramDict = {}
        
    def set_englishDictList(self,el):
        self.englishDictList = el
        
    def get_englishDictList(self):
        return self.englishDictList
    
    def anagram_partition(self):
        
        if not self.englishDictList:
            return []
        else:
            anagram_partition_set = []
            for entries in self.englishDictList:
                sortedEntry = sorted(entries) #O(N*lgN)
                sortedEntryString = "".join(sortedEntry)
                if sortedEntryString in self.anagramDict:
                    self.anagramDict[sortedEntryString].append(entries)
                else:
                    self.anagramDict[sortedEntryString] = [entries]
                    
            for entries in self.anagramDict.items():
                anagram_partition_set.append(entries[1])
                
            return anagram_partition_set
             
    
if __name__ == "__main__":
    
    englishDict = ["cat", "dog", "tac", "god", "act"]
    
    soln = Solution()
    
    soln.set_englishDictList(englishDict)
    print soln.anagram_partition()
    
    
    
