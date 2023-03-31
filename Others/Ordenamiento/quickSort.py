# Nescesitamos divisor datset
# Necesitamos punto pivotal
from datetime import datetime


def particion(array, low, high):
    i=low-1;
    pivot=array[high];

    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1;
            array[i],array[j]=array[j],array[i];

    array[i+1],array[high]=array[high],array[i+1];
    return (i+1);

def quikSort(array, low, high):
    if low<high:
        pi=particion(array, low, high);
        quikSort(array, low, pi-1);
        quikSort(array, pi+1, high);

print("|----- Quick Sort ----|");
array_unordened=[3, 94, 86, 82, 90, 10, 87, 36, 61, 8, 17, 15, 22, 10, 23, 78, 25, 2, 30, 45, 98, 43, 98, 59, 53, 57, 2, 64, 1, 41,
32, 58, 19, 99, 60, 74, 48, 80, 44, 25, 68, 1, 89, 77, 60, 25, 99, 30, 76, 32, 57, 82, 52, 44, 72, 87, 34, 87, 65, 30, 54, 6, 31,
33, 44, 44, 42, 82, 90, 17, 9, 98, 28, 86, 69, 3, 17, 8, 45, 98, 12, 47, 95, 43, 72, 39, 41, 82, 74, 56, 65, 79, 50, 26, 67,
100, 24, 67, 38, 57];
print("Desordenado: ",array_unordened);
Init = datetime.now();
n=len(array_unordened)
quikSort(array_unordened,0,n-1);
print("Ordenado",array_unordened);
print("Iteraciones: ");
print("Tiempo:", datetime.now() - Init);