'''
Created on Jun 14, 2015

@author: Debanjan Mahata
'''

"""
Implement string/integer inter-conversion functions.
"""

class Solution:
    
    def __init__(self):
        self.integer_input = None
        self.string_input = None
        
    def set_integer_input(self,i):
        self.integer_input = i
        
    def set_string_input(self,s):
        self.string_input = s
        
    def int_to_string(self):
        if self.integer_input == None:
            return None
        else:
            if self.integer_input == 0:
                return '0'

            stringRep = ""
            integer_input = abs(self.integer_input)
            
            while integer_input:
                stringRep += chr(ord('0') + integer_input % 10)
                integer_input = integer_input/10
                
            
            if self.integer_input < 0:
                return "-"+stringRep[::-1]
            else:
                return stringRep[::-1]            
    
    def string_to_int(self):
        if self.string_input == None:
            return None
        else:
            integerRep = 0
            is_negative = False
            if self.string_input[0] == '-':
                is_negative = True
                for i in range(1,len(self.string_input)):
                    integerRep = integerRep * 10 + ord(self.string_input[i]) - ord('0')
            else:
                for i in range(0,len(self.string_input)):
                    integerRep = integerRep * 10 + ord(self.string_input[i]) - ord('0')
                    
            if is_negative:
                return -integerRep
            else:
                return integerRep

                
if __name__ == "__main__":
    
    soln = Solution()
    
    soln.set_string_input("123")
    print soln.string_to_int()

    soln.set_string_input("-123")
    print soln.string_to_int()
    
    soln.set_integer_input(123)
    print soln.int_to_string()
    
    soln.set_integer_input(-123)
    print soln.int_to_string()