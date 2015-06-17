'''
Created on Jun 15, 2015

@author: Debanjan Mahata
'''

import GraphAlgorithms.Graph

keymap = {"0":"0",'1':"1",'2':"ABC",'3':"DEF",'4':"GHI",'5':"JKL",'6':"MNO",'7':"PQRS",'8':"TUV",'9':"WXYZ"}



#def phoneMnemonic(phoneNumber, digit, partialMnemonic, mnemonics):
#    phoneMnemonicHelper(phoneNumber, digit, partialMnemonic, mnemonics)
#    return mnemonics


#def phoneMnemonicHelper(phoneNumber, digit, partialMnemonic, mnemonics):
#    
#    if digit == len(phoneNumber):
#        mnemonics.append(partialMnemonic)
#    else:
#        for char in keymap[phoneNumber[digit]]:
#            partialMnemonic += char
#            phoneMnemonicHelper(phoneNumber, digit+1, partialMnemonic, mnemonics)
#            
#if __name__ == "__main__":
#    partialMnemonic = ""
#    mnemonics = []
#    phoneNumber = "234"
#    phoneMnemonicHelper(phoneNumber, 0, partialMnemonic, mnemonics)
#    print mnemonics
            

def construct_key_combination_graph(letterGraph, numberSeq):
    
    for i in range(0,len(numberSeq)-1):
        lettersLayer1 = keymap[numberSeq[i]]
        lettersLayer2 = keymap[numberSeq[i+1]]
        
        for entries in lettersLayer1:
            if letterGraph.getVertex(entries):
                pass
            else:
                letterGraph.addVertex(entries)
                letterGraph.getVertex(entries).layer = i
        
           
        for entries in lettersLayer2:
            if letterGraph.getVertex(entries):
                pass
            else:
                letterGraph.addVertex(entries)
                letterGraph.getVertex(entries).layer = i+1
            
        for l1 in lettersLayer1:
            for l2 in lettersLayer2:
                letterGraph.addEdge(l1, l2)
                
            
                
#    for vertex in letterGraph.getVertices():
#        print vertex
#        print letterGraph.getVertex(vertex).getConnections()
            
            
    return letterGraph.getVertices()

#import Queue
#def traversal(G, start, layer):
#    stringList = []
#    stringCombinationAtLevel = {}
#    q = Queue.Queue()
#    level = 0
#    q.put(start)
#    q.put("#")
#    stringList = []
#    while not q.empty():
#        node = q.get()
#        if node == "#":
#            if not q.empty():
#                q.put("#")
#             
#            if level < layer:   
#                stringList = []
##                print stringCombinationAtLevel
#                for entries in stringCombinationAtLevel[level]:
#                    stringList += entries
#            level += 1
#        else:
#            
#            for nbr in node.getConnections():
#                if level == 0:
#                    if level in stringCombinationAtLevel:
#                        stringCombinationAtLevel[level].append([node.getId()+nbr.getId()])
#                    else:
#                        stringCombinationAtLevel[level] = [[node.getId()+nbr.getId()]]
##                    tmpStr = node.getId()+nbr.getId()
##                    stringList.append(tmpStr)
#                else:
#                    tempList = []
#                    for entries in stringList:
#                        tempList.append(entries + nbr.getId())
#                    if level in stringCombinationAtLevel:
#                        stringCombinationAtLevel[level].append(tempList)
#                    else:
#                        stringCombinationAtLevel[level] = [tempList]
#                
#                q.put(nbr)
#            
#    print stringCombinationAtLevel[layer-1]
            
    
            
        
            
        
            
        
            

def permutations(G,firstKey):
    permutationList = []
    for vertex in G:
        if vertex.getId() in list(keymap[firstKey]):
#            print vertex.getId()
#            permutationList += traversal(G,G.getVertex(vertex))
            traversal(G,vertex,2)
            
            
                          
            
        
        
        
    



if __name__ == "__main__":
    
    letterGraph = GraphAlgorithms.Graph.DirectedGraph()
    
    vertices = construct_key_combination_graph(letterGraph,"234")
    
#    for vertex in letterGraph.getVertices():
#        print vertex
#        print letterGraph.getVertex(vertex).getConnections()
            
        
    permutations(letterGraph,"2")
#    
