# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Esteban Víquez Rodríguez
# Fecha: 13/10/2026        Versión: 1.0
# Descripción: Verifica si la nave tiene oxígeno y provisiones
#              suficientes para la tripulación.
# ============================================================

# Le pido al usuario lo que hay y lo que se necesita de cada recurso.
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Solo alcanza si se cumplen las dos cosas a la vez, por eso uso and.
# Uso >= porque si hay justo lo necesario, también alcanza.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")