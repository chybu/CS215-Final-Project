import random
import math

def simulatedAnnealing(adj_matrix, temp=1000, cooling_rate=0.995, stopping_temp=1e-3):
    num_nodes = len(adj_matrix)
    
    # Generate an initial random solution (a random tour)
    current_solution = list(range(num_nodes))
    random.shuffle(current_solution)
    
    def calculate_cost(solution):
        cost = 0
        for i in range(num_nodes):
            cost += adj_matrix[solution[i]][solution[(i + 1) % num_nodes]]
        return cost
    
    current_cost = calculate_cost(current_solution)
    best_solution = current_solution[:]
    best_cost = current_cost
    
    while temp > stopping_temp:
        # Generate a new solution by swapping two random nodes
        new_solution = current_solution[:]
        a, b = random.sample(range(num_nodes), 2)
        new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
        
        new_cost = calculate_cost(new_solution)
        
        # Accept new solution based on probability
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_solution = new_solution[:]
            current_cost = new_cost
            
            # Update best solution
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
        
        # Cool down
        temp *= cooling_rate
    
    return best_solution, best_cost

