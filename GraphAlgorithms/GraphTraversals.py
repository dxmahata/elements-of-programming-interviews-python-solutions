'''
Created on Jun 9, 2015

@author: Debanjan Mahata
'''
from Queue import Queue

from Graph import Graph

def BFS(G,start):
    if G == None:
        return []
    else:
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
    pass



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
    print BFS(g,g.getVertex(0))
