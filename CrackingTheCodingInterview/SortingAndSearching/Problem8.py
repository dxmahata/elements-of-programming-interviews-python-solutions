'''
Created on Jul 5, 2015

@author: Debanjan Mahata
'''

class TreeNode:
    def __init__(self, data):
        self.leftSize = 0
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, d):
        if d <= self.data:
            if self.left != None:
                self.left.insert(d)
            else:
                self.left = TreeNode(d)
            self.leftSize += 1
        else:
            if self.right != None:
                self.right.insert(d)
            else:
                self.right = TreeNode(d)
                
                
    def getRank(self,d):
        if d == self.data:
            return self.leftSize
        elif d < self.data:
            if self.left == None:
                return -1
            else:
                self.left.getRank(d)
        else:
            if self.right == None:
                return -1
            else:
                rightRank = self.right.getRank(d)
            
                if rightRank == -1:
                    return -1
                else:
                    return self.leftSize + 1 + rightRank


class Solution:
    def __init__(self,root):
        self.root = root
        
    def track(self, number):
        if self.root == None:
            self.root = TreeNode(number)
        else:
            self.root.insert(number)
            
    def getRankOfNumber(self, number):
        return self.root.getRank(number)
    
if __name__ == "__main__":
    
    root = TreeNode(20)
    soln = Solution(root)
    
    A = [15,25,10,23,5,13,24]
    
    for entries in A:
        soln.track(entries)
        
    print soln.getRankOfNumber(24)