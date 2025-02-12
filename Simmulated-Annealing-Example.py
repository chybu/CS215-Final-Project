import random
import math

#We us a dictionary to represent the displacency matrix
#because it is more efficient to look up the weight between 2 nodes

graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25, 4: 30},
    2: {0: 15, 1: 35, 3: 30, 4: 20},
    3: {0: 20, 1: 25, 2: 30, 4: 10},
    4: {1: 30, 2: 20, 3: 10}
}
start_node = 0
end_node = 2

def generate_initial_path():
    nodes = list(graph.keys()) # creates a list of nodes by taking the keys from the outer dictionary
    nodes.remove(start_node) # Remove the start and end of the path to
    nodes.remove(end_node) # preserve them from the random changes
    random.shuffle(nodes) # shuffles intermediate nodes

    return [start_node] + nodes + [end_node]

def path_cost(path):
    cost = 0
    INF = 999999
    for i in range(len(path) - 1):
        if path[i + 1] in graph[path[i]]: # This if checks if the next node in path is connected to the previous in the graph
            cost += graph[path[i][path[i + 1]]]
        else:
            return INF # return a very large number if the random path is unconnected in the graph to prevent consideration for a solution
    return cost

#Takes a given path and makes random changes to it
def get_neighbor_path(path):
    new_path = path[:] # Copy the current path
    rand_index1, rand_index2 = random.sample(range(1, len(path) - 1), 2) # picks two random indices from the path two swap, excluding the start and end
    new_path[rand_index1], new_path[rand_index2] = new_path[rand_index2], new_path[rand_index1] # swap nodes
    
    return new_path

#Initialize all of the parameters for simulated annealing
initial_temp = 1000

"""
graph        : Dictionary of dictionaries representing the adjacency matrix
start_node   : The node that our path starts from
end_node     : The node that our path ends at
temp         : The starting temperature that allows for exploration
cooling_rate : Controls how fast the temperature decreases

"""
def simulated_annealing (graph, start_node, end_node, temp, cooling_rate, min_temp):
    current_path = generate_initial_path()
    current_cost = path_cost(current_path)
    best_path = current_path[:]
    best_cost = current_cost

    while temp > min_temp:
        new_path = get_neighbor_path(current_path) # Get a new possible solution
        new_cost = path_cost(new_path) # Evaluate its cost

        #Check whether the new solution is better or is accepted based on the temperature
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / temp):
            current_path, current_cost = new_path, new_cost
            if new_cost < best_cost:
                best_path, best_cost = new_path[:], new_cost

        #Update the temperature
        temp *= cooling_rate

    return best_path, best_cost
shortest_path, shortest_cost = simulated_annealing(graph, start_node, end_node, initial_temp, 0.99, 1)
print(shortest_path)
print(shortest_cost)
     