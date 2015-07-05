'''
Created on Jul 4, 2015

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
    
    
def merge_sort(head):
    if head == None or head.next == None:
        return head
    
    else:
    
        middle = getmiddle(head)
#        print middle.data
        firstHalf = head
        secondHalf = middle.next
        middle.next = None
        
#        merge_sort(firstHalf)
#        merge_sort(secondHalf)
        
        return merge(merge_sort(firstHalf),merge_sort(secondHalf))
        
        
    
        
def getmiddle(head):
    if head == None or head.next == None:
        return head
    
    else:
    
        ptr1 = head
        ptr2 = head
        
        iCounter = 0
        
        while ptr1.next != None:
            if iCounter == 0:
                ptr1 = ptr1.next
                iCounter = 1
            elif iCounter == 1:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                iCounter = 0
                
        return ptr2
        
        
def merge(a,b):
    if a == None:
        return b
    if b == None:
        return a
    else:
        if a.data < b.data:
            result = a
            result.next = merge(a.next,b)
        else:
            result = b 
            result.next = merge(a, b.next)
        return result

if __name__ == "__main__":
    
    A = [12,1,0,-1,24,32,2,22]
    
    head = Node(23)
    
    ln = LinkedList()
    ln.head = head
    
    for entries in A:
        ln.insert_at_end(entries)
        
    print ln.print_list()
    
    ref = merge_sort(ln.head)
    
    current = ref
    while current!= None:
        print current.data
        current = current.next
