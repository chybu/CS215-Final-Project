import random
def generateAdjacencyMatrix(vertices, weight, density):
    adjMatrix = [[float('inf')] * vertices for _ in range(vertices)]
    
    for i in range(vertices):
        #makes diags 0
        adjMatrix[i][i]=0
    
    for i in range(vertices):
        for j in range(vertices):
            #different values to go/return to same location. ex: it could take a weight of 1 to go from a to b, but a weight of inf to go from b to a.
            
            if  i != j and random.random() < density:
                adjMatrix[i][j] = random.randint(1, weight)
    return adjMatrix