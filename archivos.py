import csv

# --- FUNCIÓN: Cargar países automáticamente al iniciar ---
def cargar_desde_csv_automatico():
    lista_inicial = []
    try:
        with open("paises.csv", "r", encoding="utf-8-sig") as archivo:
            # NOTA: Si tu archivo CSV sigue sin encabezados en la primera línea,
            # debes usar: csv.DictReader(archivo, delimiter=';', fieldnames=["nombre", "poblacion", "superficie", "continente"])
            lector_csv = csv.DictReader(archivo, delimiter=';')
            
            for fila in lector_csv:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    lista_inicial.append(pais)
                except KeyError as e:
                    print(f"Error al iniciar: No se encontró la columna {e} en el CSV.")
                    return []
                except ValueError:
                    print(f"Aviso: se omitió '{fila.get('nombre','?')}' por datos inválidos")
            print(f"--- Base de datos inicializada: {len(lista_inicial)} países cargados automáticamente. ---")
    except FileNotFoundError:
        print("Aviso: No se encontró el archivo 'paises.csv'. El programa iniciará vacío.")
    
    return lista_inicial

# --- FUNCIÓN: Guardar países al salir ---
def guardar_en_csv(lista_paises):
    try:
        with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor_csv = csv.DictWriter(archivo, fieldnames=campos, delimiter=';')
            escritor_csv.writeheader()
            for pais in lista_paises:
                escritor_csv.writerow(pais)
        print(f"--- Base de datos guardada: {len(lista_paises)} países exportados a 'paises.csv'. ---")
    except PermissionError:
        print("Error: No se pudo guardar el archivo 'paises.csv'. Verifique los permisos de escritura.")
    except OSError:
        print(f"Error del sistema al guardar el archivo: {e}. Verifique espacio en disco y la ruta de guardado.")
    except Exception as e:
        print(f"Error inesperado al guardar el archivo: {e}.")