resultado=None;
print(resultado);
print(type(resultado));

#True(1) / False(0)
resultado=10;

if resultado>10:
    print("Resultado mayor que 10");
else:
    print("No es mayor que 10");

variable= "A" or 0 or [] or True;
print(variable);

listado=["Universitario"];
nombre="Ilan";
"""
if listado:
    variable=listado;
else:
    variable=nombre;

print(variable);
"""
variable=listado or nombre;
print(variable);