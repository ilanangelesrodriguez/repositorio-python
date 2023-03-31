import random

countries = ['col', 'mex', 'per']
population = {}

for country in countries:
    population[country] = random.randint(1, 10)

print(population)

population_v2 = {country: random.randint(1, 10) for country in countries}

print(population_v2)

names = ["Ansu Fati", "Ferran Torres", "O. Dembelé"]
numbers = [10, 11, 7]

fist_dic = dict(zip(names, numbers))
print(fist_dic)

list1 = list(zip(names, numbers))
second_dic = {names: numbers for (names, numbers) in list1}
print(second_dic)

third_dic = {names[i]: numbers[i] for i in range(len(names))}
print(third_dic)

