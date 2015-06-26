'''
Created on Jun 9, 2015

@author: Debanjan Mahata
'''
import sys

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.distance = sys.maxint
        self.entryTime = 0
        self.exitTime = 0
        self.predecessor = None
        self.indegree = 0
        self.outdegree = 0
        self.layer = None
        

    def addNeighbor(self,nbr,weight=0):
        """adds an edge from one vertex to another in the adjacency list"""
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """gets the list of vertices to which a vertex is connected to"""
        return self.connectedTo.keys()

    def getId(self):
        """gets the id of the vertex"""
        return self.id

    def getWeight(self,nbr):
        """gets the weight of the edge between two vertices"""
        return self.connectedTo[nbr]
    
    def setDistance(self,dist):
        """sets the distance of the vertex from a given source vertex during 
        calculation of shortest paths"""
        self.distance = dist
        
    def getDistance(self):
        """gets the distance of the vertex from a given source vertex during 
        calculation of shortest paths. The default value is infinity"""
        return self.distance
    
    def setColor(self,col):
        """sets the color of the vertex during implementation of graph traversals"""
        self.color = col
        
    def getColor(self):
        """gets the color of the vertex during implementation of graph traversals.
        The default is 'white', which stands for unvisited. The color codes are:
        'gray' -> visited
        'black' -> explored/processed"""
        return self.color
    
    def setEntryTime(self,t):
        """Sets the time at which DFS first visits the vertex"""
        self.entryTime = t
        
    def getEntryTime(self):
        """Gets the time at which DFS first visits the vertex"""
        return self.entryTime
    
    
    def setExitTime(self,t):
        """Sets the time at which DFS last visits the vertex"""
        self.exitTime = t
        
    def getExitTime(self):
        """Gets the time at which DFS last visits the vertex"""
        return self.exitTime

    def setPredecessor(self,pred):
        self.predecessor = pred
        
    def getPredecessor(self):
        return self.predecessor
    
    def setInDegree(self,indegree):
        self.indegree = indegree
        
    def getInDegree(self):
        return self.indegree
    
    def setOutDegree(self,outdegree):
        self.outdegree = outdegree
        
    def getOutDegree(self):
        return self.outdegree

    
    
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        """adds new vertex to the graph"""
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        

    def getVertex(self,n):
        """gets the vertex with id n"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        """checks if the vertex with id n is present in the graph"""
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        """adds an undirected edge between vertex with id f and a vertex with id t, cost
        being the weight of the edge."""
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[f].setOutDegree(self.vertList[f].getOutDegree()+1)
        self.vertList[t].setInDegree(self.vertList[t].getInDegree()+1)
        
        self.vertList[t].addNeighbor(self.vertList[f], cost)
        self.vertList[t].setOutDegree(self.vertList[t].getOutDegree()+1)
        self.vertList[f].setInDegree(self.vertList[f].getInDegree()+1)

    def getVertices(self):
        """gets the list of vertices of the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterator for the vertices of the graph"""
        return iter(self.vertList.values())
    
    
class DirectedGraph(Graph):
    
    def addEdge(self,f,t,cost=0):
        """adds an edge for a directed graph"""
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[f].setOutDegree(self.vertList[f].getOutDegree()+1)
        self.vertList[t].setInDegree(self.vertList[t].getInDegree()+1)




