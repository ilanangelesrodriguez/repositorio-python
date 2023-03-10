usuarios=["Usuario1","Usuario2","Usuario3","Usuario4"];

#Foreach ---> For -- variable --
for usuario in usuarios:
    print(usuario);


titulo_curso="Dinamica de Sistemas II";
for letra in titulo_curso:
    if letra=="i":
        continue;
    print(letra);
