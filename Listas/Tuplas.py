#Permite almacenar diferentes tipos de datos
#Son inmutables, no se modifican

#Cada elemento tiene un indice (0,1,2,3,....)
tupla=("first",1,2.5,True,4,[1,2,3],(4,5,6));
print(tupla);
print(type(tupla));

tupla2=("Java","Python","JavaScript","C++");
primer=tupla2[0];
print(primer);
ultimo=tupla[-1];
print(ultimo);

subtupla2=tupla2[0:2];
print(subtupla2);

#tupla2[:]--> subtupla con todos los elementos

print("|---- Ceiduns ----|");
cursos=["Ingles","Frances","Quechua","Aleman"];
tupla_cursos=tuple(cursos);
print(tupla_cursos);
print(type(tupla_cursos))

niveles=("Basico","Intermedio","Avanzado");
lista_niveles=list(niveles);
print(lista_niveles);
print(type(lista_niveles));