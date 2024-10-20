miembros_iniciales = int(input())
dias_observacion = int(input())

for dia in range(1, dias_observacion + 1):
    miembros_iniciales *= 2
    print(f"Al final del día {dia}, el grupo tiene {miembros_iniciales} miembros")

