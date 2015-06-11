'''
Created on Jun 9, 2015

@author: Debanjan Mahata
'''
from Queue import Queue
import sys

from Graph import Graph

def BFS(G,start):
    if G == None:
        return []
    else:
        for vertex in G:
            vertex.setColor("white")
            vertex.setPredecessor(None)
            vertex.setDistance(sys.maxint)
            vertex.setEntryTime(0)
            vertex.setExitTime(0)

        bfsTraversal = []
        q = Queue()
        start.setDistance(0)
        start.setColor("gray")
        q.put(start)
        
        while not q.empty():
            currNode = q.get()
            bfsTraversal.append(currNode.getId())
            for node in currNode.getConnections():
                if node.getColor() == "white":
                    node.setColor("gray")
                    node.setDistance(currNode.getDistance()+1)
                    node.setPredecessor(currNode)
                    q.put(node)
            currNode.setColor("black")
        
        return bfsTraversal
                    
                
        
    

def DFS(G,start):
    if G == None:
        return []
    else:
        for vertex in G:
            vertex.setColor("white")
            vertex.setPredecessor(None)
            vertex.setDistance(sys.maxint)
            vertex.setEntryTime(0)
            vertex.setExitTime(0)
            
        dfsTraversal = []
        stack = []
        time = 0
        start.setColor("gray")
        start.setPredecessor(None)
        time += 1
        start.setEntryTime(time)
        stack.append(start)
        while stack != []:
            currNode = stack.pop()
            dfsTraversal.append(currNode.getId())
            for node in currNode.getConnections():
                if node.getColor() == "white":
                    time += 1
                    node.setColor("gray")
                    node.setPredecessor(currNode)
                    node.setEntryTime(time)
                    stack.append(node)
            currNode.setColor("black")
            time += 1
            currNode.setExitTime(time)
            
        return dfsTraversal
    
    
def DFSAlternate(G,start):
    if G == None:
        return []
    else:
        stack = [start]
        visited = set()
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(vertex.getConnections())-visited)
        return visited
    
    
    
def DFSRecursive(G, start, time, dfsTraversal):
    time += 1
    start.setEntryTime(time)
    start.setColor("gray")
    dfsTraversal.append(start.getId())
    for node in start.getConnections():
        if node.getColor() == "white":
            DFSRecursive(G,node,time,dfsTraversal)
    start.setColor("black")
    time += 1
    start.setExitTime(time)
            
            
def DFSIterativeWithRecOutput(G,start):
    if G == None:
        return []
    else:
        for vertex in G:
            vertex.setColor("white")
            vertex.setPredecessor(None)
            vertex.setDistance(sys.maxint)
            vertex.setEntryTime(0)
            vertex.setExitTime(0)
            
        dfsTraversal = []
        stack = []
        time = 0
        start.setColor("gray")
        start.setPredecessor(None)
        time += 1
        start.setEntryTime(time)
        stack.append(start)
        while stack != []:
            currNode = stack.pop()
            dfsTraversal.append(currNode.getId())
            tempStack = []
            for node in currNode.getConnections():
                if node.getColor() == "white":
                    time += 1
                    node.setColor("gray")
                    node.setPredecessor(currNode)
                    node.setEntryTime(time)
                    tempStack.append(node)
            for node in tempStack[::-1]:
                stack.append(node)
            currNode.setColor("black")
            time += 1
            currNode.setExitTime(time)
            
        return dfsTraversal

        

                
        



if __name__ == "__main__":
    g = Graph()
    
    #add random vertices to the graph
    for i in range(6):
        g.addVertex(i)
        
    
    
    #print all the newly added vertices
    for vertex in g:
        print vertex
        
        
    #add edges between the vertices
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    
    #print all the edges of the graph
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    
    #print the BFS traversal of the graph        
    print BFS(g, g.getVertex(0))
    
    #print the DFS traversal of the graph
    print DFS(g, g.getVertex(0))

    #recursive DFS
    for vertex in g:
        vertex.setColor("white")
        vertex.setPredecessor(None)
        vertex.setDistance(sys.maxint)
        vertex.setEntryTime(0)
        vertex.setExitTime(0)
     
    time = 0
    dfsTraverse = []   
    DFSRecursive(g,g.getVertex(0),time,dfsTraverse)
    print dfsTraverse
    
    print DFSIterativeWithRecOutput(g,g.getVertex(0))

    #alternate DFS
    for vertex in DFSAlternate(g,g.getVertex(0)):
        print vertex.getId()
        
