'''
Created on Jul 2, 2015

@author: Debanjan Mahata
'''

def lcaBinaryTree(root, n1, n2):
    if root == None:
        return None
    elif root.key == n1 or root.key == n2:
        return root
    else:
        left = lcaBinaryTree(root.getLeftChild(), n1, n2)
        right = lcaBinaryTree(root.getRightChild(), n1, n2)
        
        if left and right:
            return root
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
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    
    print lcaBinaryTree(r,"b","c").getRootVal()
