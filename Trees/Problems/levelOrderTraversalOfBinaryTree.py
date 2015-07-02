'''
Created on Jul 2, 2015

@author: Debanjan Mahata
'''

"""
Problem Source: http://www.geeksforgeeks.org/level-order-tree-traversal/
"""

import Queue

def levelOrderTraversal(root):
    if root is None:
        return 0
    q = Queue.Queue()
    q.put(root)
    node = None

    while not q.empty():
        node = q.get()  # dequeue FIFO
        print node.getRootVal()
        if node.getLeftChild() is not None:
            q.put(node.getLeftChild())

        if node.getRightChild() is not None:
            q.put(node.getRightChild())
    




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
    
    levelOrderTraversal(r)
