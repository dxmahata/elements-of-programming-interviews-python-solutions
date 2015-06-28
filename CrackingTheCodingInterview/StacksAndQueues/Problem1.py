'''
Created on Jun 28, 2015

@author: Debanjan Mahata
'''

class CombinedStack:
    
    def __init__(self):

        self.stack_size = 100
        self.buffer = [0]*3*self.stack_size
        self.stack_pointers = [0,0,0]
        
        
    def push(self,stack_num, val):
        
        if self.stack_pointers[stack_num-1] >= self.stack_size:
            return "Out of space"
        
        insert_index = self.stack_size * (stack_num-1) + self.stack_pointers[stack_num-1]
        self.stack_pointers[stack_num-1] += 1
        self.buffer[insert_index] = val
        
    def pop(self, stack_num):
        if self.stack_pointers[stack_num-1] == 0:
            return "Stack is empty"
        
        pop_index = self.stack_size * (stack_num-1) + self.stack_pointers[stack_num-1]
        pop_item = self.buffer[pop_index-1]
        self.stack_pointers[stack_num-1] -= 1
        self.buffer[pop_index-1] = 0
        return pop_item
    
    def peek(self, stack_num):
        
        peek_index = self.stack_size * (stack_num-1) + self.stack_pointers[stack_num-1]
        return self.buffer[peek_index-1]
    
    
if __name__ == "__main__":
    
    combined_stack = CombinedStack()
    
    combined_stack.push(1,1)
    combined_stack.push(1,2)
    combined_stack.push(1,3)
    
    combined_stack.push(2,101)
    combined_stack.push(2,102)
    combined_stack.push(2,103)
    
    combined_stack.push(3,201)
    combined_stack.push(3,202)
    combined_stack.push(3,203)
    
    print combined_stack.pop(1)
    print combined_stack.pop(2)
    print combined_stack.pop(3)
    
    print combined_stack.peek(1)
    print combined_stack.peek(2)
    print combined_stack.peek(3)

    
    


