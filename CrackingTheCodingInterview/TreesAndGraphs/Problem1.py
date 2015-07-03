'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''

def is_balanced(tree):
    if tree == None:
        return 0
    else:
        left_height = is_balanced(tree.getLeftChild())
        right_height = is_balanced(tree.getRightChild())
        
        if left_height == -1:
            return -1
        
        if right_height == -1:
            return -1
        
        height_difference = left_height - right_height
        
        if abs(height_difference) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1
        

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            self.leftChild.parent = self
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            t.parent = self

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
            self.rightChild.parent = self
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            t.parent = self


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    def getParent(self):
        return self.parent
        
        
if __name__ == "__main__":
    r = BinaryTree("a")
    s = BinaryTree("b")
    t = BinaryTree("c")
    
    r.leftChild = s
    r.rightChild = t
    
    print is_balanced(r) != -1
    
    
    a = BinaryTree("a")
    b = BinaryTree("b")
    c = BinaryTree("c")
    d = BinaryTree("d")
    e = BinaryTree("e")
    
    a.leftChild = b
    a.rightChild = c
    c.rightChild = d
    d.rightChild = e
    
    print is_balanced(a) != -1


