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

tabla = {
    '1': [0],
    '2': [908,0],
    '3': [117,515,0],
    '4': [687,448,886,0],
    '5': [1651,970,1373,922,0],
    '6': [117,791,999,804,1540,0],
    '7': [1882,1013,117,1404,1191,1765,0],
    '8': [1310,441,844,832,529,1193,662,0],
    '9': [889,246,684,202,720,840,1202,630,0],
    '10': [760,181,559,479,997,643,1194,622,277,0],
    '11': [2348,1707,1811,1619,697,2237,694,1223,1417,1694,0],
    '12': [782,127,541,426,943,665,1140,568,223,54,1640,0],
    '13': [697,546,984,98,952,814,1502,930,300,577,1649,523,0],
    '14': [1370,928,317,1319,1463,1253,1154,934,1117,774,1848,756,1417,0],
    '15': [1431,750,1153,702,220,1320,971,309,500,777,917,723,732,1250,0],
    '16': [395,513,721,744,1262,278,1407,915,542,365,1959,387,842,975,1042,0],
    '17': [697,316,739,504,1022,580,1329,757,302,180,1719,202,602,954,802,302,0],
    '18': [1328,600,291,991,1148,1211,826,606,789,729,1520,711,1089,328,928,933,913,0],
    '19': [490,540,626,817,1335,373,1553,981,615,392,2032,414,915,890,1115,95,397,960,0],
    '20': [481,636,813,867,1385,364,1610,1038,665,480,2082,510,965,1077,1165,123,425,1056,187,0],
    '21': [1244,511,300,902,1046,1127,737,517,700,664,1431,646,1000,417,826,849,844,89,895,972,0],
    '22': [810,171,344,542,1029,693,1072,500,340,215,1766,197,640,559,809,416,395,514,446,538,449,0],
    '23': [881,572,235,943,1430,764,1352,901,741,616,2046,598,1041,499,1210,486,796,526,391,578,615,401,0],
    '24': [1145,460,898,416,506,1034,1257,595,214,491,1203,437,446,1331,286,756,516,1003,829,879,914,554,955,0],
    '25': [513,631,780,862,1380,396,1605,1033,660,483,2077,505,960,1044,1160,118,420,1051,154,33,967,533,545,874,0],
    '26': [461,497,704,678,1195,344,1432,938,476,349,1893,371,776,1041,976,66,236,898,161,189,852,360,552,690,184,0],
    '27': [1407,538,642,929,784,1290,475,255,727,719,1169,665,1027,679,564,1012,854,351,1043,1135,262,597,877,850,1130,957,0],
    '28': [1000,131,534,522,839,883,882,310,320,312,1576,258,620,797,619,605,447,469,636,728,380,190,591,534,723,550,407,0]
}

def obtener_heuristica(tabla,nodo_origen,nodo_destino):
    # Si el nodo al que queremos llegar es mayor al nodo donde estamos
    if int(nodo_destino) > int(nodo_origen):
        # Tomamos el valor del renglon del nodo destino
        heuristica = tabla[nodo_destino][int(nodo_origen)-1]
    # Caso contrario
    else:
        # Tomamos el valor del nodo en el que estamos
        heuristica = tabla[nodo_origen][int(nodo_destino)-1]
    return heuristica

def busqueda_escalada_maxima_pendiente(grafo,tabla,nodo_inicial,nodo_final,sentido):
    nodo_actual = nodo_inicial
    ruta = [nodo_inicial]
    nodo_meta = False
    heuristica_actual = obtener_heuristica(tabla,nodo_actual,nodo_final)

    while not nodo_meta:
        print(f"\nNodo {nodo_actual} visitado heuristica {heuristica_actual} \n")

        if(nodo_actual == nodo_final):
            nodo_meta = True
            break

        hijos = grafo[nodo_actual]

        if sentido == 'antihorario':
            hijos = reversed(grafo[nodo_actual])

        mejor_hijo = None
        mejor_heuristica = heuristica_actual

        for hijo in hijos:
            heuristica_hijo = obtener_heuristica(tabla,hijo[0],nodo_final)
            print(f"PADRE {nodo_actual}  Nodo {hijo[0]} heuristica {heuristica_hijo}")
            # En caso de que el proximo nodo tenga un mejor valor heuristico lo almacenamos en mejor_hijo
            # y actualizamos el valor heuristico por el del hijo para compararlo con los demás hijos
            if(heuristica_hijo <= mejor_heuristica):
                mejor_hijo = hijo[0]
                mejor_heuristica = heuristica_hijo

        #Si existe un hijo con mejor valor heuristico, lo convertimos en el nodo actual
        if mejor_hijo:
            nodo_actual = mejor_hijo
            ruta.append(nodo_actual)
            heuristica_actual = mejor_heuristica
        # Si no, abandonamos la búsqueda
        else:
            print("\nNO HAY UN MEJOR NODO")
            break
        
    print("\nRuta ", ruta)
    input("Presione ENTER para salir")

nodo_inicio = input("Digite el nodo inicial : ")
nodo_fin = input("Digite el nodo final : ")
direccion = input("Digite el sentido : ")
busqueda_escalada_maxima_pendiente(grafo,tabla,nodo_inicio,nodo_fin,direccion)