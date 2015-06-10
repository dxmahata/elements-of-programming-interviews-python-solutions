'''
Created on Jun 10, 2015

@author: Debanjan Mahata
'''

"""
Detecting Bipartite Graph using BFS or two color problem

The main strategy in this procedure is to do a BFS traversal of the 
given graph and to see if a bipartite graph can be constructed from it
or not.

We color the starting vertex red and then the vertices in the next level 
of the BFS tree as blue. We again color the vertices of the next level
as red. So the vertices of the alternative levels have alternate red and
blue colors.

While coloring if at any point there are two vertices that are of same
color but belong to alternate levels (parent and child level) of the BFS tree,
then a bipartite graph cannot be constructed. Otherwise, a bipartite graph
can be constructed out of the given graph.
"""

from Queue import Queue

from Graph import Graph


def is_bipartite(G,start):
    if G == None:
        return False
    else:
        q = Queue()
        start.setColor("red")
        q.put(start)
        
        while not q.empty():
            currNode = q.get()
            for node in currNode.getConnections():
                if node.getColor() == currNode.getColor():
                    return False
                if node.getColor() == "white":
                    if currNode.getColor() == "red":
                        node.setColor("blue")
                    if currNode.getColor() == "blue":
                        node.setColor("red")
                    q.put(node)
        
        return True


if __name__ == "__main__":
    
    G1 = Graph()
    G1.addVertex('a')
    G1.addVertex('b')
    G1.addVertex('c')
    G1.addVertex('d')
    G1.addVertex('e')
    G1.addVertex('f')
    
    G1.addEdge("a","b",1)
    G1.addEdge("a","f",1)
    G1.addEdge("f","e",1)
    G1.addEdge("e","d",1)
    G1.addEdge("d","c",1)
    G1.addEdge("c","b",1)
    
    print is_bipartite(G1,G1.getVertex('a'))
    
    G2 = Graph()
    G2.addVertex('a')
    G2.addVertex('b')
    G2.addVertex('c')
    G2.addVertex('d')
    G2.addVertex('e')
    G2.addVertex('f')
    G2.addVertex('g')
    
    G2.addEdge("a","b",1)
    G2.addEdge("a","f",1)
    G2.addEdge("f","e",1)
    G2.addEdge("e","d",1)
    G2.addEdge("d","c",1)
    G2.addEdge("c","b",1)
    G2.addEdge("g","f",1)
    G2.addEdge("g","a",1)
    
    print is_bipartite(G2,G2.getVertex('a'))


    
    
