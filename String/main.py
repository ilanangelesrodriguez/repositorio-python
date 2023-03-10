# Strings
"""@ilanangelesrodriguez"""
lenguajes="Python Java Javascript C";
listado=lenguajes.split(); #Divide el string entre los espacios
print("|---- Separación por espacio ----|")
print(lenguajes)
print(listado)


print("|----- Separación por Guion -----|")
clubes="Universitario-Barcelona-BVB";
listado2=clubes.split("-");
print(clubes)
print(listado2)

print("|----- Separación por Slash -----|")
clubes1="Universitario//Barcelona//BVB";
listado3=clubes1.split("//",1); #N° de separacion
print(clubes1)
print(listado3)


#Generar String a partir de una lista
a="a"
print("Creacion de String a partir de lista")
string=" ".join(listado);
print(string)
print(type(string))





