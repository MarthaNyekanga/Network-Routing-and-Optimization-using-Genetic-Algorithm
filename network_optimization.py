import random

# -----------------------------
# Step 1: Define the Network
# -----------------------------
nodes = ["A", "B", "C", "D", "E"]

distances = {
    ("A", "B"): 5,
    ("A", "C"): 10,
    ("B", "D"): 3,
    ("C", "D"): 2,
    ("D", "E"): 4,
    ("B", "C"): 6,
    ("C", "E"): 8
}

start = "A"
end = "E"

# -----------------------------
# Step 2: Generate Random Route
# -----------------------------
def generate_route():
    middle_nodes = [n for n in nodes if n not in [start, end]]
    random.shuffle(middle_nodes)
    route = [start] + middle_nodes + [end]
    return route

# -----------------------------
# Step 3: Cost Function
# -----------------------------
def route_cost(route):
    total = 0
    for i in range(len(route) - 1):
        edge = (route[i], route[i+1])
        total += distances.get(edge, 100)  # penalty if path doesn't exist
    return total

# -----------------------------
# Step 4: Selection
# -----------------------------
def select_best(population, k=5):
    population = sorted(population, key=lambda x: route_cost(x))
    return population[:k]

# -----------------------------
# Step 5: Crossover
# -----------------------------
def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut]
    
    for node in parent2:
        if node not in child:
            child.append(node)
    
    return child

# -----------------------------
# Step 6: Mutation
# -----------------------------
def mutate(route, mutation_rate=0.1):
    route = route[:]
    if random.random() < mutation_rate:
        i = random.randint(1, len(route) - 2)
        j = random.randint(1, len(route) - 2)
        route[i], route[j] = route[j], route[i]
    return route

# -----------------------------
# Step 7: Genetic Algorithm
# -----------------------------
def genetic_algorithm(generations=50, population_size=20):
    population = [generate_route() for _ in range(population_size)]
    
    for generation in range(generations):
        selected = select_best(population)
        
        next_population = selected[:]
        
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_population.append(child)
        
        population = next_population
        
        best = min(population, key=route_cost)
        print(f"Generation {generation+1}: Best Cost = {route_cost(best)}")
    
    best_route = min(population, key=route_cost)
    return best_route

# -----------------------------
# Run the Algorithm
# -----------------------------
best = genetic_algorithm()

print("\nBest Route Found:", " -> ".join(best))
print("Total Cost:", route_cost(best))
