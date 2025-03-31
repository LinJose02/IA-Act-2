class Ruta:
    """Clase que representa una conexión entre estaciones y su tiempo de viaje."""
    def __init__(self, origen, destino, tiempo):
        self.origen = origen  # Estación de origen
        self.destino = destino  # Estación de destino
        self.tiempo = tiempo  # Tiempo de viaje entre las estaciones

class SistemaRutas:
    """Sistema que gestiona las rutas y busca caminos óptimos entre estaciones utilizando reglas lógicas explícitas."""
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
        """Encuentra la mejor ruta aplicando reglas lógicas y verificando rutas alternativas si es necesario."""
        todas_rutas = self.encontrar_rutas(origen, destino)
        
        if not todas_rutas:
            # Regla de fallback: Intentar rutas alternativas usando estaciones intermedias
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