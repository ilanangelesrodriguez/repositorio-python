def operacion(cantidad,balance,tipo="Deposito"):

    def deposito(cantidad,balance):
        return cantidad+balance;


    def retiro(cantidad,balance):
        if cantidad<=balance:
            return balance-cantidad;
        else:
            return None;


    if tipo=="Deposito":
        return deposito(cantidad,balance);
    elif tipo=="Retiro":
        return retiro(cantidad,balance);
    #print(deposito(10,20));
    #print(retiro(150,80));

resultado=operacion(10,20);
print(resultado);