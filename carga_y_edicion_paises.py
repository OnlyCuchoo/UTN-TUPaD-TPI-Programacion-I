
# --- FUNCIÓN: Agregar un nuevo país manualmente ---
def agregar_pais(lista_paises):
    nombre = input("Ingrese el nombre del país: ").strip().lower()
    if nombre in [p["nombre"] for p in lista_paises]:
        print("Error: Ese país ya está en la lista.")
        return
    if not nombre.replace(" ", "").isalpha():
        print("Error: El nombre del país no puede contener números ni caracteres especiales.")
        return
    if nombre == "":
        print("Error: El nombre del país no puede estar vacío.")
        return
    try:
        poblacion = int(input("Ingrese la población del país: ").strip())
        if poblacion <= 0:
            print("Error: La población debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return
    if poblacion == "":
        print("Error: La población del país no puede estar vacía.")
        return
    try:
        superficie = int(input("Ingrese la superficie del país (en km²): ").strip())

        if superficie <= 0:
            print("Error: La superficie debe ser mayor a 0.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return
    continente = input("Ingrese el continente del país: ").strip().lower()
    if continente == "":
        print("Error: El continente del país no puede estar vacío.")
        return
    if not continente.replace(" ", "").isalpha():
        print("Error: El nombre del continente no puede contener números ni caracteres especiales.")
        return
    try:
        pais = {
            "nombre": nombre,
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente
        }
        lista_paises.append(pais)
        print(f"Éxito: País '{nombre}' agregado correctamente.")
    except ValueError:
        print("Error: La población y la superficie deben ser números enteros.")

# --- FUNCIÓN: Actualizar datos de un país ---
def actualizar_pais(lista_paises):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip().lower()
    pais_encontrado = None
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            pais_encontrado = p
            break
    if not pais_encontrado:
        print(f"Error: Ese país no está en la lista.")
        return
    
    print(f"Datos actuales de '{pais_encontrado['nombre']}':")
    print(f"  Población: {pais_encontrado['poblacion']}")
    print(f"  Superficie: {pais_encontrado['superficie']}")

    nueva_poblacion = input("Ingrese la nueva población (dejar vacío para mantener): ").strip()
    if nueva_poblacion != "":
        try:
            nueva_poblacion = int(nueva_poblacion)
            if nueva_poblacion <= 0:
                print("Error: La población debe ser mayor a 0.")
                return
        except ValueError:
            print("Error: La población debe ser un número entero.")
            return
    nueva_superficie = input("Ingrese la nueva superficie (dejar vacío para mantener): ").strip()
    if nueva_superficie != "":
        try:
            nueva_superficie = int(nueva_superficie)
            if nueva_superficie <= 0:
                print("Error: La superficie debe ser mayor a 0.")
                return
        except ValueError:
            print("Error: La superficie debe ser un número entero.")
            return
    print(f"Éxito: País '{pais_encontrado['nombre']}' actualizado correctamente.")