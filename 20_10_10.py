edad = int(input("Ingrese su edad: "))
es_estudiante = input("Es estudiante? responda con True/False: ")
es_estudiante = es_estudiante.strip() == "True"
if edad < 18 or es_estudiante:
    print("Descuento")
else: 
    print("Precio regular")
    
print("pago realizado")

