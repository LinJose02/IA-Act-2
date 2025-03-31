# Buscar todas las rutas entre A y C
todas_rutas = sistema.encontrar_rutas("A", "C")
if todas_rutas:
    todas_rutas.sort()  # Ordenar las rutas por tiempo total ascendente
    print("Rutas encontradas:")
    for tiempo, ruta in todas_rutas:
        print(f"{' -> '.join(ruta)} con un tiempo total de {tiempo} minutos")
else:
    estaciones_disponibles = {r.origen for r in sistema.rutas} | {r.destino for r in sistema.rutas}
    print(f"No se encontró una ruta válida. Estaciones disponibles: {', '.join(estaciones_disponibles)}")

# Buscar la mejor ruta entre A y C aplicando reglas lógicas
mejor_tiempo, mejor_ruta = sistema.encontrar_mejor_ruta("A", "C")
if mejor_ruta:
    print(f"\nLa mejor ruta desde A hasta C es: {' -> '.join(mejor_ruta)} con un tiempo total de {mejor_tiempo} minutos")
else:
    estaciones_disponibles = {r.origen for r in sistema.rutas} | {r.destino for r in sistema.rutas}
    print(f"No se encontró una ruta válida. Estaciones disponibles: {', '.join(estaciones_disponibles)}")