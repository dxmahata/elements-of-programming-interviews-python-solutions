'''
Created on Jul 4, 2015

@author: Debanjan Mahata
'''

def sorted_word(word):
    return "".join(sorted(word.lower()))

def sort_anagrams(A):
    hashTable = {}
    for entries in A:
        sorted_entry = sorted_word(entries)
        if sorted_entry in hashTable:
            hashTable[sorted_entry].append(entries)
        else:
            hashTable[sorted_entry] = [entries]
            
    sortedAnagramList = []
    
    for vals in hashTable.values():
        sortedAnagramList.extend(vals)
        
    return sortedAnagramList


if __name__ == "__main__":
    
    anagramList = ["mates","tablet","god","battle","care","dog","acre","meats","race","teams"]
    
    print sort_anagrams(anagramList)

