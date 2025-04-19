from collections import deque

grafo = {
    '1' : [('6',117),('13',699),('4',701)],
    '2' : [('22',171),('12',137),('9',245)],
    '3' : [('14',317),('23',235),('19',638),('18',291)],
    '4' : [('9',202),('1',701),('13',98)],
    '5' : [('15',220),('11',705)],
    '6' : [('16',288),('1',117)],
    '7' : [('27',475),('8',662),('11',696)],
    '8' : [('27',268),('15',309),('7',662),],
    '9' : [('28',320),('2',245),('17',321),('4',202),('24',214)],
    '10' : [('16',381),('12',54)],
    '11' : [('7',696),('5',705)],
    '12' : [('10',54),('2',137)],
    '13' : [('4',98),('1',699),('24',446)],
    '14' : [('23',499),('3',317)],
    '15' : [('8',309),('24',286),('5',220)],
    '16' : [('19',95),('25',118),('20',123),('6',288),('26',66),('10',381)],
    '17' : [('26',259),('9',321)],
    '18' : [('14',328),('3',291),('21',89)],
    '19' : [('23',391),('16',95),('3',638)],
    '20' : [('25',33,),('16',123)],
    '21' : [('18',89),('22',499),('28',380),('27',262)],
    '22' : [('21',449),('23',401),('2',171),('28',190)],
    '23' : [('14',499),('19',391),('22',401),('3',235)],
    '24' : [('9',214),('13',446),('15',286)],
    '25' : [],
    '26' : [('16',66),('17',259)],
    '27' : [('21',262),('28',390),('8',268),('7',475)],
    '28' : [('27',390),('21',380),('22',190),('2',131),('9',320),('8',310)]
}

def busqueda_anchura(grafo,nodo_inicial,nodo_final,sentido):
    cola = deque([nodo_inicial])
    visitados = set()
    padres = {}
    nodo_meta = False

    # Mientras no alcancemos el nodo meta y haya elementos en la cola, realizamos la búsqueda 
    while(not(nodo_meta) and cola):
        print("cola ", list(cola))
        nodo_visitado = cola.popleft() # Elminamos el primer elemento de la cola FIFO
        visitados.add(nodo_visitado)
        print(nodo_visitado, "visitado")

        if(nodo_visitado == nodo_final):
            nodo_meta = True
        else:
            hijos = grafo[nodo_visitado]
            # Si es sentido antihorario, invertimos el orden de los nodos hijos
            if sentido == 'antihorario':
                hijos = reversed(grafo[nodo_visitado])
            
            for hijo in hijos:
                if hijo[0] not in visitados and hijo[0] not in cola:
                    cola.append(hijo[0])
                    padres[hijo[0]] = nodo_visitado # Colocamos el origen del nodo agregado a la cola
                    
    if(nodo_meta):
        ruta = [nodo_final] 
        while ruta[-1] != nodo_inicial: # Hasta alcanzar el nodo inicial en la ruta
            ruta.append(padres[ruta[-1]]) # Agregamos el padre del ultimo nodo en la ruta
        ruta.reverse() # Invertimos el orden para mostrar la ruta desde nodo_inicio->nodo_final 
        print("\nRuta ", ruta)
    else:
        print("No hay ruta existente")

busqueda_anchura(grafo,'14','25','horario')