#  Implement a genetic algorithm for the Knapsack Problem.

import random

# Define the items and their values and weights
items = [("item1", 10, 5), ("item2", 4, 2), ("item3", 6, 3), ("item4", 12, 6), ("item5", 8, 4)]

# Define the capacity of the knapsack
capacity = 10

# Define the size of the population and the number of generations
population_size = 10
num_generations = 100

def generate_individual():
    # Generate a random binary string representing the presence or absence of each item
    return [random.randint(0, 1) for _ in range(len(items))]

def calculate_fitness(individual):
    # Calculate the total value and weight of the items in the individual
    total_value = sum([items[i][1] * individual[i] for i in range(len(items))])
    total_weight = sum([items[i][2] * individual[i] for i in range(len(items))])
    # If the total weight exceeds the capacity, the fitness is 0
    if total_weight > capacity:
        return 0
    # Otherwise, the fitness is the total value
    else:
        return total_value

def select_parents(population):
    # Select two parents using tournament selection
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    while parent2 == parent1:
        parent2 = random.choice(population)
    return parent1, parent2

def crossover(parent1, parent2):
    # Perform single-point crossover
    crossover_point = random.randint(1, len(items) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    # Perform bitwise mutation
    mutation_rate = 0.01
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

def run_genetic_algorithm():
    # Generate the initial population
    population = [generate_individual() for _ in range(population_size)]
    # Iterate through the generations
    for generation in range(num_generations):
        # Calculate the fitness of each individual
        fitnesses = [calculate_fitness(individual) for individual in population]
        # Select the parents for the next generation
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
    # Return the best individual and its fitness
    best_individual = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_individual)
    return best_individual, best_fitness

best_individual, best_fitness = run_genetic_algorithm()
print("Best individual: ", best_individual)
print("Best fitness: ", best_fitness)
