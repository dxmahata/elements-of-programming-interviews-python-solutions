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
    

if __name__ == "__main__":
    
    main_stack = Stack()
    aux_stack = Stack()
    
    for entries in [54,26,93,17,77,31,44,55,20]:
        main_stack.push(entries)
        
    aux_stack.push(main_stack.pop())
    
    while not main_stack.isEmpty():
        temp = main_stack.pop()
        while not aux_stack.isEmpty() and aux_stack.peek() < temp:
            main_stack.push(aux_stack.pop())
        aux_stack.push(temp)
        
    while not aux_stack.isEmpty():
        print aux_stack.pop()
