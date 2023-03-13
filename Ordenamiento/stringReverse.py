#string=[];
#n=len(string);
#if n==0:
#    print("Arreglo vacio")

def reverseString(string):
    if string == "":
        return string
    else:
        return reverseString(string[1:]) + string[0]

String=input("Introduce cadena: ");
print("1er elemento:",String[0])
print("Resto:",String[1:]);
String=reverseString(String);
print(String)