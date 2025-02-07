# Python program for Floyd-Warshall Algorithm

# Number of vertices
V = 4

# Use a large number for vertices that are not conected
INF = 9999

# This algorithm solves the shortest path 
# between all pairs of vertices

def floydWarshall(graph):
    """ Final output will be dist[][]
        that will hold the shortest
        distance between every pair of vertices"""
    """ The result is initialized as a copy
        of the input graph"""
    
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):

        # pick all vertices as starting point
        for i in range(V):

            # pick all vertices as destination
            for j in range(V):

                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])
    
    printSolution(dist)

# function to print the solution
def printSolution(dist):
    print("The following matrix shows the shortest \
          distances between every pair of vertices")
    
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()

# Driver's code
if __name__ == "__main__":
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    floydWarshall(graph)
