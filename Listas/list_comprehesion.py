numbers = []
print(numbers)

print("Version 1")
for element in range(1, 11):
    numbers.append(element*2)

print(numbers)

print("Version 2")
numbers_2 = [element*2 for element in range(1, 11)]
print(numbers_2)

# Con condiciones
print("Version 3")
numbers_3 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_3)
