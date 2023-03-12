class Animal():
    def comer(self):
        print("El animal esta comiendo");
    def dormir(self):
        print("El animal esta ZZZZ");


class Mascota(Animal): #Clase padre
    def jugar(self):
        print("La mascota esta Jugando");

class Felino:
    def cazar(self):
        print("El felino esta Cazando");


class Perro(Mascota): #Clase hijo
    pass

class Gato(Mascota,Felino):
    pass


print("|---- Perro ----|")
Duke=Perro()
Duke.jugar();
Duke.comer()
Duke.dormir()
print("")

print("|---- Gato ----|")
Patero=Gato()
Patero.jugar()
Patero.comer()
Patero.dormir()
Patero.cazar()
#print(Duke)