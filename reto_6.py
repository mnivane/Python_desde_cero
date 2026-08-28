edad = int(input("Ingresa la edad: "))

if edad < 0:
    print("Edad no válida")
elif edad <= 11:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")

temperatura = 28

# Operador ternario guardado en variable
mensaje = "Hace calor" if temperatura > 25 else "Está fresco"
print(mensaje)

# Ternario escrito directamente dentro de la f-string
print(f"El clima hoy: {'Hace calor' if temperatura > 25 else 'Está fresco'}")

print("Opciones de menú:")
print("1. Consultar nota")
print("2. Calcular promedio")
print("3. Centro de ayuda")
print("4. Salir")
opcion = input("Selecciona una opción (1-4): ")

match opcion:
    case "1":
        print("Consultando nota...")
    case "2":
        print("Calculando promedio...")
    case "3":
        print("Centro de ayuda.")
    case "4":
        print("Saliendo del programa...")
    case _:
        print("Opción no válida. Intenta de nuevo.")

nota = 5.0

if nota >= 3.0:
    print("Aprobado")
elif nota >= 4.5:
    print("Excelente")