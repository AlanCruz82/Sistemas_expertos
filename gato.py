import tkinter as tk
import random

# Variables del juego normal
jugadores = ["X", "O"]
jugador_actual = None
turnos = 0
final_juego = False
marcador_x = 0
marcador_o = 0
marcador_empates = 0

# Variables para modalidad contra computadora
primer_jugador = None
primer_turno = None
simbolo_maquina = None

tablero = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

def pintar_casilla(fila, columna):
    global jugador_actual, simbolo_maquina

    # Si ya gano algun jugador o la casilla seleccionada ya tiene un símbolo, regresamos sin pintar nada
    if final_juego or tablero[fila][columna]["text"] != "":
        return

    # Pintamos la casilla con el símbolo del jugador actual
    tablero[fila][columna]["text"] = jugador_actual

    # Revisamos si una vez establecido el símbolo el jugador_actual gana
    verificar_ganador()

    if not final_juego:
        # Cambiamos el turno para que juegue el siguiente símbolo
        jugador_actual = jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]
        encabezado["text"] = jugador_actual + " turno"

        # Si el jugador actual es la máquina, hacemos el movimento
        if jugador_actual == simbolo_maquina:
            ventana.after(500, movimiento_maquina)

def iniciar_juego(simbolo,turno):
    global jugador_actual, primer_jugador, primer_turno, simbolo_maquina, jugadores

    # Almacenamos el simbolo y turno con el que el usuario eligio jugar
    primer_jugador = simbolo
    primer_turno = turno
    jugador_actual = simbolo

    # Si seleccionaron que iniciara la computadora, guardamos el símbolo de la máquina y pintamos su jugada
    if turno == "computadora":
        simbolo_maquina = simbolo
        ventana.after(500, movimiento_maquina)
    # Si no, almacenamos el símbolo de la máquina (el opuesto al seleccionado)
    else:
        simbolo_maquina = jugadores[1] if simbolo == jugadores[0] else jugadores[0]
    
    encabezado.config(text=jugador_actual + " turno")

    ventana_inicio.destroy()
    ventana.deiconify()

def movimiento_maquina():
    global jugador_actual

    if final_juego:
        return

    # Almacenamos las posiciones disponibles en el tablero
    movimientos_disponibles = [(f, c) for f in range(3) for c in range(3) if tablero[f][c]["text"] == ""]
    if movimientos_disponibles:
        # Seleccionamos una posicion del tablero al azar
        fila, columna = random.choice(movimientos_disponibles)
        tablero[fila][columna]["text"] = jugador_actual
        verificar_ganador()

        if not final_juego:
            # Cambiamos de turno
            jugador_actual = jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]
            encabezado["text"] = jugador_actual + " turno"


def verificar_ganador():
    global turnos, final_juego, marcador_x, marcador_o, marcador_empates

    turnos += 1

    # Horizontal
    for fila in range(3):
        if tablero[fila][0]["text"] == tablero[fila][1]["text"] == tablero[fila][2]["text"] != "":
            marcar_ganador(tablero[fila][0]["text"])
            for columna in range(3):
                tablero[fila][columna].config(foreground="#3667a3", background="#a4deda")
            return

    # Vertical
    for columna in range(3):
        if (tablero[0][columna]["text"] == tablero[1][columna]["text"] == tablero[2][columna]["text"] != ""):
            marcar_ganador(tablero[0][columna]["text"])
            for fila in range(3):
                tablero[fila][columna].config(foreground="#3667a3", background="#a4deda")
            return

    # Diagonal \
    if (tablero[0][0]["text"] == tablero[1][1]["text"] == tablero[2][2]["text"] != ""):
        marcar_ganador(tablero[0][0]["text"])
        for i in range(3):
            tablero[i][i].config(foreground="#3667a3", background="#a4deda")
        return

    # Diagonal /
    if (tablero[0][2]["text"] == tablero[1][1]["text"] == tablero[2][0]["text"] != ""):
        marcar_ganador(tablero[0][2]["text"])
        tablero[0][2].config(foreground="#3667a3", background="#a4deda")
        tablero[1][1].config(foreground="#3667a3", background="#a4deda")
        tablero[2][0].config(foreground="#3667a3", background="#a4deda")
        return

    # Empate
    if turnos == 9:
        final_juego = True
        marcador_empates += 1
        encabezado.config(text="Empate", foreground="#3667a3")
        marcador_label.config(text=f"X: {marcador_x}   O: {marcador_o}   Empates: {marcador_empates}")

