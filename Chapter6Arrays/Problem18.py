'''
Created on Jun 14, 2015

@author: Debanjan Mahata
'''

"""
Implement run-length encoding and decoding functions. Assume the string to be
encoded consists of letters of the alphabet, with no digits, and the string
to be decoded is a valid string.
"""


class Solution:
    
    def __init__(self):
        self.encoded_string = None
        self.decoded_string = None
        
    def set_encoded_string(self,es):
        self.encoded_string = es
        
    def set_decoded_string(self,ds):
        self.decoded_string = ds
        
    def get_encoded_string(self):
        return self.encoded_string
    
    def get_decoded_string(self):
        return self.decoded_string
        
    def run_length_encoding(self):
        if not self.decoded_string:
            return self.decoded_string
        else:
            encoded_str = ""
            letter_count = 1
            
            for i in range(1,len(self.decoded_string)):
                
                if self.decoded_string[i] == self.decoded_string[i-1]:
                    letter_count += 1
                else:
                    encoded_str += str(letter_count)+self.decoded_string[i-1]
                    letter_count = 1
            
            encoded_str += str(letter_count)+self.decoded_string[-1]        
            self.encoded_string = encoded_str
            
        
    
    def run_length_decoding(self):
        if not self.encoded_string:
            return self.encoded_string
        else:
            letter_count = 0
            decoded_str = ""
            
            for i in range(0, len(self.encoded_string)):
                if self.encoded_string.isdigit():
                    letter_count = letter_count * 10 + ord(self.encoded_string[i]) - ord('0')
                else:
                    for j in range(0,letter_count):
                        decoded_str += self.encoded_string[i+1]
                    letter_count = 0
                    
            self.decoded_string = decoded_str
            
    
    
if __name__ == "__main__":
    
    soln = Solution()
    
    soln.set_decoded_string("aaaabcccaa")
    soln.run_length_encoding()
    print soln.get_encoded_string()
    print soln.get_decoded_string()
    
    