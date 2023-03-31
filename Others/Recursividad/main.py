# Recursividad

def factorial(n):
    if n==0:
        return 1;
    else:
        return n*factorial(n-1);


print("|--- Factorial de un Numero ---|");
num=int(input("Introduce el N°: "));
fact=factorial(num);
print("Factorial:",fact);
