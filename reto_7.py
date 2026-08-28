NOTA_MINIMA = 3.0

print("=" * 34)
print("  BOLETÍN DE CALIFICACIONES")
print("=" * 34)

nombre = input("Nombre del estudiante: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3
mejor = max(n1, n2, n3)
aprobo = promedio >= NOTA_MINIMA

estado = "APROBADO" if aprobo else "REPROBADO"

print(f"\nEstudiante: {nombre.title()}")
print(f"Promedio:   {promedio:.2f}")
print(f"Mejor nota: {mejor:.1f}")
print(f"Estado:     {estado}")

if promedio >= 4.5:
    print("Desempeño: SUPERIOR 🏆 (¡Postúlate a proyectos de investigación!)")
elif promedio >= 4.0:
    print("Desempeño: ALTO ⭐ (Mantienes un ritmo excelente)")
elif promedio >= NOTA_MINIMA:
    print("Desempeño: BÁSICO 👍 (Aprobaste, pero no te confíes)")
else:
    print("Desempeño: BAJO ⚠️ (Pide asesoría con tu docente)")

print("\n¿Qué quieres hacer? (repasar / mejorar / beca / salir)")
accion = input("> ").lower()

match accion:
    case "repasar":
        print("Empieza por repasar la materia donde sacaste la nota más baja.")
    case "mejorar":
        falta = round((4.0 * 3) - (n1 + n2 + n3), 2)
        if falta > 0:
            print(f"Para llegar a 4.0 te faltan {falta} puntos en total.")
        else:
            print("¡Ya superaste la meta de 4.0!")
    case "beca":
        if promedio >= 4.5:
            print("¡Felicidades! Calificas para el 100% de beca académica.")
        elif promedio >= 4.0:
            print("Calificas para un descuento del 50% por buen rendimiento.")
        else:
            print("Para aplicar a una beca necesitas un promedio mínimo de 4.0.")
    case "salir":
        print("¡Hasta la próxima!")
    case _:
        print("No entendí esa opción.")