
RESERVA_COMBUSTIBLE = 10

combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

if combustible_disponible >= combustible_total and oxigeno_disponible >= oxigeno_requerido and energia_disponible >= energia_requerida and provisiones_disponibles >= provisiones_requeridas:
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
