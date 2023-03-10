from datetime import date
import sys

print("|--- Primer codigo en Python ---|")
x=20
x/=10
print("Resultado: "+str(x))

print("|------- Fecha --------|")
print(date.today())

print("|----- Conversión -----|")
print("Fecha actual: " + str(date.today()))

#print(sys.argv)
#print(sys.argv[0]) # program name
#print(sys.argv[1]) # first arg

print("|----- Entrada de Datos -----|")
name = input("Introduce tu nombre: ")
print("Hola "+name)

print("|----- Operaciones: SUMA -----|")
n1=input("1er Numero: ")
n2=input("2do Numero: ")
suma=int(n1)+int(n2)
print("Resultado: "+str(suma))