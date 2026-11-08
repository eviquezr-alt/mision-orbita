# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Esteban Víquez Rodríguez
# Fecha: 08/11/2026        Versión: 1.0
# Descripción: Simula las actividades de exploración en el destino
#              con un menú que se repite y suma puntos científicos.
# ============================================================

# Constantes: lo que gasta y lo que gana cada actividad.
# Están en mayúscula porque no cambian durante el programa.
ENERGIA_ANALIZAR_TERRENO = 8
ENERGIA_RECOLECTAR_MUESTRA = 12
ENERGIA_REALIZAR_OBSERVACION = 5
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_ANALIZAR_TERRENO = 10
PUNTOS_RECOLECTAR_MUESTRA = 20
PUNTOS_REALIZAR_OBSERVACION = 8

# Entradas: los recursos con los que la nave llega al destino.
energia_disponible = int(input("Energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Provisiones disponibles al llegar al destino: "))

# Acumulador y contadores empiezan en 0 porque todavía no se ha hecho nada.
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

# Variable de control: mientras sea True el menú se sigue repitiendo.
seguir_explorando = True

while seguir_explorando:
    # El menú se muestra en cada vuelta para que la tripulación elija.
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una actividad: "))

    if opcion == 1:
        # Se revisa primero si alcanza la energía para no quedar en negativo.
        if energia_disponible >= ENERGIA_ANALIZAR_TERRENO:
            energia_disponible = energia_disponible - ENERGIA_ANALIZAR_TERRENO
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR_TERRENO
            print("Actividad realizada: Analizar terreno. Puntos obtenidos:", PUNTOS_ANALIZAR_TERRENO)
        else:
            # Si no alcanza, el enunciado pide terminar la exploración.
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            seguir_explorando = False
    elif opcion == 2:
        # Recolectar muestra gasta energía y provisiones, por eso se revisan las dos.
        if energia_disponible >= ENERGIA_RECOLECTAR_MUESTRA and provisiones_disponibles >= PROVISIONES_RECOLECTAR_MUESTRA:
            energia_disponible = energia_disponible - ENERGIA_RECOLECTAR_MUESTRA
            provisiones_disponibles = provisiones_disponibles - PROVISIONES_RECOLECTAR_MUESTRA
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas = muestras_recolectadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_RECOLECTAR_MUESTRA
            print("Actividad realizada: Recolectar muestra. Puntos obtenidos:", PUNTOS_RECOLECTAR_MUESTRA)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            seguir_explorando = False
    elif opcion == 3:
        if energia_disponible >= ENERGIA_REALIZAR_OBSERVACION:
            energia_disponible = energia_disponible - ENERGIA_REALIZAR_OBSERVACION
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_REALIZAR_OBSERVACION
            print("Actividad realizada: Realizar observación. Puntos obtenidos:", PUNTOS_REALIZAR_OBSERVACION)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            seguir_explorando = False
    elif opcion == 4:
        # La tripulación decide terminar: se cambia la variable de control para salir del ciclo.
        print("Exploración finalizada por la tripulación.")
        seguir_explorando = False
    else:
        # Cualquier otro número no existe en el menú; el ciclo sigue.
        print("Opción no válida.")

# Resumen final: se muestra una sola vez, después de salir del ciclo.
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible, "unidades")
print("Provisiones restantes:", provisiones_disponibles, "unidades")