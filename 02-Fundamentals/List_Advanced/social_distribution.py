population = [int(x) for x in input().split(", ")]
minimum = int(input())

for i in range(len(population)):
    max_index = population.index(max(population))
    if population[i] < minimum:
        transfer = population[max_index] - (minimum - population[i])
        population.pop(max_index)
        population.insert(max_index, transfer)
        population[i] = minimum

if min(population) >= minimum:
    print(population)
else:
    print("No equal distribution possible")
