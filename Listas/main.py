
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def print_var(variable):
    print(variable)
    print(type(variable))


# Constante, linea comentada
TITULO_CURSO = "|---- Listas ----|"

print(TITULO_CURSO)

"""Comentario
con saltos de linea
"""

# String
titulo = "Hola mundo :v"
titulo_2 = 'Here we go again'
mensaje = '''Barcelona
DT: Xavi
Jugador: Ansu Fati'''
print(mensaje)
# Int
# Al dividir con / obtenemos un dato flotante
# Al dividir con // se obtiene un dato entero
first_number = 3/2
print(first_number)
second_number = 3//2
print(second_number)
# Float
new_number = -3.4
print(new_number)
# Booleano
# True-False
valor = True
print(valor)

# Operadores logicos
# and, or y not
res = True and False
res2 = True or False
print(res)

tipo = type(titulo)
print(tipo)
print("|---- Nombre ----|")
a = input("Introduce tu nombre: ")  # String
print_var(a)

print("|---- Edad ----|")
edad = int(input("Introduce tu edad: "))
print_var(edad)

print("|---- Altura ----|")
altura = float(input("Introduce altura: "))
print_var(altura)

print("|---- Autorización ----|")
permitir = input("Dar autorizacion? (SI/NO)") == "SI"
print_var(permitir)

nombre, apellido, titulo = "Ilan", "Angeles", "Mr."

