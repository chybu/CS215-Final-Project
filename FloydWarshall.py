import copy

V = 4

inf = 99999

def floydWarshall(graph):
    solution = copy.deepcopy(graph)

    for i in range(V):

        for j in range(V):

            for k in range(V):

                solution[j][k] = min(solution[j][k], solution[j][i] + solution[i][k])
                
    printSolution(solution)

def printSolution(graph):
    print("Following matrix shows the shortest distances\
        between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(graph[i][j] == inf):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (graph[i][j]), end=' ')
            if j == V-1:
                print()


if __name__ == "__main__":
    graph = [[0, 5, inf, 10],
             [inf, 0, 3, inf],
             [inf, inf, 0, 1],
             [inf, inf, inf, 0]]
    
    floydWarshall(graph)