from Arbitro_IAsistente import Arbitro_IAsistente as Arbitro
import tkinter as tk
from tkinter import messagebox

def interpretar(balon,origen,posicion,interfirio,intencionalidad,intebalon,ocasion,pomanos,accion,zonacampo,cofisico,
                actuacion,portero,preamones,faltas):
    
    # Construimos los hechos a partir de las entradas dadas por el usuario
    hechos_jugada = {
    'balon_en_juego': balon,
    'origen_jugada': origen,
    'posicion_penultimo_rival': posicion,
    'interfirio_jugada': interfirio,
    'intencionalidad': intencionalidad,
    'intento_jugar_balon' : intebalon,
    'ocasion_gol': ocasion,
    'posicion_natural_manos': pomanos,
    'accion': accion,
    'zona_campo': zonacampo,
    'contacto_fisico': cofisico,
    'actuacion_jugada': actuacion,
    'portero': portero,
    'previamente_amonestado': preamones,
    'faltas': faltas,
    'sancionado': False, # Hechos intermedios
    'jugada_previa': False, # Hechos intermedios
    'penal': False, # Hechos intermedios
    'infraccion': None # Hechos intermedios
}
    
    # Generamos una instancia del árbitro
    arbitro_central = Arbitro(hechos_jugada)
    
    # Llamamos a su método para interpretar los hechos de la jugada
    decisiones = arbitro_central.decision_arbitral()
    
    # Cadena de texto que vamos a mostrar al usuario para que saber que decisión se tomó
    interpretaciones = ""
    for decision in decisiones:
        # Construimos el texto a mostrar en base a las decisiones obtenidas
        interpretaciones+= decision[0] + "\n"
        interpretaciones+= decision[1] + "\n\n"
        
    # Le mostramos al usuario la decisión arbitral obtenida
    messagebox.showinfo("Decision árbitral", interpretaciones)

def main():
    ventana = tk.Tk()
    ventana.title("Árbitro IAsistente")
    ventana.geometry("500x700")
    marco = tk.Frame(ventana)
    marco.pack()

    balon_en_juego = tk.StringVar()
    origen_jugada = tk.StringVar()
    posicion_penultimo_rival = tk.StringVar()
    interfirio_jugada = tk.StringVar()
    intencionalidad = tk.StringVar()
    intento_jugar_balon = tk.StringVar()
    ocasion_gol = tk.StringVar()
    posicion_natural_manos = tk.StringVar()
    accion = tk.StringVar()
    zona_campo = tk.StringVar()
    contacto_fisico = tk.StringVar()
    actuacion_jugada = tk.StringVar()
    portero = tk.StringVar()
    previamente_amonestado = tk.StringVar()
    faltas = tk.StringVar()

    tk.Checkbutton(ventana, text="El balón estaba en juego", variable=balon_en_juego, onvalue="Si", offvalue="No").pack()

    pase = ['Pase companero', 'Pase rival', 'Saque de banda', 'Saque de meta', 'Saque de esquina']

    tk.Label(ventana, text="Origen de la jugada", font=("Consolas", 10)).pack(pady=5)
    origen_jugada.set("Pase rival")
    tk.OptionMenu(ventana, origen_jugada, *pase).pack()

    posicion = ['Adelante', 'Atras']

    tk.Label(ventana, text="Posición del jugador respecto al penultimo rival", font=("Consolas", 10)).pack(pady=5)
    posicion_penultimo_rival.set("Atras")
    tk.OptionMenu(ventana, posicion_penultimo_rival, *posicion).pack()

    tk.Checkbutton(ventana, text="Interfirió en la jugada", variable=interfirio_jugada, onvalue="Si", offvalue="No").pack()
    tk.Checkbutton(ventana, text="Hizo la falta con intención", variable=intencionalidad, onvalue="Si", offvalue="No").pack()
    tk.Checkbutton(ventana, text="Intento jugar el balón", variable=intento_jugar_balon, onvalue="Si", offvalue="No").pack()
    tk.Checkbutton(ventana, text="Era una clara ocasión de gol para el rival", variable=ocasion_gol, onvalue="Si", offvalue="No").pack()
    tk.Checkbutton(ventana, text="Las manos están en una posición natural", variable=posicion_natural_manos, onvalue="Si", offvalue="No").pack()
    tk.Checkbutton(ventana, text="Hubo contacto físico", variable=contacto_fisico, onvalue="Si", offvalue="No").pack()

    acciones = ['Empuja', 'Carga sobre el rival', 'Patada', 'Sujeta', 'Golpea', 'Disputa el balon',
                'Zancadilla', 'Toca el balon con la mano', 'Obstaculiza al rival', 'Muerde', 'Escupe',
                'Lanza un objeto contra el balon/adversario', 'Juega de forma peligrosa',
                'Comportamiento ofensivo/insultante o humillante', 'Ofensas verbales',
                'Impide que el arquero saque el balon', 'Retrasa la reanudación del juego',
                'Entra o vuelve al terreno de manera deliberada', 'Entra en el area del VAR', 'Repite el gesto del VAR',
                'Simula una falta', 'Muestra  falta de respeto al espiritu del futbol',
                'Intenta burlar alguna regla del reglamento', 'Pide tarjetas con gestos exagerados',
                'Procede de manera provocativa', 'Lanza un objeto al terreno de juego', 'Utiliza dispositivos no autorizados']

    tk.Label(ventana, text="Acción realizada", font=("Consolas", 10)).pack(pady=5)
    accion.set("Empuja")
    tk.OptionMenu(ventana, accion, *acciones).pack()

    campo = ['Area penal jugador', 'Area penal rival', 'Medio campo jugador', 'Medio campo rival']

    tk.Label(ventana, text="Zona del campo", font=("Consolas", 10)).pack(pady=5)
    zona_campo.set("Medio campo jugador")
    tk.OptionMenu(ventana, zona_campo, *campo).pack()

    actuacion = ['Falta de atencion', 'Dano fisico leve', 'Uso excesivo de fuerza']

    tk.Label(ventana, text="Actuación de la jugada", font=("Consolas", 10)).pack(pady=5)
    actuacion_jugada.set("Falta de atencion")
    tk.OptionMenu(ventana, actuacion_jugada, *actuacion).pack()

    tk.Checkbutton(ventana, text="El jugador es el portero", variable=portero, onvalue="Si", offvalue="No").pack()

    tk.Checkbutton(ventana, text="Estaba amonestado previamente", variable=previamente_amonestado, onvalue="Si", offvalue="No").pack()

    tk.Label(ventana, text="Cuántas faltas lleva el jugador", font=("Consolas", 10)).pack(pady=5)
    faltas.set("0")
    tk.Entry(ventana, textvariable=faltas).pack()

    tk.Button(ventana, text="Interpretar", font=("Consolas", 16), background="blue",
            foreground="white", command=lambda: interpretar(balon_en_juego.get(),origen_jugada.get(),
            posicion_penultimo_rival.get(),interfirio_jugada.get(),intencionalidad.get(),
            intento_jugar_balon.get(),ocasion_gol.get(),posicion_natural_manos.get(),
            accion.get(),zona_campo.get(),contacto_fisico.get(),actuacion_jugada.get(),
            portero.get(),previamente_amonestado.get(),int(faltas.get()))).pack(pady=20)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()