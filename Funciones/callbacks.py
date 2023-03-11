promedio=lambda *args:sum(args)/len(args);

aprobatorio=lambda calificacion:calificacion>=10;

def mostrar_mensaje(f_prom,f_apro,*args):
    promedio=f_prom(*args);
    if f_apro(promedio):
        print(f"Felicidades aprobaste con {promedio}");
    else:
        print("No aprobaste");

mostrar_mensaje(promedio,aprobatorio,13,10,9)