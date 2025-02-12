INF = 999999

#number of unique vertices in the graph
V = 5

graph = [[0, 4, INF, 5, INF],
         [INF, 0, 1, INF, 6],
         [2, INF, 0, 3, INF],
         [INF, INF, 1, 0, 2],
         [1, INF, INF, 4, 0]]

#graph = [[0, 5, INF, 10],
#        [INF, 0, 3, INF],
#        [INF, INF, 0, 1],
#       [INF, INF, INF, 0]]

def floydWarshall(graph):

    #create an empty copy of the graph matrix
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for source in range(V):

        #pick intermediate vertices
        for intermediate in range(V):

            #pick destination vertices
            for destination in range(V):
                
                #check if new path to destination is shorter than current
                #update if true
                dist[source][destination] = min(dist[source][destination], dist[source][intermediate] + dist[intermediate][destination])
    printGraph(dist)

def printGraph(graph):
    for list in graph:
        print(list)

if(__name__ == "__main__"):
    floydWarshall(graph)
                