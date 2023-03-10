#Rango
#Inicio, Fin, Saltos(skip)
print("---- Range ----")
rango=range(2,8,2)
print(rango)
print(type(rango))

for valor in rango:
    print(valor);


print("--- Enumerate ---")
#Enumerar
numeros=[10,20,30,40,50];
for indice,numero in enumerate(numeros,20):
    print(indice, numero)
