import random

def generateAdjacencyMatrix(vertices, weight, density):
    adjMatrix = [[float('inf')] * vertices for _ in range(vertices)]
    
    for i in range(vertices):
        #makes diags 0
        adjMatrix[i][i]=0
    
    for i in range(vertices):
        for j in range(i+1,vertices):
            if random.random() < density:
                weight = random.randint(1, weight)
                adjMatrix[i][j] = weight
                adjMatrix[j][i] = weight
    return adjMatrix
def floydWarshall(graph):

    #create an empty copy of the graph matrix
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for source in range(vertices):

        #pick intermediate vertices
        for intermediate in range(vertices):

            #pick destination vertices
            for destination in range(vertices):
                
                #check if new path to destination is shorter than current
                #update if true
                dist[source][destination] = min(dist[source][destination], dist[source][intermediate] + dist[intermediate][destination])
    for row in dist:
        print(row)
    return dist


vertices = 5
weight = 10
density = 0.5
adj_matrix = generateAdjacencyMatrix(vertices, weight, density) 
floydWarshall(adj_matrix)

for row in adj_matrix:
    print(row)