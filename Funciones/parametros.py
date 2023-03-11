import math


def area_circulo(radio, pi=math.pi):
    return pi*(radio**2);
resultado=area_circulo(4);
print(resultado);


print("|---- Promedio ----|");
def promedio(*listado):
    print(listado);
    print(type(listado));
    return sum(listado)/len(listado);
res_promedio=promedio(1,2,3,4,5);
print("Promedio: ",res_promedio);


#print(promedio(1));
#Por convencion *args--> para tuplas
def combinacion(p1,p2,*args,p4=100):
    print(p1);
    print(p2);
    print(args);
    print(p4);
    #print(p1,p2,args)
combinacion(12,11,13,1,2,3,4,p4=50);