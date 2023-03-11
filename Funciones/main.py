# Docstring: Comentario que se coloca en la 1ra linea de la funcion
# El docstring se almacena en el atributo __doc__
# __doc__ :(Modulos ,Clases, Metodos y Funciones)

def suma_numeros(num_1,num_2):
    """
    La funcion suma dos numeros, ----> Descripcion
    Argumentos:
    :param num_1:
    :param num_2:

    Retorna la suma de los parametros
    :return:

    >>> suma_numeros(12,10)
    22
    >>> suma_numeros(10,24)
    34
    TODO:
        *Elementos;
    """
    #suma=num_1+num_2;
    return num_1+num_2, "Operacion de 2 variables";

"""
def pedir_numero():
    num=int(input("Numero: "));
"""

print("|----- SUMA -----|")
num_1=int(input("1er número: "));
num_2=int(input("2do número: "));
resultado, variables=suma_numeros(num_1,num_2);
print("El resultado es: ",resultado);
print(variables);
print(type(resultado))

print("|--- Documentacion ---|")
#print(suma_numeros.__doc__);
print(help(suma_numeros))