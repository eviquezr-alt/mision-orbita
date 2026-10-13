# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Esteban Víquez Rodríguez
# Fecha: 12/10/2026        Versión: 1.0
# Descripción: Calcula los recursos necesarios (combustible,
#              oxígeno, energía y provisiones) para una misión.
# ============================================================

# Valores fijos de la misión.
# Los dejo aquí arriba para que sea fácil cambiarlos si hace falta.
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
OXIGENO_POR_TRIPULANTE = 2
RESERVA_OXIGENO = 5
TRAYECTOS_IDA_REGRESO = 2
ENERGIA_POR_DIA = 5
ENERGIA_PARA_EXPLORACION = 10
PROVISIONES_POR_TRIPULANTE = 1
RESERVA_PROVISIONES = 3

# Le pido al usuario los datos de la misión.
# Los tripulantes y los días los paso a número para poder hacer las cuentas.
nombre_mision = input("Nombre de la misión: ")
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días de viaje: "))

# Calculo el combustible.
# Ir y volver tardan lo mismo, por eso los dos usan los mismos días.
combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA

# Sumo ida, regreso y la reserva, porque la nave tiene que poder volver.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Calculo oxígeno, energía y provisiones.
# Multiplico por los dos trayectos porque se gastan al ir y al volver.
oxigeno_requerido = dias_viaje * OXIGENO_POR_TRIPULANTE * TRAYECTOS_IDA_REGRESO * cantidad_tripulantes + RESERVA_OXIGENO
energia_requerida = dias_viaje * ENERGIA_POR_DIA * TRAYECTOS_IDA_REGRESO + ENERGIA_PARA_EXPLORACION
provisiones_requeridas = dias_viaje * PROVISIONES_POR_TRIPULANTE * cantidad_tripulantes * TRAYECTOS_IDA_REGRESO + RESERVA_PROVISIONES

# Muestro el resumen de la misión en el mismo orden que pide la consigna.
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")