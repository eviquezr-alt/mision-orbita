# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Esteban Víquez Rodríguez
# Fecha: 13/10/2026        Versión: 1.0
# Descripción: Verifica si la nave tiene combustible suficiente
#              para ir, volver y llevar la reserva.
# ============================================================

# Valores fijos de la misión.
# La reserva es lo extra que se lleva; el margen es lo mínimo que debe sobrar.
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO = 10

# Le pido al usuario los datos del combustible.
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))

# Sumo ida, regreso y reserva, porque la nave tiene que poder volver.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
# Lo que sobra después de apartar todo lo necesario.
combustible_adicional = combustible_disponible - combustible_total

# Estas salidas se muestran siempre, por eso van fuera del if.
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# Si sobra menos del margen mínimo, aviso que el combustible está justo.
if combustible_adicional < MARGEN_MINIMO:
    print("Advertencia: el margen adicional de combustible es bajo.")