from datetime import datetime


# Encuentra el numero mas pequeño y manda al incio

# 1- Buscar el numero menor
# 2- Crear 2 subarrays para llevar el control del algoritmo
# 3- Imprimir el resultado del ordenamiento

def selectionSort(array, count=0):
    #Recorrer el array
    for i in range(len(array)):
        #Encontrar el valor minimo
        idx=i;
        for j in range(i+1, len(array)):
            if array[idx]>array[j]:
                idx=j;
                #Encontramos el menor valor y lo intercambiamos por el 1er valor del array desordenado
                array[i],array[idx]=array[idx],array[i];
                count += 1;
                print(count, "-->", array)
                #print(array)

    print("N° de intercambios", count)
    print(array)


"""
def selectionSort(array, count=0):
    n=len(array);
    for i in range(n):
        for j in range(n):
            if array[j]>array[i]:
                array[j],array[i]=array[i],array[j];
                count+=1;
                print(array)
    print("N° de cambios",count)
    print(array)
"""
Init=datetime.now();
#array=[3,2,5,6,1,0]
"""
array=[-796, 3229, -5164, -362, 4408, 8965, -6068, 9329, -3034, -443, -6693, 9497, 2615, -5966, -9065, -1160, 6148, 5517, 1123, -8887
,5649, 3302, -1176, -8542, -9166, 8, -2906, 8987, -2414, -7984, 4410, 8872, 5241, -4556, 59, -5562, -3877, 7452, -4467, 2076, 4076, 4297
,-3847, -2055, 4483, -1484, -2371, 6199, -7261, -7032, 6010, 2325, -6625, -2601, 3870, 1822, -5665, 9622, 9883, -5794, -5218, 2926, 8599, -3099
,6399, -2570, 3943, -2409, 5114, 9791, -4420, 1065, 3077, -1062, -8004, 4397, 1635, 8578, -9226, 9222, -1793, -2691, -5060, -4727, -4098
,946, -6558, -4111, 4575, -2685, -4729, -5277, 1936, 5106, -2089, 824, 9421, -1683, -2083, 7891, -2099, 1305, -9076, -3535, 2565, -2871, 9448
,7177, -8614, -9954, -362, 1455, -8834, -9846, -8412, 1175, -1981, -5991, 7201, -1997, -515, -1634, -9803, 1032, 9551, -6153, 8502, 3536
,-2980, 8681, -9210, 4408, 8780, -916, -369, -8651, 1246, -702, -5555, 23, 8208, 2037, 6941, 9545, -5147, 5063, -8358, 2772, 8553, 9885, 4624
,-3576, 9131, 1229, -429, -479, -673, -7060, -4031, 5650, 6679, 6796, 5622, -6256, -238, -6096, 3096, -1610, -2948, 6291, -1666, 5219, 5850, 7387
,-3260, 3672, -1766, -9941, 8252, 2649, 7079, -8026, 6356, 676, -5065, -6338, 3287, 680, -3269, 2770, 6637, -8744, 9162, -2204, -3066, -7228, 8762
,1505, 4957, 766, -9136, 4632, -5022, -9999, 5361, 2732, 7831, -501, -4650, 7236, 3682, -2438, 5574, -8230, -9669, -7442, 7966, -2905, 7629
,7137, 200, -8670, -749, 2228, 458, 7889, -3668, -5350, -3261, 6741, -6953, 4800, 3372, 6662, -1018, 8523, 3164, 3577, 9720, -6826, -1574, -7875
,-2796, -1078, -4755, 4926, 3368, 4302, 9254, 6410, -4689, 7878, 2461, 8233, -6688, 5904, 4735, -2940, 8830, 9976, -3674, 4222, -1446, 6187, -3181
,-8882, 5487, -6939, -7885, 3786, -6234, -1062, -4553, -5709, 8459, 5008, 3352, 6586, 537, -7610, 3261, 8246, -2105, 5107, 7957, -7886, -2925, -2541
,-7449, 9521, 5073, -239, -8054, -4379, -8323, -6485, -4828, -5294, -2720, 595];
"""
array=[3, 94, 86, 82, 90, 10, 87, 36, 61, 8, 17, 15, 22, 10, 23, 78, 25, 2, 30, 45, 98, 43, 98, 59, 53, 57, 2, 64, 1, 41,
32, 58, 19, 99, 60, 74, 48, 80, 44, 25, 68, 1, 89, 77, 60, 25, 99, 30, 76, 32, 57, 82, 52, 44, 72, 87, 34, 87, 65, 30, 54, 6, 31,
33, 44, 44, 42, 82, 90, 17, 9, 98, 28, 86, 69, 3, 17, 8, 45, 98, 12, 47, 95, 43, 72, 39, 41, 82, 74, 56, 65, 79, 50, 26, 67,
100, 24, 67, 38, 57];
selectionSort(array);
#for i in range(len(array)):
#    print("%d" %array[i]);
print("Tiempo:",datetime.now()-Init)
