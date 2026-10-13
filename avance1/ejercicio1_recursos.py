# Constantes
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
OXIGENO_POR_TRIPULANTE = 2
RESERVA_OXIGENO = 5
TRAYECTOS_IDA_REGRESO = 2
ENERGIA_POR_DIA = 5
ENERGIA_PARA_EXPLORACION = 10
PROVISIONES_POR_TRIPULANTE = 1
RESERVA_PROVISIONES = 3

# Entrada de datos
nombre_mision = input("Nombre de la misión: ")
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días de viaje: "))

# Procesamiento: cálculo de recursos
combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
oxigeno_requerido = dias_viaje * OXIGENO_POR_TRIPULANTE * TRAYECTOS_IDA_REGRESO * cantidad_tripulantes + RESERVA_OXIGENO
energia_requerida = dias_viaje * ENERGIA_POR_DIA * TRAYECTOS_IDA_REGRESO + ENERGIA_PARA_EXPLORACION
provisiones_requeridas = dias_viaje * PROVISIONES_POR_TRIPULANTE * cantidad_tripulantes * TRAYECTOS_IDA_REGRESO + RESERVA_PROVISIONES

# Salida de resultados
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