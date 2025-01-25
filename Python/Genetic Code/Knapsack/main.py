import random

def generate_individual(length):
    return [random.choice([0,1]) for _ in range(length)]

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

def fitness(individual, items, capacity):
    total_weight = total_value = 0
    for i,gene in enumerate(individual):
        if gene==1:
            total_weight+=items[i]["weight"]
            total_value+=items[i]["value"]
    if total_weight > capacity:
        return 0
    return total_value

def selection(population, items, capacity):
    fitnesses = [fitness(ind, items, capacity) for ind in population]
    total_fitness = sum(fitnesses)
    if total_fitness==0:
        return random.sample(population, 2)
    probabilities = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=probabilities, k=2)

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1=parent1[:point]+parent2[point:]
    child2=parent2[:point]+parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

def genetic_algorithm():
    population = generate_population(POPULATION_SIZE, len(objects))

    for generation in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = selection(population, objects, max_weight)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1, MUTATION_RATE), mutate(child2, MUTATION_RATE)])
        population = new_population
        best_individual = max(population, key=lambda ind: fitness(ind, objects, max_weight))
        best_fitness = fitness(best_individual, objects, max_weight)
        print(f"Generation {generation+1}: Best Fitness = {best_fitness}")

    best_solution = max(population, key=lambda ind: fitness(ind, objects, max_weight))
    best_value = fitness(best_solution, objects, max_weight)
    total_weight = sum(objects[i]["weight"] for i, bit in enumerate(best_solution) if bit == 1)
    print("\nFinal Best Solution:")
    print(f"Items Selected: {best_solution}")
    print(f"Total Value: {best_value}")
    print(f"Total Weight: {total_weight}")

if __name__=="__main__":
    objects = [
        {"weight": 2, "value": 3},
        {"weight": 3, "value": 4},
        {"weight": 4, "value": 5},
        {"weight": 5, "value": 6},
        {"weight": 9, "value": 10},
    ]
    max_weight = 10

    POPULATION_SIZE = 20
    MUTATION_RATE = 0.1
    NUM_GENERATIONS = 50
    genetic_algorithm()