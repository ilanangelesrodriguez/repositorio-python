class SerVivo:
    def dormir(self):
        print("El ser duerme");

class Animal(SerVivo): #Clase padre
    def comer(self):
        super().comer();
        print("El animal esta comiendo");
    def dormir(self): #Clase padre
        print("El animal esta ZZZZ");

class Mascota(Animal): #Clase padre
    def jugar(self):
        print("La mascota esta Jugando");
    def comer(self):
        super().comer();
        print("La mascota esta comiendo");

class Felino:
    def cazar(self):
        print("El felino esta Cazando");

class Gato(Mascota,Felino): #Clase hijo
    def __init__(self,nombre):
        self.nombre=nombre;

    def comer(self):
        print(f"{self.nombre} esta comiendo");

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")


patero=Gato("Patero")

patero.comer();  #Toma el metodo mas cercano
patero.dormir();

#La funcion super nos permite acceder al padre inmediato de la clase