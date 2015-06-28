'''
Created on Jun 26, 2015

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
            
            

        
        
    def traverse(self):
        current = self.head
        link_list = []
        while current != None:
            link_list.append(current.data)
            current = current.next
        return link_list
            
            
if __name__ == "__main__":
    
    head = Node("Jyoti")
    
    ln = LinkedList()
    ln.head = head
    
    ln.insert_at_end("Debanjan")
    ln.insert_at_end("Anil")
    ln.insert_at_end("Mamata")
    ln.insert_at_end("Bhola")
    
    print ln.traverse()
    
    print ln.search("Mamata")
    
    ln.delete("Anil")
    ln.delete("macchar")
    ln.delete("Bhola")
    ln.delete("Jyoti")
    ln.insert_at_front("Chunki")
    
    print ln.traverse()
    
