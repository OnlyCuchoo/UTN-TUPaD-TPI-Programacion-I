# --- FUNCIÓN: Mostrar estadísticas ---
def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay países en la lista para mostrar estadísticas.")
        return
    
    pais_mayor_poblacion = max(lista_paises, key=lambda p: p["poblacion"])
    pais_menor_poblacion = min(lista_paises, key=lambda p: p["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in lista_paises) / len(lista_paises)
    promedio_superficie = sum(p["superficie"] for p in lista_paises) / len(lista_paises)
    
    paises_por_continente = {}
    for p in lista_paises:
        continente = p["continente"]
        paises_por_continente[continente] = paises_por_continente.get(continente, 0) + 1
        
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} (Población: {pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} (Población: {pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")
    
    print("Cantidad de países por continente:")
    for continente, cantidad in paises_por_continente.items():
        print(f"  - {continente}: {cantidad} país(es)")