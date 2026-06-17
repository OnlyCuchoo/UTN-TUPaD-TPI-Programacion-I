# --- FUNCIÓN: Buscar país por nombre ---
def buscar_pais(lista_paises):
    criterio = input("Ingrese el nombre del país a buscar (puede ser parcial): ").strip().lower()
    resultados = []
    for p in lista_paises:
        if criterio in p["nombre"].lower():
            resultados.append(p)
    if resultados:
        print(f"Se encontraron {len(resultados)} país(es) que coinciden con '{criterio}':")
        for pais in resultados:
            print(f"  - {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']} km², Continente: {pais['continente']})")
    else:
        print(f"No se encontraron países que coincidan con '{criterio}'.")

# --- FUNCIÓN: Filtrar países ---
def filtrar_paises(lista_paises):
    print("Opciones de filtrado:")
    print("1. Por continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    opcion = input("Seleccione una opción de filtrado (1-3): ").strip()
    
    if opcion == "1":
        continente = input("Ingrese el continente para filtrar: ").strip().lower()
        resultados = [p for p in lista_paises if p["continente"].strip().lower() == continente]
        if resultados:
            print(f"Países en el continente '{continente}':")
            for pais in resultados:
                print(f"  - {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']} km²)")
        else:
            print(f"No se encontraron países en el continente '{continente}'.")
            
    elif opcion == "2":
        poblacion_min = int(input("Ingrese la población mínima para filtrar: ").strip())
        poblacion_max = int(input("Ingrese la población máxima para filtrar: ").strip())
        if poblacion_min > poblacion_max:
            print("Error: La población mínima no puede ser mayor que la máxima.")
            return
        if (poblacion_min) < 0 or (poblacion_max) < 0:
            print("Error: La población mínima y máxima deben ser números enteros no negativos.")
        try:
            poblacion_min = (poblacion_min)
            poblacion_max = (poblacion_max)
            resultados = [p for p in lista_paises if poblacion_min <= p["poblacion"] <= poblacion_max]
            if resultados:
                print(f"Países con población entre {poblacion_min} y {poblacion_max}:")
                for pais in resultados:
                    print(f"  - {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']} km²)")
            else:
                print(f"No se encontraron países con población entre {poblacion_min} y {poblacion_max}.")
        except ValueError:
            print("Error: La población debe ser un número entero.")
    elif opcion == "3":
        superficie_min = int(input("Ingrese la superficie mínima para filtrar (en km²): ").strip())
        superficie_max = int(input("Ingrese la superficie máxima para filtrar (en km²): ").strip())
        if (superficie_min) < 0 or (superficie_max) < 0:
            print("Error: La superficie mínima y máxima deben ser números enteros no negativos.")
        try:
            superficie_min = float(superficie_min)
            superficie_max = float(superficie_max)
            resultados = [p for p in lista_paises if superficie_min <= p["superficie"] <= superficie_max]
            if resultados:
                print(f"Países con superficie entre {superficie_min} y {superficie_max} km²:")
                for pais in resultados:
                    print(f"  - {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']} km²)")
            else:
                print(f"No se encontraron países con superficie entre {superficie_min} y {superficie_max} km².")
        except ValueError:
            print("Error: La superficie debe ser un número.")
    else:
        print("Error: Opción de filtrado no válida.")
        return

# --- FUNCIÓN: Ordenar países ---
def ordenar_paises(lista_paises):
    print("Opciones de ordenamiento:")
    print("1. Por nombre (A-Z)")
    print("2. Por población (Mayor a Menor)")
    print("3. Por superficie (Ascendente o Descendente)")
    opcion = input("Seleccione una opción de ordenamiento (1-3): ").strip()
    
    if opcion == "1":
        lista_ordenada = sorted(lista_paises, key=lambda p: p["nombre"])
        print("Países ordenados por nombre (A-Z):")
        for pais in lista_ordenada:
            print(f"  - {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']} km²)")
    elif opcion == "2":
        lista_ordenada = sorted(lista_paises, key=lambda p: p["poblacion"], reverse=True)
        print("Países ordenados por población (mayor a menor):")
        for pais in lista_ordenada:
            print(f"  - {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']} km²)")
    elif opcion == "3":
        print("Opciones de ordenamiento por superficie:")
        print("1. Ascendente")
        print("2. Descendente")
        opcion_superficie = input("Seleccione una opción (1-2): ").strip()
        if opcion_superficie == "1":
            lista_ordenada = sorted(lista_paises, key=lambda p: p["superficie"])
            print("Países ordenados por superficie (menor a mayor):")
            for pais in lista_ordenada:
                print(f"  - {pais['nombre']} (Superficie: {pais['superficie']} km²)")
        elif opcion_superficie == "2":
            lista_ordenada = sorted(lista_paises, key=lambda p: p["superficie"], reverse=True)
            print("Países ordenados por superficie (mayor a menor):")
            for pais in lista_ordenada:
                print(f"  - {pais['nombre']} (Superficie: {pais['superficie']} km²)")
        else:
            print("Error: Opción de ordenamiento por superficie no válida.")
    else:
        print("Error: Opción de ordenamiento no válida.")