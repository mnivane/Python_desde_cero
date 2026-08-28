a = 17
b = 5

print(f"suma: {a + b}")
print(f"resta: {a - b}")
print(f"multiplicación: {a * b}")
print(f"división : {a / b}")
print(f"división entera: {a // b}")
print(f"módulo: {a % b}")
print(f"potencia: {a ** b}")

numero = int(input("Ingresa un número: "))

es_par = numero % 2 == 0
es_multiplo_3 = numero % 3 == 0
en_rango = 1 <= numero <= 100  
print(f"¿Es par?: {es_par}")
print(f"¿Es múltiplo de 3?: {es_multiplo_3}")
print(f"¿Está entre 1 y 100?: {en_rango}")

precio = 45000
talla = "M"
color = "negro"
hay_stock = True

cumple_busqueda = (precio <= 50000) and (talla == "M") and (color == "negro") and hay_stock

print(f"¿El producto cumple los requisitos?: {cumple_busqueda}")