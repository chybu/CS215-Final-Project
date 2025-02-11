import random

def floydWarshall(graph):
    vertices = len(graph)
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
    return dist