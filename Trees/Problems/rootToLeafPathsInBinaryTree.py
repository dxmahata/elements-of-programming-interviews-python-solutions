'''
Created on Jul 2, 2015

@author: Debanjan Mahata
'''

def printPath(path, pathLen):
    return [path[i] for i in range(pathLen)]
        
    

def rootToLeafPaths(root, path, pathLen):
    if root == None:
        return 
    else:
        path[pathLen] = root.getRootVal()
        pathLen += 1
        
        if root.getLeftChild() == None and root.getRightChild() == None:
            print printPath(path, pathLen)
        else:
            rootToLeafPaths(root.getLeftChild(), path, pathLen)
            rootToLeafPaths(root.getRightChild(), path, pathLen)
            
            

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
    
    path = [0]*256
    pathLen = 0
    rootToLeafPaths(r, path, pathLen)
    
    
