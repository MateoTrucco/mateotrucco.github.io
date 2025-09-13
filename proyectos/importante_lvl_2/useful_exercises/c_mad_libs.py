"""
===============
    MAD LIB
===============

En este juego, se pedirán diferentes preguntas al usuario
para obtener información para crear una historia.
Cuando se tengan todas las entradas necesarias,
se puede reorganizar la información para crear una historia
divertida y única.

¡Espero que te diviertas jugando!
"""
from ....base_functions import *

write("\nSe te van a hacer unas preguntas para un divertido Mat Lib\n")

while True:
       wait()
       nombre_persona = wInput("\n¿Cuál es tu nombre?: ")
       wait()
       nombre_cumbia = wInput("\n¿Cuál es el nombre de tu grupo de cumbia favorita?: ")
       wait()
       nombre_objeto = wInput("\n¿Cuál es el nombre de tu comida favorita?: ")
       wait()
       nombre_bebida = wInput("\n¿Cuál es el nombre de tu bebida favorita?: ")
       wait()
       adjetivo_singular = wInput("\n¿Cuál es un adjetivo singular?: ")
       wait()
       adjetivo_plural = wInput("\n¿Cuál es un adjetivo plural?: ")
       wait()
       adjetivo_singular2 = wInput("\n¿Cuál es un adjetivo singular?: ")
       wait()
       nombre_lugar = wInput("\n¿Cuál es el nombre de tu lugar favorito?: ")

       wait()
       write(encuadrar(f"""\n
Anoche, en lo de {nombre_persona},
todo estaba listo para la fiesta.
La música estaba a todo volumen y la pista de baile
estaba llena de gente moviéndose al ritmo de {nombre_cumbia}.
De repente, {nombre_persona} quiso armar alboroto.
Agarró un {nombre_objeto}, lo lanzó al aire
y exclamó: "¡Atrapen este {nombre_objeto}!"
Todos en la fiesta se miraron entre sí
con una sonrisa pícara y rápidamente
se unieron al juego.
El {nombre_objeto} volaba de un lado a otro
mientras la gente saltaba para atraparlo.
¡Fue una locura total! El {nombre_objeto} chocó
contra una botella de {nombre_bebida}
y se hizo añicos, dejando a todos
atónitos.
Después de un momento de {adjetivo_singular}, alguien
soltó una carcajada y pronto toda la
habitación se llenó de risas.
A pesar del desastre, la fiesta en
{nombre_lugar} se convirtió en una
de las más divertidas que {nombre_persona}
y sus amigos habían tenido en la vida.
       """), 0.01)
       
       playAgain()
