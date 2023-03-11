# Es una función, toma como input una funcion y retorna la misma
# 3 funciones: input, output, main
# a ---> Decorador
# b ---> La funcion a decorar
# c ---> La funcion decorada
# a(b) = c

"""
def funcion_a(funcion_b):
    def funcion_c():
        print(">>> Antes del llamado.")
        funcion_b()
        print(">>> Despues del llamado.")
        #pass
    return funcion_c

#Para extender funcionalidades
@funcion_a
def saludar():
    print("Es una funcion");

    #def funcion_c():
    #    pass
    #return funcion_c()

saludar()
"""


def funcion_a(funcion_b):
    def funcion_c(*args,**kwargs):
        print(">>> Antes del llamado.")
        resultado=funcion_b(*args,**kwargs)
        print(">>> Despues del llamado.")
        #pass
        return resultado

    return funcion_c

#Para extender funcionalidades
@funcion_a
def suma(num_1,num_2):
    return num_1+num_2;

resultado=suma(10,20);
print(resultado)




