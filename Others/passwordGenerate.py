import random
# Importo paquete para trabajar con aleatoriedad
import string
# Importo paquete para trabajar con aleatoriedad

def generatePassword():
    #Se genera listas de simbolos mayusculas, minusculas y numeros
    #declaracion de listas
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    numeros = ['0','1','2','3','4','5','6', '7', '8', '9']

    #Se suma las listas para tener un producto
    caracteres = mayus + minus + numeros
    password = []
    count = 0

    #ciclo para generar contrasenas
    while count < 15:
        caracter = random.choice(caracteres)
        password.append(caracter)
        count += 1

    #conversion de lista a cadena de texto
    password = "".join(password)

    return password

def main():
    password = generatePassword()
    print('Tu nueva contraseña es: '+ password)

if __name__ == "__main__":
    main()