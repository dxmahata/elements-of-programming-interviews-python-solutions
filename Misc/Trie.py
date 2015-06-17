'''
Created on Jun 16, 2015

@author: Debanjan Mahata
'''

class TrieNode():
    def __init__(self):
        self.key = None
        self.value = "not terminal"
        self.children = {}
        
    def set_value(self,val):
        self.value = val
        
    def get_value(self):
        return self.value
    
    def set_key(self,key):
        self.key = key
        
    def get_key(self):
        return self.key

    
    def add_child(self, key):
        if key in self.children:
            return
        else:
            new_child = TrieNode()
            new_child.set_key(key)
            self.children[key] = new_child
            

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0
        
    def insert(self, key):
        
        current = self.root
        
        for char in key:
            current.add_child(char)
            current = current.children[char]
            
        current.set_value("terminal")
        self.count += 1
    
    def search(self, key):
        
        current = self.root
        key_len = len(key)
        key_index = 0
        while current.get_value() != "not terminal" and key_index < key_len:
            if key[key_index] in current.children:
                current = current.children[key[key_index]]
                key_index += 1
            else:
                return False
        
        if current.get_value() == "terminal":
            return True
        else:
            return "word not present needs to be inserted"
        
        
    def is_prefix(self, prefix):
        
        current = self.root
        prefix_len = len(prefix)
        prefix_index = 0
        while current.get_value() != "not terminal" and prefix_index < prefix_len:
            if prefix[prefix_index] in current.children:
                current = current.children[prefix[prefix_index]]
                prefix_index += 1
            else:
                return False
        
        return True
    
    def dfs(self,start):
        stack = [start]
        visited = []
        suffixes = []
        tempStr = ""
        while stack:
            currNode =  stack.pop()
            if currNode == start:
                pass
            else:
                tempStr += currNode.get_key()
            if currNode.get_value() == "terminal" and currNode.children == {}:
                suffixes.append(tempStr)
                tempStr = ""
                
            for node in currNode.children.itervalues():
                if node not in visited:
                    stack.append(node)
                    
        return suffixes
    
    
    def auto_complete(self, prefix):
        
        current = self.root
        for char in prefix:
            current = current.children[char]
            
          
        suffixes = self.dfs(current)
        return [prefix+suffix for suffix in suffixes]
    
        
    
if __name__ == "__main__":
    
    trie = Trie()
    
    wordList = ["there", "their", "answer", "any", "bye", "and", "an"]
    
    for entries in wordList:
        trie.insert(entries)
        
    print trie.search("the")
    print trie.is_prefix("the")
    print trie.auto_complete("the")
    print trie.auto_complete("an")
    
            
            
            
        
        
