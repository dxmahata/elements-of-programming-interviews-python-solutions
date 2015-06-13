'''
Created on Jun 10, 2015

@author: Debanjan Mahata
'''

"""
The topological sort is a simple but useful adaptation of a depth first search. The algorithm for the topological sort is as follows:

1. Call dfs(g) for some graph g. The main reason we want to call depth first search is to compute the finish times for each of the vertices.
2. Store the vertices in a list in decreasing order of finish time.
3. Return the ordered list as the result of the topological sort.
"""

import heapq
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
            
        stack = []
        time = 0
        start.setColor("gray")
        start.setPredecessor(None)
        time += 1
        start.setEntryTime(time)
        stack.append(start)
        while stack:
            currNode = stack.pop()
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


#def topologicalSort(G,start):
#    if G == None:
#        return []
#    else:
#        #raise assertion error if the graph has a cycle
#        assert has_cycle(G,start) == False
#        
#        for vertex in G:
#            vertex.setColor("white")
#            vertex.setPredecessor(None)
#            vertex.setDistance(sys.maxint)
#            vertex.setEntryTime(0)
#            vertex.setExitTime(0)
#
#        heap = []
#        stack = []
#        time = 0
#        start.setColor("gray")
#        start.setPredecessor(None)
#        time += 1
#        start.setEntryTime(time)
#        stack.append(start)
#        while stack:
#            currNode = stack.pop()
#            for node in currNode.getConnections():
#                if node.getColor() == "white":
#                    time += 1
#                    node.setColor("gray")
#                    node.setPredecessor(currNode)
#                    node.setEntryTime(time)
#                    stack.append(node)
#            currNode.setColor("black")
#            time += 1
#            currNode.setExitTime(time)
#            heapq.heappush(heap,(time,currNode.getId()))
#            
#        return heap
#    
#def topologicalSortRecursive(G,node,heap):
#    pass
def topologicalSort(G):
    """Perform a topological sort of the nodes. If the graph has a cycle,
    throw a GraphTopologicalException with the list of successfully
    ordered nodes."""
    # topologically sorted list of the nodes (result)
    topologicalList = []
    # queue (fifo list) of the nodes with inDegree 0
    topologicalQueue = []
    # {node: inDegree} for the remaining nodes (those with inDegree>0)
    remainingInDegree = {}
    
    nodes = G.getVertices()
    for v in G:
        indegree = v.getInDegree()
        if indegree == 0:
            topologicalQueue.append(v)
        else:
            remainingInDegree[v] = indegree

    # remove nodes with inDegree 0 and decrease the inDegree of their sons
    while len(topologicalQueue):
        # remove the first node with degree 0
        node = topologicalQueue.pop(0)
        topologicalList.append(node)
        # decrease the inDegree of the sons
        for son in node.getConnections():
            son.setInDegree(son.getInDegree() - 1)
            if son.getInDegree() == 0:
                topologicalQueue.append(son)

    # if not all nodes were covered, the graph must have a cycle
    # raise a GraphTopographicalException
    if len(topologicalList) != len(nodes):
        print "Error"
        
    # Printing the topological order    
    while len(topologicalList):
        node = topologicalList.pop(0)
        print node.getId()
    
    
if __name__ == "__main__":
    
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
    
    topologicalSort(G)
    
#    topologicalSortedNodes = topologicalSort(G,G.getVertex('a'))
    
    
    DG = DirectedGraph()
    DG.addVertex('a')
    DG.addVertex('b')
    DG.addVertex('c')
    DG.addVertex('d')
    DG.addVertex('e')
    DG.addVertex('f')
    DG.addVertex('g')
    DG.addVertex('h')
    DG.addVertex('i')

    DG.addEdge('a', 'd', 1)  
    DG.addEdge('b', 'd', 1)
    DG.addEdge('c', 'd', 1)
    DG.addEdge('d', 'g', 1)
    DG.addEdge('d', 'e', 1)
    DG.addEdge('g', 'h', 1)
    DG.addEdge('f', 'e', 1)
    DG.addEdge('e', 'i', 1)
    DG.addEdge('i', 'h', 1)
    
    topologicalSort(DG)
    
    DG1 = DirectedGraph()
    DG1.addVertex('a')
    DG1.addVertex('b')
    DG1.addVertex('c')
    DG1.addVertex('d')
    DG1.addVertex('e')
    DG1.addVertex('f')
    DG1.addVertex('g')
    DG1.addVertex('h')
    DG1.addVertex('i')

    DG1.addEdge('a', 'b', 1)  
    DG1.addEdge('b', 'c', 1)
    DG1.addEdge('c', 'd', 1)
    DG1.addEdge('e', 'a', 1)
    DG1.addEdge('e', 'c', 1)
    DG1.addEdge('d', 'e', 1)

    topologicalSort(DG1)
    
#    topologicalSortedNodes = topologicalSort(DG,DG.getVertex('a'))
#    print topologicalSortedNodes[::-1]
#    
#    for node in topologicalSortedNodes[::-1]:
#        print node[1].getId()


    
    
    
    

