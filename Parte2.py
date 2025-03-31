        

# Regla principal: Seleccionar la ruta con menor tiempo de viaje
        mejor_ruta = min(todas_rutas, key=lambda x: x[0])
        return mejor_ruta
    
    def _buscar_rutas(self, origen, destino, ruta_actual, tiempo_acumulado, todas_rutas):
        """Busca rutas recursivamente y almacena aquellas que conectan el origen con el destino, evitando ciclos."""
        if origen == destino:
            todas_rutas.append((tiempo_acumulado, ruta_actual + [destino]))  # Guardar la ruta encontrada
            return
        
        for ruta in self.rutas:
            if ruta.origen == origen and ruta.destino not in ruta_actual:
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
