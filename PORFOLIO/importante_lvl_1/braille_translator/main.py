from base import *
def tablaBase(p1, p2, p3, p4, p5, p6):
    return [p1, p4, p2, p5, p3, p6]  # Mantiene el orden para cada posición específica

# Definir el alfabeto en braille
abecedario = {
    ' ': tablaBase(0, 0, 0, 0, 0, 0),
    'a': tablaBase(1, 0, 0, 0, 0, 0),
    'b': tablaBase(1, 0, 1, 0, 0, 0),
    'c': tablaBase(1, 1, 0, 0, 0, 0),
    'd': tablaBase(1, 1, 0, 1, 0, 0),
    'e': tablaBase(1, 0, 0, 1, 0, 0),
    'f': tablaBase(1, 1, 1, 0, 0, 0),
    'g': tablaBase(1, 1, 1, 1, 0, 0),
    'h': tablaBase(1, 0, 1, 1, 0, 0),
    'i': tablaBase(0, 1, 1, 0, 0, 0),
    'j': tablaBase(0, 1, 1, 1, 0, 0),
    'k': tablaBase(1, 0, 0, 0, 1, 0),
    'l': tablaBase(1, 0, 1, 0, 1, 0),
    'm': tablaBase(1, 1, 0, 0, 1, 0),
    'n': tablaBase(1, 1, 0, 1, 1, 0),
    'ñ': tablaBase(1, 1, 1, 1, 0, 1),
    'o': tablaBase(1, 0, 0, 1, 1, 0),
    'p': tablaBase(1, 1, 1, 0, 1, 0),
    'q': tablaBase(1, 1, 1, 1, 1, 0),
    'r': tablaBase(1, 0, 1, 1, 1, 0),
    's': tablaBase(0, 1, 1, 0, 1, 0),
    't': tablaBase(0, 1, 1, 1, 1, 0),
    'u': tablaBase(1, 0, 0, 0, 1, 1),
    'v': tablaBase(1, 0, 1, 0, 1, 1),
    'w': tablaBase(0, 1, 1, 1, 0, 1),
    'x': tablaBase(1, 1, 0, 0, 1, 1),
    'y': tablaBase(1, 1, 0, 1, 1, 1),
    'z': tablaBase(1, 0, 0, 1, 1, 1),
}

# Función para representar la letra en braille y retornarla como un string
def braille(letra):
    # Crear la representación en formato de 3x2 (columnas)
    if letra not in abecedario:
        return "Letra no válida"
    else:
        puntos = abecedario[letra]
        braille_visual = [
            f"{'•' if puntos[0] else ' '} {'•' if puntos[3] else ' '}",
            f"{'•' if puntos[1] else ' '} {'•' if puntos[4] else ' '}",
            f"{'•' if puntos[2] else ' '} {'•' if puntos[5] else ' '}"
        ]
    # Unir las líneas para pasarlo a `encuadrar`
    return '\n'.join(braille_visual)

palabra = input("Ingrese una letra del abecedario (a-z, ñ): ").lower()
# Usar `encuadrar` para cada letra en el abecedario
print(f"Braille para '{palabra}':")
for letra in palabra:
    print(encuadrar(braille(letra)))
