#Metodos
class Usuario:
    # __init__ : Metodo para inicializar los atributos de objeto
    # Object
    def __init__(self,username='',password=''):  #Se llama cuando instanciamos
        print("Estamos creando un usuario.")
        self.username = username;
        self.password = password;

    """
    def inicializar(self,username,password):
        self.username=username;
        self.password=password;
    """

    def saludar(self):
        return "Hola"


User1= Usuario("Ilan",123);
#User1.name="Ilan";
User2= Usuario("User2",456);
User3=Usuario();
"""
User1.inicializar("Ilan",123);
User2.inicializar("User2",456);
"""
Ilan=User1.__dict__;
User2=User2.__dict__;
User3=User3.__dict__;
print(Ilan)
print(User2)
print(User3)
