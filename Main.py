from FloydWarshall import floydWarshall
from SimAnnealing import simAnneal
from RandomAdjacencyMatrix import generateAdjacencyMatrix
vertices = 5
weight = 10
density = 0.5
adj_matrix = generateAdjacencyMatrix(vertices, weight, density) 
floydWarshall = floydWarshall(adj_matrix)

for row in adj_matrix:
    print(row)
print("\n shortest paths")
for row in floydWarshall:
    print(row)