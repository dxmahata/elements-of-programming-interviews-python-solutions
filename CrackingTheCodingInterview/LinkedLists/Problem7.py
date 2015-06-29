'''
Created on Jun 28, 2015

@author: Debanjan Mahata
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.current_len = 0
        
    def is_empty(self):
        return self.head == None
    
    def __len__(self):
        return self.current_len
    
    def insert_at_front(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.current_len += 1
        
    def search(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.data == item:
                return (current, previous)
            previous = current
            current = current.next
        return (current, previous)
    
    def insert_at_end(self,item):
        
        current = self.head
        while current.next != None:
            current = current.next
            
        new_node = Node(item)
        current.next = new_node
        self.current_len += 1
        
    def delete(self, item):
        
        ptr = self.search(item)
        print ptr
        if ptr[0] == None:
            return "Item for deletion not found in the list"
        else:
            if ptr[1] == None:
                self.head = self.head.next
            else:
                ptr[1].next = ptr[0].next      
        
    def print_list(self):
        current = self.head
        link_list = []
        while current != None:
            link_list.append(current.data)
            current = current.next
        return link_list
    
    def is_palindrome(self):
        current = self.head
        runner = self.head
        
        stack = []
        
        while runner != None and runner.next != None:
            stack.append(current.data)
            current = current.next
            runner = runner.next 
            
        if runner != None:
            current = current.next
            
        while current != None:
            if current.data == stack.pop():
                current = current.next
            else:
                return False
            
        return True


if __name__ == "__main__":
    
    A = ["m","a","d","a","m"]
    
    head = Node(1)
    
    ln = LinkedList()
    ln.head = head
    
    for entries in A:
        ln.insert_at_end(entries)
        
    print ln.is_palindrome()
