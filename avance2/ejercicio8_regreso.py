# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Esteban Víquez Rodríguez
# Fecha: 08/11/2026        Versión: 1.0
# Descripción: Decide si la nave puede regresar a la Tierra y
#              simula el regreso, o calcula cuántos días puede
#              sobrevivir la tripulación si queda varada.
# ============================================================

# Constantes: lo que se gasta por día de viaje.
# Están en mayúscula porque no cambian durante el programa.
COMBUSTIBLE_POR_DIA = 8
OXIGENO_POR_TRIPULANTE = 2
ENERGIA_POR_DIA = 5
PROVISIONES_POR_TRIPULANTE = 1

# Entradas: el estado de la nave al terminar la exploración.
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días del viaje de ida: "))
combustible = int(input("Combustible disponible: "))
oxigeno = int(input("Oxígeno disponible: "))
energia = int(input("Energía disponible: "))
provisiones = int(input("Provisiones disponibles: "))

# El oxígeno y las provisiones por día dependen de cuántos tripulantes hay.
oxigeno_por_dia = cantidad_tripulantes * OXIGENO_POR_TRIPULANTE
provisiones_por_dia = cantidad_tripulantes * PROVISIONES_POR_TRIPULANTE

# El regreso dura lo mismo que la ida; aquí no se suma la reserva.
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA

# Decisión principal: si alcanza el combustible se intenta el regreso (caso A);
# si no, la tripulación queda varada (caso B).
if combustible >= combustible_regreso:
    # Caso A: contador de días en 0 y variable de control en True para iniciar el ciclo.
    dias_completados = 0
    puede_continuar = True

    # El ciclo se repite mientras falten días y los recursos alcancen.
    while dias_completados < dias_viaje and puede_continuar:
        # Se revisa primero si alcanzan los cuatro recursos para no quedar en negativo.
        if combustible >= COMBUSTIBLE_POR_DIA and oxigeno >= oxigeno_por_dia and energia >= ENERGIA_POR_DIA and provisiones >= provisiones_por_dia:
            combustible = combustible - COMBUSTIBLE_POR_DIA
            oxigeno = oxigeno - oxigeno_por_dia
            energia = energia - ENERGIA_POR_DIA
            provisiones = provisiones - provisiones_por_dia
            dias_completados = dias_completados + 1
            print("Día", dias_completados, "| Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
        else:
            # Si algo no alcanza, ese día no se gasta nada y se cambia la variable de control para salir del ciclo.
            puede_continuar = False

    # Al salir del ciclo se revisa si se completaron todos los días.
    if dias_completados == dias_viaje:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")
    else:
        # El día que falló es el siguiente a los completados.
        print("El regreso se interrumpió en el día", str(dias_completados + 1) + ".")
        # El combustible no se revisa aquí porque ya se verificó al inicio.
        if oxigeno < oxigeno_por_dia:
            print("Recurso insuficiente: oxígeno")
        if energia < ENERGIA_POR_DIA:
            print("Recurso insuficiente: energía")
        if provisiones < provisiones_por_dia:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
else:
    # Caso B: no hay combustible para volver, la tripulación queda varada.
    print("La tripulación quedó varada en el destino.")

    # División entera (//): solo cuentan los días completos que alcanza cada recurso.
    dias_oxigeno = oxigeno // oxigeno_por_dia
    dias_energia = energia // ENERGIA_POR_DIA
    dias_provisiones = provisiones // provisiones_por_dia

    # Se busca el menor de los tres comparando uno por uno, porque el curso no permite min().
    supervivencia = dias_oxigeno
    if dias_energia < supervivencia:
        supervivencia = dias_energia
    if dias_provisiones < supervivencia:
        supervivencia = dias_provisiones

    # Se arma el texto con todos los recursos que empatan en el menor valor;
    # si ya hay uno escrito, se agrega una coma antes del siguiente.
    recursos_limitantes = ""
    if dias_oxigeno == supervivencia:
        recursos_limitantes = "oxígeno"
    if dias_energia == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes = recursos_limitantes + ", energía"
    if dias_provisiones == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"

    # Resumen final del caso B.
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)
    print("Supervivencia estimada:", supervivencia, "días")
    print("Recurso(s) limitante(s):", recursos_limitantes)