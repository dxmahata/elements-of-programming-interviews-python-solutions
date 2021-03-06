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
    
    
    def remove_duplicates(self):
        previous = None
        current = self.head
        hashTable = {}
        
        while current != None:
            current_data = current.data
            if current_data in hashTable:
                previous.next = current.next
            else:
                hashTable[current_data] = True
                previous = current
                
            current = current.next
                
        
        
    
    
if __name__ == "__main__":
    
    A = [0,0,0,2,3,1,2,1,3,4,5,2,4,21,2]
    
    head = Node(1)
    
    ln = LinkedList()
    ln.head = head
    
    for entries in A:
        ln.insert_at_end(entries)
        
    print ln.print_list()
    
    ln.remove_duplicates()
    
    print ln.print_list()

