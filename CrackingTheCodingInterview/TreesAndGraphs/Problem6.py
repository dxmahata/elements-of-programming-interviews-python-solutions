'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def __setitem__(self,k,v):
        self.put(k,v)
    
    def put(self,key,val):
        """
        Starting at the root of the tree, search the binary tree comparing the new key to the key in the current node. 
        If the new key is less than the current node, search the left subtree. 
        If the new key is greater than the current node, search the right subtree.
        When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.
        To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the previous step.
        """

        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1
    
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                   
                   
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res
            else:
                return None
        else:
            return None
    
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
        
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    
    def __getitem__(self,key):
        return self.get(key)
    
    
def get_inorder_successor(node):
    if node == None:
        return None
    elif node.parent == None or node.hasRightChild():
        return leftmostChild(node.rightChild)
    else:
        q = node
        x = node.parent
        
        while (x != None or x.leftChild != q):
            q = x
            x = x.parent
            
def leftmostChild(node):
    current = node
    while current.leftChild != None:
        current = current.leftChild
    return current


if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    
    print get_inorder_successor(mytree.get(2)).payload
    
    