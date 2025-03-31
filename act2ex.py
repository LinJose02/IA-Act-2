""" 
30/03/2025
IA - ACT 2 Busqueda y sistemas basados en reglas
Linda Carolina Zambrano Leon, Juan Sebastián Hernández Galindo, Jose Luis Rodriguez Castillo
"""

""" Sistema inteligente para encontrar la mejor ruta en un sistema de transporte masivo """

class Ruta:
    """Clase que representa una conexión entre estaciones y su tiempo de viaje."""
    def __init__(self, origen, destino, tiempo):
        self.origen = origen  # Estación de origen
        self.destino = destino  # Estación de destino
        self.tiempo = tiempo  # Tiempo de viaje entre las estaciones

class SistemaRutas:
    """Sistema que gestiona las rutas y busca caminos óptimos entre estaciones utilizando reglas lógicas."""
    def __init__(self):
        self.rutas = []  # Lista para almacenar las rutas disponibles

    def agregar_ruta(self, origen, destino, tiempo):
        """Agrega una ruta al sistema."""
        self.rutas.append(Ruta(origen, destino, tiempo))
    
    def encontrar_rutas(self, origen, destino):
        """Encuentra todas las rutas posibles entre dos estaciones, permitiendo múltiples combinaciones."""
        todas_rutas = []
        self._buscar_rutas(origen, destino, [], 0, todas_rutas)
        return todas_rutas
    
    def encontrar_mejor_ruta(self, origen, destino):
        """Encuentra la mejor ruta entre dos estaciones aplicando reglas lógicas y verifica rutas alternativas si no hay conexión directa."""
        todas_rutas = self.encontrar_rutas(origen, destino)
        
        if not todas_rutas:
            # Intentar encontrar rutas alternativas a través de estaciones intermedias
            estaciones_intermedias = {r.origen for r in self.rutas} | {r.destino for r in self.rutas}
            for estacion in estaciones_intermedias:
                if estacion != origen and estacion != destino:
                    ruta_parcial1 = self.encontrar_rutas(origen, estacion)
                    ruta_parcial2 = self.encontrar_rutas(estacion, destino)
                    if ruta_parcial1 and ruta_parcial2:
                        mejor_parcial1 = min(ruta_parcial1, key=lambda x: x[0])
                        mejor_parcial2 = min(ruta_parcial2, key=lambda x: x[0])
                        mejor_ruta_alternativa = (mejor_parcial1[0] + mejor_parcial2[0], mejor_parcial1[1] + mejor_parcial2[1][1:])
                        return mejor_ruta_alternativa
            return None, None
        
        # Aplicación de reglas lógicas para elegir la mejor ruta
        mejor_ruta = min(todas_rutas, key=lambda x: x[0])  # Regla: elegir la ruta con menor tiempo
        return mejor_ruta
    
    def _buscar_rutas(self, origen, destino, ruta_actual, tiempo_acumulado, todas_rutas):
        """Busca rutas recursivamente y almacena aquellas que conectan el origen con el destino."""
        if origen == destino:
            todas_rutas.append((tiempo_acumulado, ruta_actual + [destino]))  # Guardar la ruta encontrada
            return
        
        for ruta in self.rutas:
            if ruta.origen == origen and ruta.destino not in ruta_actual:
                # Regla: evitar ciclos en la ruta
                self._buscar_rutas(
                    ruta.destino, destino, ruta_actual + [origen], tiempo_acumulado + ruta.tiempo, todas_rutas
                )

# Crear el sistema y agregar rutas con tiempos únicos
sistema = SistemaRutas()
sistema.agregar_ruta("A", "B", 12)
sistema.agregar_ruta("B", "C", 18)
sistema.agregar_ruta("A", "D", 22)
sistema.agregar_ruta("D", "C", 14)
sistema.agregar_ruta("B", "E", 7)
sistema.agregar_ruta("E", "C", 13)
sistema.agregar_ruta("A", "F", 27)
sistema.agregar_ruta("F", "C", 16)
sistema.agregar_ruta("B", "G", 9)
sistema.agregar_ruta("G", "C", 15)
sistema.agregar_ruta("F", "E", 10)
sistema.agregar_ruta("E", "B", 5)
sistema.agregar_ruta("F", "B", 5)
sistema.agregar_ruta("C", "F", 14)
sistema.agregar_ruta("D", "F", 11)
sistema.agregar_ruta("G", "F", 8)
sistema.agregar_ruta("E", "D", 12)
sistema.agregar_ruta("G", "B", 6)

# Buscar todas las rutas entre F y B
todas_rutas = sistema.encontrar_rutas("A", "C")
if todas_rutas:
    todas_rutas.sort()  # Ordenar las rutas por tiempo total ascendente
    print("Rutas encontradas:")
    for tiempo, ruta in todas_rutas:
        print(f"{' -> '.join(ruta)} con un tiempo total de {tiempo} minutos")
else:
    estaciones_disponibles = {r.origen for r in sistema.rutas} | {r.destino for r in sistema.rutas}
    print(f"No se encontró una ruta válida. Estaciones disponibles: {', '.join(estaciones_disponibles)}")

# Buscar la mejor ruta entre F y B aplicando reglas lógicas
mejor_tiempo, mejor_ruta = sistema.encontrar_mejor_ruta("A", "C")
if mejor_ruta:
    print(f"\nLa mejor ruta desde A hasta C es: {' -> '.join(mejor_ruta)} con un tiempo total de {mejor_tiempo} minutos")
else:
    estaciones_disponibles = {r.origen for r in sistema.rutas} | {r.destino for r in sistema.rutas}
    print(f"No se encontró una ruta válida. Estaciones disponibles: {', '.join(estaciones_disponibles)}")
