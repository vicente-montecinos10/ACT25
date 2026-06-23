
#creamos la lista deonde almacenarenmos los vehiculos
vehiculos = []

#0.- Funcion para validar la patente
def buscar(patente):
    for i in range(len(vehiculos)):
        if vehiculos[i]["patente"] == patente:
            return i
    return -1

#1.-agregar
def agregar(patente, tipo, anio, precio):
    #validar que tenga 6 caracteres sin espacios en blanco
    if len(patente)!=6:
        print("numero de caracteres no valido")
        return
    #validar que no tenga espacios en blanco
    elif " " in patente:
        print("no puede tener espacios en blanco")
        return
    #validar que la patente no se repita
    elif buscar(patente)>=0:
        print("no se puede repetir la patente")
        return
    #validar tipo
    elif tipo not in ("Sedan","suv","camioneta"):
        print("tipo no valido")
        return
    elif anio<2015 or anio>2026:
        print("Año no valido")
        return
    elif precio<=5000000:
        print("precio no valido")        
        return

    #Si los datos son validos creamos el directorios con los datos
    auto = {"Patente" :patente,"tipo":tipo,"anio":anio,"precio":precio}
    vehiculos.append(auto)
    print("vehiculo registrado")

def mostrar(patente):
    posicion = buscar(patente)
    if posicion >= 0:
        print(f"patente enconrtada : {vehiculos[posicion]}")
    else:
        print("patente no encontrada")

