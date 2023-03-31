elementos = {}

elementos["Alumno"] = "Ilan"
elementos[(1, 2, 3)] = "La llave es una tupla"
elementos["Alumno"] = "Ilan Nestor"
elementos1 = {"a": 1, "b": 2, "c": 3, "d": 4}
print(elementos1)
print(elementos)
print(len(elementos))

# Eliminar elementos
del elementos1["a"]
print(elementos1)
elementos1.pop("b")
print(elementos1)

elementos1.clear()
print(elementos1)
