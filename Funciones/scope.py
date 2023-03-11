#Scope
player="Messi";  #Variable global --> funcion, condicion, ciclo

def print_player():
        player="Ansu Fati";  #Variable local
        print("V. LOCAL:",player);
        print(id(player));


print_player();
print("V. GLOBAL:",player);
print(id(player));