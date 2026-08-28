nombre = "Vanessa"
edad = 17
estatura = 1.62
tiene_mascota = False
videojuego_favorito = "Outlast"
horas_de_sueno = 7

print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(tiene_mascota))
print(type(videojuego_favorito))
print(type(horas_de_sueno))

# Provocar el error a propósito
print("Tengo " + 17 + " años")

# Forma 1 de arreglarlo: usando str() para convertir los enteros a texto
print("Tengo " + str(17) + " años")

# Forma 2 de arreglarlo: usando comas para separar los argumentos en el print
print("Tengo", 17, "años")

print(0.1 + 0.2)      
print(round(0.1 + 0.2, 2)) 