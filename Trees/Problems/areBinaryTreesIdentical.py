'''
Created on Jul 2, 2015

@author: Debanjan Mahata
'''

"""
Problem Source: http://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
"""

def isIdentical(tree1, tree2):
    
    if tree1 == None and tree2 == None:
        return True
    elif tree1 == None or tree2 == None:
        return False
    else:
        if tree1 != None and tree2 != None:
            return tree1.getRootVal() == tree2.getRootVal() and isIdentical(tree1.getLeftChild(), tree2.getLeftChild()) and isIdentical(tree1.getRightChild(), tree2.getRightChild())
        
        
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
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')

    s = BinaryTree('a')
    s.insertLeft('b')
    s.insertRight('c')
    
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('d')
    
    
    print isIdentical(r,s)
    print isIdentical(r,t)
