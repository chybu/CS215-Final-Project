# Number of vertices
V  = 5

# Define infinity as a large enough value to
#  represent unconnected vertices
INF = 99999

#Initialize graph as adjacency matrix
graph = [[0, 4, INF, 5, INF],
         [INF, 0, 1, INF, 6],
         [2, INF, 0, 3, INF],
         [INF, INF, 1, 0, 2],
         [1, INF, INF, 4, 0]]


#graph = [[0, 5, INF, 10],
#       [INF, 0, 3, INF],
#      [INF, INF, 0,   1],
#     [INF, INF, INF, 0]]


def floydWarshall(graph):

    #create an empty copy of the graph matrix
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    #iterate through every vertex as a source
    for source in range(V):

        #iterate through every vertex as an intermediate
        for intermediate in range(V):

            #iterate through every vertex as a destination
            for destination in range(V):
                
                #if the new path is shorter than current, update
                dist[source][destination] = min(dist[source][destination], dist[source][intermediate] + dist[intermediate][destination])

    printGraph(dist)

def printGraph(graph):
    for list in graph:
        print(list)

if (__name__ == "__main__"):
    floydWarshall(graph)
