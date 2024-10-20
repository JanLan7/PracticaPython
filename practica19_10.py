miembros_iniciales = int(input("Introduce el número inicial de miembros del grupo: "))
dias_observacion = int(input("Introduce el número de días de observación: "))

for dia in range(1, dias_observacion + 1):
    miembros_iniciales *= 2
    print(f"Al final del día {dia}, el grupo tiene {miembros_iniciales} miembros")

