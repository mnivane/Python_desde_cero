nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio final es: {promedio:.2f}")

nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))
ciudad = input("Ingresa la ciudad: ")

año_cumple_30 = 2026 + (30 - edad)

print(f"Hola, mi nombre es {nombre}, vivo en {ciudad} y tengo {edad} años. En el año {2026 + (30 - edad)} cumpliré 30 años.")

# Encabezados
print(f"{'Nombre':<15} | {'Edad':^5} | {'Nota':>6}")
print("-" * 32)

# Filas de estudiantes
print(f"{'Vane':<15} | {17:^5} | {4.8:>6.1f}")
print(f"{'Alejandro':<15} | {18:^5} | {4.2:>6.1f}")
print(f"{'Santiago':<15} | {19:^5} | {3.9:>6.1f}")