import math
import random

graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

V = 4

initial_temperature = 1000
cooling_rate = 0.99  
min_temperature = 1
max_iterations = 50000 

def cost(path):
    total_cost = 0

    for i in range(len(path) - 1):
        node1, node2 = path[i], path[i + 1]
        if graph[node1][node2] == float('inf'):  
            return float('inf')
        total_cost += graph[node1][node2]
    return total_cost

def generate_path(path):
    if len(path) == 2:
        return path
    
    new_path = path.copy()
    
    if random.random() < 0.5 and len(path) > 2:  # remove node
        idx = random.randint(1, len(path) - 2) 
        new_path.pop(idx) 
    else:  # insert node
        idx = random.randint(1, len(path) - 1)  
        valid_nodes = [x for x in range(V) if graph[path[idx - 1]][x] != float('inf') and x not in path]
        if valid_nodes:  
            new_node = random.choice(valid_nodes)  
            new_path.insert(idx, new_node)  
        else:
            return path  
    
    if cost(new_path) == float('inf'):
        return path  # keep original path
    
    return new_path

def simulated_annealing(start, end):
    if graph[start][end] != float('inf'):
        current_solution = [start, end] # start with path if valid
    else:
        current_solution = [start]
        current_node = start
        while current_node != end:
            next_nodes = [x for x in range(V) if graph[current_node][x] != float('inf') and x not in current_solution]
            if not next_nodes:
                break  
            current_node = random.choice(next_nodes)
            current_solution.append(current_node)
        if current_solution[-1] != end:
            current_solution.append(end)  

    current_cost = cost(current_solution)

    best_solution = current_solution
    best_cost = current_cost

    temperature = initial_temperature
    iteration = 0

    while temperature > min_temperature and iteration < max_iterations:
        neighbor_solution = generate_path(current_solution)

        neighbor_cost = cost(neighbor_solution)

        delta_cost = neighbor_cost - current_cost

        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        temperature *= cooling_rate
        iteration += 1

    return best_solution, best_cost

def simulated_annealing_solution_matrix(graph):
    solution = [[float('inf') for _ in range(V)] for _ in range(V)]
    for i in range(V):
        solution[i][i] = 0  

    for i in range(V):
        for j in range(V):
            if i != j:
                best_path, best_cost = simulated_annealing(i, j)
                solution[i][j] = best_cost

    return solution

def print_solution_matrix(solution):
    print("Following matrix shows the shortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if solution[i][j] == float('inf'):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d" % (solution[i][j]), end=" ")
        print()

solution_matrix = simulated_annealing_solution_matrix(graph)
print_solution_matrix(solution_matrix)