# Permiten almacenar diferentes tipos de datos, incluso diccionarios
# Son mutables --> podemos modificar longitud y elementos
# No se rigen por indices, sino una llave
# llave --> valor
diccionario1 = {}
diccionario2 = dict()
# {llave: valor que se quiere asociar}

diccionario = {"total": 55}
diccionario = {"Total": 30, "Descuento": True, "Producto": "Gashosha"}

usuario = {
    "Nombre": "Ilan",
    "Edad": 20,
    "Curso": "Python",
    "Skills": {
        "Programacion": True,
        "Base de Datos": False
    },
    "Club": ["Barcelona", "Universitario"]
}
print("|---- DICCIONARIO ----|")
# Crear diccionario
diccionario_new=dict()
# Agregar nueva llave valor
diccionario_new["Usuario"] = "Messi"
# Actualizar valor mediante llave
diccionario_new["Usuario"] = "Yo"
# Obtener valor mediante una llave
print(diccionario_new["Usuario"])

print(usuario.keys())
print(usuario.values())

for key, value in usuario.items():
    print(key, value)
