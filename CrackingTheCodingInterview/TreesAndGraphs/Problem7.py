'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''


def first_common_ancestor(node, node1, node2):
    if node == None:
        return None
    elif node == node1 or node == node2:
        return node
    else:
        left = first_common_ancestor(node.getLeftChild(), node1, node2)
        right = first_common_ancestor(node.getRightChild(), node1, node2)
        
        if left and right:
            return node
        else:
            if left:
                return left
            else:
                return right
            
            
            
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
    
    print first_common_ancestor(r,s,t).key
    
    
    a = BinaryTree("a")
    b = BinaryTree("b")
    c = BinaryTree("c")
    d = BinaryTree("d")
    e = BinaryTree("e")
    
    a.leftChild = b
    a.rightChild = c
    c.rightChild = d
    d.rightChild = e
    
    print first_common_ancestor(a,d,e).key
    print first_common_ancestor(a,b,e).key
    
