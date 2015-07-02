'''
Created on Jul 2, 2015

@author: Debanjan Mahata
'''

"""
How to build a parse tree from a fully parenthesized mathematical expression.
How to evaluate the expression stored in a parse tree.
How to recover the original mathematical expression from a parse tree.
"""


"""Building a Parse Tree"""

"""
Rules for building a parse tree
If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
If the current token is a number, set the root value of the current node to the number and return to the parent.
If the current token is a ')', go to the parent of the current node.
"""

import operator

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
    
class Stack:
    def __init__(self):
        self.__storage = []
    
    def isEmpty(self):
        return len(self.__storage) == 0
    
    def push(self,p):
        self.__storage.append(p)
    
    def pop(self):
        return self.__storage.pop()
    
    def peek(self):
        return self.__storage[-1]



def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def postorder(tree):
    if tree == None:
        return None
    else:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print tree.getRootVal()
        


if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    postorder(pt)
    print postordereval(pt)
        


