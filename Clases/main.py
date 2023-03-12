#Class <CamelCase>
class Usuario:
    #No se puede dejar bloques vacios, podemos usar PASS, el bloque no hara nada
    pass


Ilan=Usuario();
print(Ilan);
#print(type(Ilan))
#Usuario(Argumento);


# Atributos de clase
# Atributos de instancia
class Club:
    name="FC Barcelona";
    DT="Xavi";

#print("Club:",Club.name);
#print("DT:",Club.DT);

#__dict__ ---> atributos que tienen las clases
# Almacena mediante un diccionario los atributos
Club1=Club();
Club2=Club();


Club1.name="Universitario de deportes";
Club1.DT="Fossati";
Club1.RUC=12345;


print(Club1.name)
#print(id(print(Club1.name)))
#print(id(print(Club.name)))
print(Club1.__dict__)
print("|--- Club2 ---|")
print(Club2.DT)