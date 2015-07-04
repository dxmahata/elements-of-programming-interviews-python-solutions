'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''
def is_BST(root):
    if root == None:
        return True
    else:
        prev = None
        if not is_BST(root.leftChild):
            return False
        
        if prev != None and prev.key >= root.key:
            return False
        
        prev = root
        
        return is_BST(root.rightChild)

def create_minimal_BST(A, start, end):
    if end < start:
        return None
    else:
        mid = start + (end - start)//2
        n = BinaryTree(A[mid])
        n.leftChild = create_minimal_BST(A, start, mid-1)
        n.rightChild = create_minimal_BST(A, mid+1, end)
        return n


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
    
    A = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    
    bst = create_minimal_BST(A,0,len(A)-1)
    
    print is_BST(bst)