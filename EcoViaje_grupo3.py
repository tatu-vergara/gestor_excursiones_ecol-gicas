
# Creando la lista

excursiones = {

    1: {"Nombre" : "Torres del paine", "cupos disponibles": 15},
    2: {"Nombre" : "Rapa nui", "cupos disponibles": 15},
    3: {"Nombre" : "San pedro de atacama", "cupos disponibles": 15}
}


# Mostrar la lista de excursiones disponibles con cupos limitados.

def mostrar_lista():
    print("Excursiones disponibles: ")

    for num, datos in excursiones.items():
        if datos["cupos disponibles"] > 0:
            print(f"{num}. {datos['Nombre']} - Cupos dispobibles : {datos['cupos disponibles']}")
        else:
            print(f"{num}. {datos['Nombre']} - LLENO ")



while True:

    mostrar_lista()

    opcion = input("¿Deseas reservar una excursion? digite ´si´ o ´no´: ")
    opcion = opcion.lower()

    if opcion == "no":
        print("Adios,Vuelva pronto")
        break
    elif opcion == "si":
        pass
    elif opcion != "si":
        print("Opcion invalida,intente otra vez.")
        continue




    try:
        nombre = input("Ingrese su nombre: ")
        numero = int(input("ingrese el numero de la excursion que desea reservar"))
    except ValueError:
        print("Valores no validos")
        continue

    if numero not in excursiones:
        print("numero de excursion no valido.")

    if excursiones[numero]["cupos disponibles"] == 0:
        print("lo sentimos,esa excursion no tiene cupo")

    


    excursiones[numero]["cupos disponibles"] -= 1
    print(f"Reservando cupo para {nombre} en '{excursiones[numero]['Nombre']}'.")

