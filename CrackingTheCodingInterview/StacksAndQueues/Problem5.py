'''
Created on Jun 28, 2015

@author: Debanjan Mahata
'''

class Stack:
    def __init__(self):
        self.__storage = []
    
    def isEmpty(self):
        return len(self.__storage) == 0
    
    def push(self,p):
        self.__storage.append(p)
    
    def pop(self):
        return self.__storage.pop()
    
    def peek(self):
        return self.__storage[-1]

class QueueStack:
    
    def __init__(self):
        self.stackNewest = Stack()
        self.stackOldest = Stack()
        
    def size(self):
        return len(self.stackNewest) + len(self.stackOldest)
    
    def add(self, val):
        self.stackNewest.push(val)
        
    def shiftStack(self):
        if self.stackOldest.isEmpty():
            while (not self.stackNewest.isEmpty()):
                self.stackOldest.push(self.stackNewest.pop())
                
    def peek(self):
        self.shiftStack()
        return self.stackOldest.peek()
    
    def remove(self):
        self.shiftStack()
        return self.stackOldest.pop()
    
if __name__ == "__main__":
    
    qs = QueueStack()
    
    for entries in [54,26,93,17,77,31,44,55,20]:
        qs.add(entries)
        
    print qs.peek()
    print qs.remove()
    print qs.peek()

        
