#Concatenar
Nombres="Ilan Nestor";
Apellido="Angeles Rodriguez";

Nombre_Completo=Nombres+Apellido;
print(Nombre_Completo);

Nombre_Completo="Mr. %s %s" %(Nombres,Apellido);
print(Nombre_Completo);

Nombre_Completo="Ing. {} {}" .format(Nombres,Apellido);
print(Nombre_Completo);

Nombre_Completo="Ing. {LastName} {Name}" .format(Name=Nombres,LastName=Apellido);
print(Nombre_Completo);