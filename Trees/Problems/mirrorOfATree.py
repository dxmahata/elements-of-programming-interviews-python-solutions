'''
Created on Jul 2, 2015

@author: Debanjan Mahata
'''

"""
Problem Source: http://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/
"""


def mirror(tree):
    if tree == None:
        return None
    else:
        mirror(tree.getLeftChild())
        mirror(tree.getRightChild())
        temp = tree.getLeftChild()
        tree.leftChild = tree.rightChild
        tree.rightChild = temp
        
        
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
    
def preorder(tree):
    if tree == None:
        return None
    else:
        print tree.getRootVal()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

if __name__ == "__main__":

    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    
    print "Preorder traversal of the original tree"
    preorder(r)
    
    mirror(r)
    
    print "\nPreorder traversal of the mirror tree"
    preorder(r)
