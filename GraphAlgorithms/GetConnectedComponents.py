'''
Created on Jun 9, 2015

@author: Debanjan Mahata
'''

"""
Getting connected components using Breadth First Search
"""

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

def connected_components_with_bfs(G):
    connectedComponents = []
    for vertex in G:
        if vertex.getColor() == "white":
            connectedComponents.append(BFS(G, vertex))
            
    return connectedComponents


if __name__ == "__main__":
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addVertex('g')
    G.addVertex('h')
    G.addEdge('a', 'b', 1)  
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    
      
    connectedComponents = connected_components_with_bfs(G)
    print "Total number of connected components:", len(connectedComponents)
    print "The connected components are:"
    for components in connectedComponents:
        print components
