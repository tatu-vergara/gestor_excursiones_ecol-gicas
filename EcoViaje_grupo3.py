
excursiones = [
    {"id": 1, "nombre": "Cerro Chena", "cupos": 5},
    {"id": 2, "nombre": "Cerro Renca", "cupos": 10},
    {"id": 3, "nombre": "Cerro Carbón", "cupos": 8}
]

while True:
    for excursion in excursiones:
        print(f'{excursion["id"]} - {excursion["nombre"]} (Cupos disponibles: {excursion["cupos"]})')

    selecciona_excursion = int(input("ingresa el número de la excursión que quierer reservar: "))

    excursion_seleccionada = None

    for excursion in excursiones:
        if excursion["id"] == selecciona_excursion:
            excursion_seleccionada = excursion
            break

    if excursion_seleccionada:
        print(f"seleccionaste : {excursion_seleccionada['nombre']}")
        break
    else:
        print("no existe esa excursión")


cantidad_de_cupos = int(input("¿Cuántos cupos quieres reservar?"))