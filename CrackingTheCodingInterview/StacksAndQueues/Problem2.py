'''
Created on Jun 28, 2015

@author: Debanjan Mahata
'''

import sys 

class MinStack:
    
    def __init__(self):
        self.min_value = sys.maxint
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        if val < self.min_value:
            self.min_value = val
            self.min_stack.append(val)
            
        self.stack.append(val)
        
        
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"

        pop_item = self.stack.pop()
        if pop_item == self.min_stack[-1]:
            self.min_stack.pop()
        return pop_item
    
    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        
        peek_item = self.stack[-1]
        return peek_item
    
    def get_min_value(self):
        if not self.min_stack:
            return "Min Stack is Empty"
        
        return self.min_stack[-1]
    
    
if __name__ == "__main__":
    
    stck = MinStack()
    
    for entries in [54,26,93,17,77,31,44,55,20]:
        stck.push(entries)
        
        
    print stck.get_min_value()
    
    print stck.pop()
    print stck.pop()
    print stck.pop()
    print stck.pop()
    print stck.pop()
    print stck.pop()
    
    print stck.peek()
    print stck.get_min_value()
    

        
        
