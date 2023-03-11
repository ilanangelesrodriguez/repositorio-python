# Generador: Retorna objetos que podemos iterar sin que la funcion finalice

def pares():  #Generador -> Lazy iterator--> Podemos obtener cada objeto que genera
    for numero in range(0,100,2):
        yield numero #Suspende su ejecucion

        print("Se reanuda el generador")

#yield: Suspende su ejecucion, para retornar el objeto
"""
pares();
for par in pares():
    print(par)
#print(pares())
"""

"""
Ventajas del generador:
yield, suspende la funcion de forma momentanea, 
uso memoria, reservamos
"""
generador=pares();
while True:
    try:
        par=next(generador);
        print(par);
    except StopIteration:
        print("FIN");
        break;

#print(next(generador))
