def usuarios(**kwargs):  #Con 2 * --> se hace uso de un diccionario
    print(kwargs);
    print(type(kwargs));

usuarios(Ilan=[15,10,10]);


def combinacion(*args,**kwargs):
    print(args);
    print(kwargs);

print("|----- COMBINACION -----|");
combinacion(1,2,3,4,5,6,Universitario={"Valera","Cabanillas","Corzo"});