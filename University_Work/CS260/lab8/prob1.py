#! usr/bin/env python3

#Michael Palumbo

import sys

INF = sys.maxsize

def getInput():
    inp = []
    for line in sys.stdin:
        inp.append(line)
    return inp

def buildGraph(data):
    n = len(data)
    
    Graph = [[INF for i in range(n)] for i in range(n)]

    #Make diagonal 0's
    for i in range(n):
        Graph[i][i] = 0

    #Get Vertices from inputed data, and then add it to the graph
    for line in data:
        splitted = line.split()

        vertice = splitted[0]
        edges = splitted[1:]
        
        for e in edges:
            node , weight = e.split(",")
            Graph[int(vertice)][int(node)] = int(weight)
            Graph[int(node)][int(vertice)] = int(weight)
    return Graph

def printGraph(graph):
    for i in range(len(graph)):
        for ii in range(len(graph)):
            print(graph[i][ii] if graph[i][ii] != INF else "INF",end="\t")
        print()


def floyd_warshall(graph):
    #Predecessor Array
    n = len(graph)
    PGraph = [[INF for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                PGraph[i][j] = None
            else:
                PGraph[i][j] = i

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    PGraph[i][j] = PGraph[k][j]
    return graph, PGraph

if __name__ == "__main__":
    data = getInput()
    print("Orginal Graph")
    print(30*"-")
    graph = buildGraph(data)
    printGraph(graph)
    print("\nFloyd-Warshall affected Graph")
    print(30*"-")
    graph2, pgraph = floyd_warshall(graph)
    printGraph(graph2)
    print("\nPredecessor Graph")
    print(30*"-")
    printGraph(pgraph)
