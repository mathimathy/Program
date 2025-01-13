import string
import random

CHARSET = string.ascii_letters + string.digits + " "

def generate_individual(length):
    return ''.join(random.choice(CHARSET) for _ in range(length))

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

def fitness(individual, target):
    return sum(1 for i, letter in enumerate(individual) if letter == target[i])

def selection(population, target):
    fitnesses = [fitness(ind, target) for ind in population]
    total_fitness = sum(fitnesses)
    if total_fitness==0:
        return random.sample(population, 2)
    probabilities = [f/total_fitness for f in fitnesses]
    return random.choices(population, weights=probabilities, k=2)

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1=parent1[:point]+parent2[point:]
    child2=parent2[:point]+parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    return ''.join(
        letter if random.random() > mutation_rate else random.choice(CHARSET)
        for letter in individual
    )

def genetic_algorithm():
    population = generate_population(POPULATION_SIZE, WORD_LENGTH)

    for generation in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = selection(population, TARGET_WORD)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1, MUTATION_RATE), mutate(child2, MUTATION_RATE)])
        population = new_population
        best_individual = max(population, key=lambda ind: fitness(ind, TARGET_WORD))
        best_fitness = fitness(best_individual, TARGET_WORD)
        print(f"Generation {generation+1}: Best Word = {best_individual}, Fitness: {best_fitness}")
        if best_fitness == WORD_LENGTH:
            print("\nSolution Found")
            print(f"Target Word: {TARGET_WORD}")
            print(f"Guessed Word: {best_individual}")
            break

if __name__=="__main__":
    TARGET_WORD="Spagghetti"
    WORD_LENGTH=len(TARGET_WORD)

    POPULATION_SIZE = 200
    MUTATION_RATE = 0.1
    NUM_GENERATIONS = 500
    genetic_algorithm()