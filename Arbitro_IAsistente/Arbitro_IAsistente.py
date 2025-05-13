class Arbitro_IAsistente:

    # 'jugada_previa', 'infracción', 'penal' son hechos intermedios para evaluar la decisión final y la amonestación
    # estos me ayudan a generar el encadenamiento hacía adelante que utilizan los tiros libres directos, tiro penal
    # así como para conocer la amonestación que necesitan

    # 'sancionado' es un hecho intermedio que se genera cuando se amonesta alguna infracción o acción para saber
    # si debe ser expulsado por doble amarilla 
    def __init__(self,hechos_jugada):
        self.hechos = hechos_jugada
        self.decisiones = []

    def decision_arbitral(self):
        # Lista de las decisiones obtenidas por la interpretación del árbitro
        reglas = [
            self.fuera_lugar_sancionable(),
            self.fuera_lugar_sancionable1(),
            self.fuera_lugar_no_sancionable2(),
            self.fuera_lugar_no_sancionable3(),
            self.infraccion_contacto_fisico(),
            self.infraccion_escupir(),
            self.infraccion_lanzar_objeto(),
            self.infraccion_mano_voluntaria(),
            self.infraccion_mano_antinatural(),
            self.tiro_penal_libredirecto(),
            self.tiro_penal_mano(),
            self.tiro_libre_directo(),
            self.tiro_libre_indirecto(),
            self.tiro_libre_indirecto_portero(),
            self.roja_ocasion_gol(),
            self.amarilla_libre_directo_fuera_areapenal(),
            self.amarilla_acciones(),
            self.roja_penal_intenta_jugar_balon(),
            self.roja_penal_nointenta_jugar_balon(),
            self.roja_juego_brusco(),
            self.roja_juego_brusco_sinbalon(),
            self.amarilla_temeraria(),
            self.roja_doble_amarilla(),
            self.amarilla_reiteracion_faltas(),
            self.advertencia()
        ]

        # Recorrido de cada regla haciendo llamado a su función / interpretación
        for regla in reglas:
            resultado = regla
            if resultado:
                # Recolección de las decisiones tomadas
                self.decisiones.append(resultado)

        return self.decisiones

    # Fuera de lugar por interferir en la jugada
    def fuera_lugar_sancionable(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and 
            h['zona_campo'] in ['Medio campo rival', 'Area penal rival'] and 
            h['origen_jugada'] == 'Pase companero' and 
            h['posicion_penultimo_rival'] == 'Adelante' and 
            h['interfirio_jugada'] == 'Si'):
                h['jugada_previa'] = True
                return ("Tiro libre indirecto por fuera de lugar",
                "Regla 11 constituye una infracción si un jugador en posición adelante al penúltimo rival interfiere en la jugada")
    
    # Fuera de lugar por hacer por el balón
    def fuera_lugar_sancionable1(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and 
            h['zona_campo'] in ['Medio campo rival', 'Area penal rival'] and 
            h['origen_jugada'] == 'Pase companero' and 
            h['posicion_penultimo_rival'] == 'Adelante' and 
            h['intento_jugar_balon'] == 'Si'):
                h['jugada_previa'] = True
                return ("Tiro libre indirecto por fuera de lugar",
                "Regla 11 constituye una infracción si un jugador en posición adelante al penúltimo rival intenta sacar ventaja de su posición")
    
    # Fuera de lugar no sancionable por no interferir en la jugada
    def fuera_lugar_no_sancionable2(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and 
            h['zona_campo'] in ['Medio campo rival', 'Area penal rival'] and 
            h['origen_jugada'] == 'Pase companero' and 
            h['posicion_penultimo_rival'] == 'Adelante' and 
            h['interfirio_jugada'] == 'No' and
            h['inteto_jugar_balon'] == 'No'):
                h['jugada_previa'] = True
                return ("No hay fuera de lugar",
                "Regla 11 no constituye una infracción si un jugador en posición adelante al penúltimo rival no interfiere en la jugada y no hace por el balon")
    
    # Fuera de lugar no sancionable por el origen de la jugada
    def fuera_lugar_no_sancionable3(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and 
            h['zona_campo'] in ['Medio campo rival', 'Area penal rival'] and 
            h['origen_jugada'] in ['Pase rival', 'Saque de meta', 'Saque de esquina', 'Saque de banda'] and 
            h['posicion_penultimo_rival'] == 'Adelante'):
                h['jugada_previa'] = False
                return ("No hay fuera de lugar",
                "Regla 11 no constituye una infracción si un jugador en posición adelante al penúltimo rival recibe el balón del pase de un rival, una saque de banda, meta o esquina")
    
    # Hecho intermedio, libre directo por contacto fisico y acción imprudente, temeraria o con uso excesivo de fuerza    
    def infraccion_contacto_fisico(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['contacto_fisico'] == 'Si' and
           h['actuacion_jugada'] in ['Falta de atencion', 'Dano fisico leve', 'Uso excesivo de fuerza'] and
           h['accion'] in ['Empuja', 'Carga sobre el rival', 'Patada', 'Golpea', 'Disputa el balon', 'Obstaculiza al rival', 'Muerde', 'Sujeta']):
                h['infraccion'] = 'libre directo'
                return None
    
    # Hecho intermedio, libre directo por escupir
    def infraccion_escupir(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['contacto_fisico'] == 'No' and
           h['accion'] == 'Escupe'):
                h['infraccion'] = 'libre directo'
                return None

    # Hecho intermedio, libre directo por lanzar un objeto vs rival
    def infraccion_lanzar_objeto(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['contacto_fisico'] == 'No' and
           h['accion'] == 'Lanza un objeto contra el balon/adversario'):
                h['infraccion'] = 'libre directo'
                return None
    
    # Hecho intermedio, libre directo por mano voluntaria jugador
    def infraccion_mano_voluntaria(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['intencionalidad'] == 'Si' and
           h['accion'] == 'Toca el balon con la mano'):
                h['infraccion'] = 'mano'
                return None
    
    # Hecho intermedio, libre directo por mano antinatural jugador
    def infraccion_mano_antinatural(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['accion'] == 'Toca el balon con la mano' and
           h['posicion_natural_manos'] == 'No'):
                h['infraccion'] = 'mano'
                return None
    
    # Hecho final, tiro penal
    def tiro_penal_libredirecto(self):
        h = self.hechos
        if (h['infraccion'] == 'libre directo' and
           h['zona_campo'] == 'Area penal jugador'):
                h['penal'] = True
                return ("Tiro penal para el rival",
                "Regla 13 se sancionara con tiro penal al jugador que cometa un libre directo dentro de su área penal sobre un adversario")            
    
    # Hecho final, tiro penal por mano
    def tiro_penal_mano(self):
        h = self.hechos
        if (h['infraccion'] == 'mano' and
           h['zona_campo'] == 'Area penal jugador'):
                h['penal'] = True
                return ("Tiro penal para el rival",
                "Regla 12 y 13 se sancionara con tiro penal al jugador que toque el balón con la mano en una posición antinatural o de forma deliberada dentro del area penal del jugador")
        
    # Hecho final, tiro libre directo puro
    def tiro_libre_directo(self):
        h = self.hechos
        if (h['infraccion'] == 'libre directo' and
           h['zona_campo'] in ['Area penal rival', 'Medio campo rival', 'Medio campo jugador']):
                h['penal'] = False
                return ("Tiro libre directo para el rival",
                "Regla 12 se sancionará con tiro libre directo la acción de empujar, escupir, hacer una zancadilla, morder, sujetar o hacer cualquier otro tipo de contacto físico contra el adversario")
        
    # Tiro libre indirecto puro
    def tiro_libre_indirecto(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['contacto_fisico'] == 'No' and
           h['accion'] in ['Obstaculiza al rival', 'Juega de forma peligrosa', 'Ofensas verbales', 'Comportamiento ofensivo/insultante o humillante', 'Intenta burlar alguna regla del reglamento', 'Impide que el portero saque el balon']):
                return ("Tiro libre indirecto para el rival",
                "Regla 12 se sancionará con tiro libre indirecto a toda acción de tipo verbal como lo es juego peligroso, impedir el saque del portero, obstaculizar el avance de un rival sin contacto fisico. etc.")
        
    # Tiro libre indirecto por mano del portero en area penal
    def tiro_libre_indirecto_portero(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'Si' and
           h['jugada_previa'] is False and
           h['zona_campo'] == 'Area penal jugador' and
           h['origen_jugada'] == 'Pase companero' and 
           h['accion'] == 'Toca el balon con la mano' and
           h['portero'] == 'Si'):
                return ("Tiro libre indirecto para el rival",
                "Regla 12 se sancionará con tiro libre indirecto si el portero toca deliberadamente con las manos el balón dentro de su área penal despues del pase deliberado de un compañero")
        
    # Tarjeta roja por ocasion clara de gol
    def roja_ocasion_gol(self):
        h = self.hechos
        if (h['infraccion'] == 'mano' and
           h['ocasion_gol'] == 'Si'):
                return ("Tarjeta roja directa",
                "Evitar una ocasión manifiesta de gol con infracción por mano")
    
    # Tarjeta amarilla por tiros libres directos con intencion imprudente
    def amarilla_libre_directo_fuera_areapenal(self):
        h = self.hechos
        if (h['infraccion'] == 'libre directo' and
            h['actuacion_jugada'] == 'Dano fisico leve'):
              h['sancionado'] = True
              return ("Tarjeta amarilla",
                "Ocasionar un tiro libre directo con una accion temeraria")
        
    # Tarjeta amarilla por acciones que ameritan amonestacion según el reglamento
    def amarilla_acciones(self):
        h = self.hechos
        if (h['accion'] in ['Retrasa la reanudación del juego', 'Entra o vuelve al terreno de manera deliberada',
            'Repite el gesto del VAR', 'Simula una falta', 'Muestra falta de respeto al espíritu del fútbol',
            'Intenta burlar alguna regla del reglamento', 'Pide tarjetas con gestos exagerados']):
              h['sancionado'] = True
              return ("Tarjeta amarilla",
                f"{h['accion']}")
        
    # Tarjeta amarilla por marcacion de penal pero intención de jugar balon
    def roja_penal_intenta_jugar_balon(self):
        h = self.hechos
        if (h['penal'] and
            h['intento_jugar_balon'] == 'Si'):
                h['sancionado'] = True
                return ("Tarjeta amarilla",
                "Si ya se marco penal y el jugador intento jugar el balón, es motivo de tarjeta amarilla")

    # Tarjeta roja por marcacion de penal sin intención de jugar balon
    def roja_penal_nointenta_jugar_balon(self):
        h = self.hechos
        if (h['penal'] and
            h['intento_jugar_balon'] == 'No'):
                return ("Tarjeta roja directa",
                "Si se marco penal pero el jugador no intento jugar el balon es roja directa")

    # Tarjeta roja por juego brusco
    def roja_juego_brusco(self):
        h = self.hechos
        if (h['infraccion'] == 'libre directo' and
           h['actuacion_jugada'] == 'Uso excesivo de fuerza'):
                return ("Tarjeta roja directa",
                "Juego brusco")
        
    def roja_juego_brusco_sinbalon(self):
        h = self.hechos
        if (h['balon_en_juego'] == 'No' and
            h['actuacion_jugada'] == 'Uso excesivo de fuerza' and
            h['accion'] in ['Golpea', 'Muerde', 'Patada',] and
            h['actuacion_jugada'] == 'Uso excesivo de fuerza'):
                return ("Tarjeta roja directa",
                "Conducta violenta")
    
    # Tarjeta amarilla por interrumpir avance rival con mano
    def amarilla_temeraria(self):
        h = self.hechos
        if (h['infraccion'] == 'mano' and
           h['ocasion_gol'] == 'No'):
                h['sancionado'] = True
                return ("Tarjeta amarilla",
                "Cortar avance del equipo rival con infraccion por mano")
        
    # Tarjeta amarilla por recurrencia en infraccion
    def amarilla_reiteracion_faltas(self):
        h = self.hechos
        if (h['actuacion_jugada'] == 'Falta de atencion' and
           h['sancionado'] is False and
           h['faltas'] > 3):
                h['sancionado'] = True
                return ("Tarjeta amarilla",
                "Infringir reiteradamente las Reglas del Juego")
        
    # Tarjeta roja por doble amarilla
    def roja_doble_amarilla(self):
        h = self.hechos
        if (h['previamente_amonestado'] == 'Si' and
           h['sancionado']):
                return ("Tarjeta roja",
                "Tarjeta roja por doble amarilla")
    
    # Advertencia por faltan imprudente
    def advertencia(self):
        h = self.hechos
        if (h['actuacion_jugada'] == 'Falta de atencion' and
           h['sancionado'] is False and
           h['faltas'] < 4):
                return ("Llamada de atención sin sanciones",
                "Apercibimiento")