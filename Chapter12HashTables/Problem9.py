'''
Created on Jun 13, 2015

@author: Debanjan Mahata
'''

"""
You are required to write a method which takes an anonymous letter
L and text from a magazine M. Your method is to return true iff L can be written
using M, i.e., if a letter appears k times in L, it must appear at least k times in M
"""

class Solution:
    
    def __init__(self):
        
        #dictionary containing the characters and their count occurring in the letter
        self.letterDict = {} 
        self.magazineText = None
        self.letterText = None
        
    def set_letterText(self,lt):
        self.letterText = lt
        
    def set_magazineText(self,mt):
        self.magazineText = mt
        
        
    def is_letter_constructible_from_magazine(self):
        
        if self.letterText == None and self.magazineText != None:
            return True
        
        if self.magazineText == None:
            return False
        
        for char in self.letterText:
            if char.lower() in self.letterDict:
                self.letterDict[char.lower()] += 1
            else:
                self.letterDict[char.lower()] = 1
                
        
        for char in self.magazineText:
            if char.lower() in self.letterDict:
                self.letterDict[char.lower()] -= 1
                
        for values in self.letterDict.itervalues():
            if values > 0:
                return False
            
        return True
    
if __name__ == "__main__":
    
    soln = Solution()
    
    letter_text = "I am in love with you and can't sleep at night because I am always thinking of you."
    
    magazine_text = "Love is an eternal mystery. You can fall in love with a person, but it is not necessary that \
    the other person will also fall in love with you. If you can't sleep at night then you should try solving some \
    problems given in the book and always keep yourself away from thinking. I am sure this should work."
    
    soln.set_letterText(letter_text)
    soln.set_magazineText(magazine_text)
    
    print soln.is_letter_constructible_from_magazine()
    
    
    letter_text = "I am in love with you and can't sleep at night because I am always thinking of you."
    
    magazine_text = "hi! Molly"
    
    soln.set_letterText(letter_text)
    soln.set_magazineText(magazine_text)
    
    print soln.is_letter_constructible_from_magazine()


    
                
        