"""
===================
    PAR O IMPAR
===================

Este juego de adivinanzas te pedirá que adivines si un
número entero entre 1 y 1000 es par o impar.

Para empezar, se nos pedirá un número entero.
Cuando se proporcione el número, se comprobará si es
par o impar y, en función del resultado, se imprimirá
un mensaje con el resultado.

Si el número es impar, se imprimirá el mensaje: ¡Es un número impar!
¿Puedes añadir otro?

Si el número es par, se imprimirá el mensaje: ¡Es un número par!
¿Quieres seguir jugando?

¡Disfruta del juego!
"""

from a_funciones_basicas import *

while True:
    wait()
    while True:
        num = wInput("\n¿En qué número estás pensando? (1-1000):")
        try:
            num = int(num)
            break
        except ValueError:
            write("\nPor favor, introduce un NÚMERO\n")
    wait()
    if 1 <= num <= 1000:
        if num % 2 == 0:
            alarm(1)
            write(f"\n¡{num} es un número par!\n")
            playAgain()
        else:
            alarm(2)
            write(f"\n¡{num} es un número impar!\n")
            playAgain()
    else:
        alarm(3)
        write("\nPor favor, introduce un número entre 1 y 1000.\n")
