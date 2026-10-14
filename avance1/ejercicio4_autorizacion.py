# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Esteban Víquez Rodríguez
# Fecha: 14/10/2026        Versión: 1.0
# Descripción: Revisa todos los recursos y decide si se
#              autoriza o no el lanzamiento de la misión.
# ============================================================

# Valor fijo de la misión: combustible extra para emergencias.
RESERVA_COMBUSTIBLE = 10

# Le pido al usuario lo que hay y lo que se necesita de cada recurso.
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Sumo ida, regreso y reserva, porque la nave tiene que poder volver.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Solo se autoriza si alcanzan los cuatro recursos a la vez, por eso uso and.
# El combustible lo comparo contra el total, no solo contra la ida.
if combustible_disponible >= combustible_total and oxigeno_disponible >= oxigeno_requerido and energia_disponible >= energia_requerida and provisiones_disponibles >= provisiones_requeridas:
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")