'''
Created on Jun 10, 2015

@author: Debanjan Mahata
'''

from Queue import Queue
import sys

from Graph import Graph, DirectedGraph


def has_cycle(G,start):
    """Detected if the given graph has a cycle or not.
    Traverses the graph doing depth first search, and assigns
    colors to the vertices. Initially all the vertices are 
    colored 'white'. Whenever a vertex is visited by DFS it
    is colored 'gray'. When a vertex is fully explored it is
    colored 'black'. While traversing the graph if any of the
    adjacent vertex of a vertex currently being explored is gray
    in color then it indicates that a cycle exists in the graph.
    """
    if G == None:
        return False
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
        while stack:
            currNode = stack.pop()
            dfsTraversal.append(currNode.getId())
            for node in currNode.getConnections():
                if node.getColor() == "gray":
                    return True
                if node.getColor() == "white":
                    time += 1
                    node.setColor("gray")
                    node.setPredecessor(currNode)
                    node.setEntryTime(time)
                    stack.append(node)
            currNode.setColor("black")
            time += 1
            currNode.setExitTime(time)
            
        return False
    
    
if __name__ == "__main__":
    
    #existence of a cycle in an undirected graph
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a', 'b', 1)  
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    
    print has_cycle(G,G.getVertex('a'))
    
    #existence of a cycle in a directed graph
    DG = DirectedGraph()
    DG.addVertex('a')
    DG.addVertex('b')
    DG.addVertex('c')
    DG.addVertex('d')
    DG.addVertex('e')
    DG.addEdge('a', 'b', 1)  
    DG.addEdge('b', 'c', 1)
    DG.addEdge('c', 'd', 1)
    DG.addEdge('e', 'a', 1)
    DG.addEdge('e', 'c', 1)
    
    print has_cycle(DG,DG.getVertex('a'))



