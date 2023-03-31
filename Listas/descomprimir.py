print("|---- Descomprimir ----|")
numeros = (1, 2, 3, 4, 5, 6)
# uno,dos,tres,cuatro=1,2,3,4;
# *----> lista resto valores
# *_ ---> obviar valores
uno, dos, tres, cuatro, *resto_valores = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

posiciones = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_, nueve, diez = posiciones
print(uno)
print(dos)
print(nueve)
print(diez)

print("|------ Comprimir ------|")
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
resultado = zip(lista, tupla)  # ---> Objeto
resultado = tuple(resultado)
print(resultado)
