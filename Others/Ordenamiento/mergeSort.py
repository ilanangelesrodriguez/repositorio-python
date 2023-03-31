# Utilizo recursividad para el algoritmo
from datetime import datetime


def mergeSort(arr):
    if len(arr)==True:
        return arr;
    else:
        middle=len(arr)//2;
        left_array=arr[:middle];
        right_array=arr[middle:];

        sorted_left_array=mergeSort(left_array);
        sorted_right_array=mergeSort(right_array);

    return Merge(sorted_left_array,sorted_right_array);


def Merge(left_arr,right_array):
    arr_resultado=[];
    #count+=1;
    while len(left_arr)>0 and len(right_array)>0:
        if left_arr[0]>right_array[0]:
            arr_resultado.append(right_array[0]);
            right_array.pop(0);
        else:
            arr_resultado.append(left_arr[0]);
            left_arr.pop(0);

    while len(left_arr)>0:
        arr_resultado.append(left_arr[0]);
        left_arr.pop(0);

    while len(right_array) > 0:
        arr_resultado.append(right_array[0]);
        right_array.pop(0);

    return arr_resultado;

#print(5//2)
#if __name__ == '__main__':
print("|----- Merge Sort ----|");
array_unordened=[3, 94, 86, 82, 90, 10, 87, 36, 61, 8, 17, 15, 22, 10, 23, 78, 25, 2, 30, 45, 98, 43, 98, 59, 53, 57, 2, 64, 1, 41,
32, 58, 19, 99, 60, 74, 48, 80, 44, 25, 68, 1, 89, 77, 60, 25, 99, 30, 76, 32, 57, 82, 52, 44, 72, 87, 34, 87, 65, 30, 54, 6, 31,
33, 44, 44, 42, 82, 90, 17, 9, 98, 28, 86, 69, 3, 17, 8, 45, 98, 12, 47, 95, 43, 72, 39, 41, 82, 74, 56, 65, 79, 50, 26, 67,
100, 24, 67, 38, 57];
print("Desordenado: ",array_unordened);
Init = datetime.now();
ordened=mergeSort(array_unordened);
print("Ordenado",ordened);
print("Iteraciones: ");
print("Tiempo:", datetime.now() - Init);