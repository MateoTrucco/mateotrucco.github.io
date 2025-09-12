"""
============================
    CONTADOR DE PALABRAS
============================

¡Bienvenido al juego del conteo de palabras!

En este juego, se te pedirá una frase y
se te indicará el número de palabras que
contiene. ¡Vamos a empezar!

--------------
"""

from a_funciones_basicas import *

while True:
    frase = wInput("\n¿En qué esta pensando? (Escribe una frase):").split()

    wait()
    write(f"\nLa frase tiene {len(frase)} palabras.\n")
    
    playAgain()
