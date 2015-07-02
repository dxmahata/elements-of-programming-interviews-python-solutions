'''
Created on Jul 1, 2015

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
    
#def addition(l1,l2):
#    
#    current1 = l1.head
#    current2 = l2.head
#    
#    carry = 0
#    
#    while current1.next != None or current2.next != None:
#        sum_value = current1.data + current2.data
#        val = sum_value % 10
#        carry = 
    
if __name__ == "__main__":
    
    A = [2,3,4]
    B = [5,6,2]
    
    head1 = Node(A[0])
    head2 = Node(B[0])
    
    ln1 = LinkedList()
    ln1.head1 = head1
    
    for entries in A[1:]:
        ln1.insert_at_end(entries)

    ln2 = LinkedList()
    ln2.head2 = head2
    
    for entries in B[1:]:
        ln2.insert_at_end(entries)


