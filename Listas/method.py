list_players=["Corzo","Cabanillas","Murrugarra","Ureña","Valera"];
list_players2=["Di Benedeto","Polo"];
print(list_players)
print(len(list_players));

list_players.append("Siucho");
print(list_players)
print(len(list_players));

list_players.insert(4,"Calcaterra");
print(list_players)
print(len(list_players));

list_players.extend(list_players2);
print(list_players);
print(list_players2);

list_players2.remove("Polo")
print(list_players2);

#Eliminar por indice
del list_players2[0];
print("Eliminar por indice")
print(list_players2);
print(len(list_players2));

#Eliminar todos los elementos de la lista;
print("Eliminar Lista")
list_players.clear()
print(list_players);
print(len(list_players));

#OPERACIONES
list=[23,2,15,17,1,3,8];
list.sort();
print(list);

#Ordenar a la inversa
list.sort(reverse=True);
print(list);
print(list[0]);
print(list[-1]);
print("Mayor");
print(max(list));
print("Menor");
print(min(list));

print(10 in list);
print(11 not in list);

list.sort(reverse=False);
print(list.index(3));

#Matrices
columna_a=[1,2];
columna_b=[3,4];
matriz=[columna_a,columna_b];#2x2
print(matriz);
print(matriz[1][1]);