def marcar_ganador(jugador):
    global final_juego, marcador_x, marcador_o
    encabezado.config(text=jugador + " ganador", foreground="#3667a3")
    # Evaluamos el jugador que gano para incrementar el marcador
    if jugador == "X":
        marcador_x += 1
    else:
        marcador_o += 1
    final_juego = True
    marcador_label.config(text=f"X: {marcador_x}   O: {marcador_o}   Empates: {marcador_empates}")

def nuevo_juego():
    global turnos, final_juego, jugador_actual, primer_jugador, simbolo_maquina

    # Reestablecemos los valores de las variables globales
    turnos = 0
    final_juego = False
    # Simbolo elegido por el usuario al inicio
    jugador_actual = primer_jugador
    encabezado.config(text=jugador_actual + " turno", foreground="white")

    for fila in range(3):
        for columna in range(3):
            tablero[fila][columna].config(text="", foreground="#141414", background="#7acfcf")

    # Si se elegió en el inicio que la computadora iniciara el turno, volvemos a hacer el movimiento
    if jugador_actual == simbolo_maquina:
            ventana.after(500, movimiento_maquina)

# Ventana del juego
ventana = tk.Tk()
ventana.title("Gato")
ventana.geometry("500x600")
ventana.withdraw()
marco = tk.Frame(ventana)
marco.pack()

# Marcador del juego (primera fila)
marcador_label = tk.Label(marco, text="X: 0   O: 0   Empates: 0", font=("Consolas", 14),
                          background="#7acfcf", foreground="white")
marcador_label.grid(row=0, column=0, columnspan=3, sticky="we", pady=5)

# Encabezado del turno del juego (segunda fila)
encabezado = tk.Label(marco, text="", font=("Consolas", 20),
                      background="#7acfcf", foreground="white")
encabezado.grid(row=1, column=0, columnspan=3, sticky="we")

# Botones del tablero (apartir de la tercera fila)
for fila in range(3):
    for columna in range(3):
        tablero[fila][columna] = tk.Button(marco, text="", font=("Consolas", 50, "bold"),
                                           background="#7acfcf", foreground="#141414", width=4, height=1,
                                           command=lambda fila=fila, columna=columna: pintar_casilla(fila, columna))
        tablero[fila][columna].grid(row=fila+2, column=columna)

# Reinicio del juego / Nuevo juego
reiniciar = tk.Button(marco, text="Jugar de nuevo", font=("Consolas", 20), background="#7acfcf",
                      foreground="white", command=nuevo_juego)
reiniciar.grid(row=5, column=0, columnspan=3, sticky="we", pady=10)

# Ventana menú de elección de símbolo
ventana_inicio = tk.Toplevel(ventana)
ventana_inicio.geometry("500x550")

# Elección de símbolo (X O)
tk.Label(ventana_inicio, text="Elige tu símbolo", font=("Consolas", 16)).pack(pady=10)

simbolo_seleccionado = tk.StringVar()
simbolo_seleccionado.set("X")

opciones_simbolo = ["X", "O"]
tk.OptionMenu(ventana_inicio, simbolo_seleccionado, *opciones_simbolo).pack()

# Opciones de turno (yo o computadora)
tk.Label(ventana_inicio, text="¿Quién empieza?", font=("Consolas", 16)).pack(pady=10)
turno_seleccionado = tk.StringVar()
turno_seleccionado.set("computadora")

opciones_turno = ["yo", "computadora"]
tk.OptionMenu(ventana_inicio, turno_seleccionado, *opciones_turno).pack()

# Comenzamos y mostramos el tablero
tk.Button(ventana_inicio, text="Iniciar juego", font=("Consolas", 16), background="#7acfcf",
          foreground="white", command=lambda: iniciar_juego(simbolo_seleccionado.get(), turno_seleccionado.get())).pack(pady=20)

ventana.mainloop()