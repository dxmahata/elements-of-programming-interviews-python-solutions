'''
Created on Jun 13, 2015

@author: Debanjan Mahata
'''



class PriorityQueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.heapList = [0]*capacity
        
    def insert(self,key):
        self.heapList.append(key)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
        
    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def delMin(self):
        minVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return minVal
    
    def percDown(self,i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i] 
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
            
    def buildHeap(self,alist):
        i = (len(alist))//2 
        self.currentSize = len(alist)
        self.heapList = [0]+alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
            
            
if __name__ == "__main__":
    elementList = [9,5,6,2,3]
    hp = PriorityQueue(100)
    hp.buildHeap(elementList)
    print hp.heapList
    print hp.delMin()
    hp.insert(39)
    print hp.heapList
    hp.insert(1)
    print hp.heapList
    hp.insert(2)
    print hp.heapList
    hp.insert(2)
    print hp.heapList
    
    heapSortedList = []
    for i in range(len(hp.heapList)-1):
        heapSortedList.append(hp.delMin())
        
    print heapSortedList


        
            
            
