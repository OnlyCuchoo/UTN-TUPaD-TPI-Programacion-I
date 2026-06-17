from archivos import cargar_desde_csv_automatico, guardar_en_csv
from consultas import buscar_pais, filtrar_paises, ordenar_paises
from estadisticas import mostrar_estadisticas
from carga_y_edicion_paises import agregar_pais, actualizar_pais

# --- FUNCIÓN: Mostrar Menú ---
def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Agregar un nuevo país")
    print("2. Actualizar datos de un país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

# --- FUNCIÓN PRINCIPAL ---
def main():
    # El programa se inicia ejecutando directamente la carga interna del CSV
    lista_paises = cargar_desde_csv_automatico()
    opcion = ""
    try:
        while opcion != "7":
            mostrar_menu()
            opcion = input("Seleccione una opción (1-7): ").strip()
            
            if opcion == "1":
                agregar_pais(lista_paises)
            elif opcion == "2":
                actualizar_pais(lista_paises)
            elif opcion == "3":
                buscar_pais(lista_paises)
            elif opcion == "4":
                filtrar_paises(lista_paises)
            elif opcion == "5":
                ordenar_paises(lista_paises)
            elif opcion == "6":
                mostrar_estadisticas(lista_paises)
            elif opcion == "7":
                guardar_en_csv(lista_paises)
                print("Saliendo del programa. ¡Hasta luego!")
            else:
                print("Error: Opción no válida. Por favor, seleccione un número entre 1 y 7.")
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupción detectada. Guardando datos antes de salir...")
        guardar_en_csv(lista_paises)
        print("Datos guardados. Saliendo del programa. ¡Hasta luego!")

if __name__ == "__main__":
    main()