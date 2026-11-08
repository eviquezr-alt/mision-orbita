ENERGIA_ANALIZAR_TERRENO = 8
ENERGIA_RECOLECTAR_MUESTRA = 12
ENERGIA_REALIZAR_OBSERVACION = 5
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_ANALIZAR_TERRENO = 10
PUNTOS_RECOLECTAR_MUESTRA = 20
PUNTOS_REALIZAR_OBSERVACION = 8

energia_disponible = int(input("Energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Provisiones disponibles al llegar al destino: "))

puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

seguir_explorando = True

while seguir_explorando:
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una actividad: "))

    if opcion == 1:
        if energia_disponible >= ENERGIA_ANALIZAR_TERRENO:
            energia_disponible = energia_disponible - ENERGIA_ANALIZAR_TERRENO
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR_TERRENO
            print("Actividad realizada: Analizar terreno. Puntos obtenidos:", PUNTOS_ANALIZAR_TERRENO)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            seguir_explorando = False
    elif opcion == 2:
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
        print("Exploración finalizada por la tripulación.")
        seguir_explorando = False
    else:
        print("Opción no válida.")

print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible, "unidades")
print("Provisiones restantes:", provisiones_disponibles, "unidades")