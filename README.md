# 🐍 Python Desde Cero — Guía Teórica y Práctica (Niveles 1–7)

Bienvenido/a al repositorio del **Tomo 1: Niveles 1 al 7** de la serie *Python Desde Cero*. Este proyecto documenta el viaje desde escribir la primera línea de código hasta la construcción de programas interactivos con manejo de decisiones, formato avanzado y depuración de errores.

---

## 🗺️ Mapa del Curso

| Nivel | Tema | Descripción |
| :---: | :--- | :--- |
| **1** | **Los Cimientos** | ¿Qué es Python? Intérprete, archivos `.py`, filosofía (Zen de Python) y su rol en IA. |
| **2** | **Primer Programa** | Dominio de `print()`, comillas, secuencias de escape (`\n`, `\t`), `sep`, `end` y comentarios `#`. |
| **3** | **La Memoria** | Variables y los 4 tipos básicos (`int`, `float`, `str`, `bool`), asignación y tipado dinámico/fuerte. |
| **4** | **Conversación** | `input()`, conversión de tipos (*casting*) y formato moderno con `f-strings` (`:.2f`, alineación). |
| **5** | **Las Herramientas**| Operadores aritméticos (incluyendo `/`, `//` y `%`), de comparación, lógicos (`and`, `or`, `not`) y precedencia. |
| **6** | **El Poder de Decidir** | Toma de decisiones con `if`, `elif`, `else`, operador ternario y coincidencia de patrones (`match-case`). |
| **7** | **El Jefe Final** | Diagnóstico de errores (`Traceback`), depuración, buenas prácticas (PEP 8) y **Proyecto Final**. |

---

## 🚀 Proyecto Final: Boletín Inteligente (`boletin.py`)

El proyecto integrador de este tomo combina todos los conceptos aprendidos en un solo programa que calcula promedios, determina el desempeño académico de un estudiante, genera recomendaciones personalizadas y corrige situaciones límite (*edge cases*).

### 🛠️ Características del Boletín
- **Entrada interactiva y conversión:** Captura el nombre y 3 notas en coma flotante.
- **Formato dinámico (`f-strings`):** Salida tabulada con formateo a dos decimales (`:.2f`).
- **Lógica de evaluación:** Uso de expresiones relacionales y constantes para verificar la aprobación.
- **Evaluación jerárquica (`if-elif-else`):** Clasificación en desempeño SUPERIOR, ALTO, BÁSICO o BAJO.
- **Menu interactivo (`match-case`):** Sistema de consulta con patrones de coincidencias y manejo de casos comodín (`case _`).
- **Manejo de Caso Borde:** Lógica ajustada para felicitar al estudiante si su promedio ya superó la meta requerida.

---

## 💻 Instrucciones de Ejecución

### Prerrequisitos
- Tener instalado **Python 3.10** o superior (necesario para el uso de la estructura `match-case`).

### Pasos para ejecutar

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/python-desde-cero.git](https://github.com/tu-usuario/python-desde-cero.git)
   cd python-desde-cero
