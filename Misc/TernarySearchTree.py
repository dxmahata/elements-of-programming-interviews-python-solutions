'''
Created on Jun 16, 2015

@author: Debanjan Mahata
'''

class TernarySearchTreeNode:
    def __init__(self):
        self.data = None
        self.isEndOfString = False
        self.equal = None
        self.left = None
        self.right = None
        
        
        
        
class TernarySearchTree:
    def __init__(self):
        self.root = TernarySearchTreeNode()
        
    def add_node(self, c):
        child_node = TernarySearchTreeNode()
        child_node.data = c

        
        
    def insert(self, key):
        
        current = self.root
        
        for char in key:
            if current.data == None:
                current.data = char
            else:
                if char < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = self.add_node(char)
                else:
                    if char > current.data:
                        if current.right:
                            current = current.right
                        else:
                            current.right = self.add_node(char)
                    else:
                        if char == current.data:
                            if current.equal:
                                current = current.equal
                            else:
                                current.equal = self.add_node(char)
        
        current.isEndOfString = True
                                
                                
    def search(self,key):
        
        current = self.root
        
        len_key = len(key)
        key_index = 0
        
        while key_index < len_key:
            if current.data == key[key_index]:
                if current.equal:
                    current = current.equal
                                
                                
                                
if __name__ == "__main__":
    
    ternary_search_tree = TernarySearchTree()
    
    wordList = ["there", "their", "answer", "any", "bye", "and", "an"]
    
    for entries in wordList:
        ternary_search_tree.insert(entries)
        
        
                    
                
            
            
