def centigrados_a_farhenheit(grados):
    return grados*1.8+32;

print(centigrados_a_farhenheit(10))
print(centigrados_a_farhenheit(-1))
print(type(centigrados_a_farhenheit));

#Funcion lambda
#lambda <parametro> : <cuerpo de la funcion>
funcion_lambda=lambda grados : grados*1.8+32;
print(funcion_lambda(10))