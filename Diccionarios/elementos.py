elementos = {"a": 1, "b": 2, "c": 3, "d": 4}
print(elementos)
"""
valor=elementos["d"];
print(valor)
"""

print("a" in elementos)
# get
valor = elementos.get("d")
print(valor)

valor = elementos.get("f", "La llave no existe")
print(valor)

# setdefault --> valor de una llave
valor1 = elementos.setdefault("e", 5)
print(valor1)
print(elementos)
