#Closure --> funcion que genera otra funcion(accede variables locales, tienen memoria)

def saludar(username):
    mensaje=f"Hola {username}";#variable local

    def mostrar_mensaje(): #Anidada
        print(mensaje);

    return mostrar_mensaje();

username="Ilan";
respuesta=saludar(username);
