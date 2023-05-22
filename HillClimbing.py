import random


def objective_function(x):
    # This is a sample objective function that we want to optimize
    return x ** 2


def hill_climbing(initial_solution, step_size, objective_function):
    current_solution = initial_solution
    current_score = objective_function(current_solution)
    while True:
        # Generate a new solution by making a small random adjustment to the current solution
        new_solution = current_solution + random.uniform(-step_size, step_size)
        new_score = objective_function(new_solution)
        # If the new solution is better, make it the current solution
        if new_score < current_score:
            current_solution = new_solution
            current_score = new_score
        # Otherwise, terminate the algorithm and return the current solution
        else:
            return current_solution


# Example usage
initial_solution = 12
step_size = 7
solution = hill_climbing(initial_solution, step_size, objective_function)
print("Optimal solution:", solution)
